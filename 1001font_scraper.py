import requests as req
from bs4 import BeautifulSoup as Soup
import json
import os
import uuid
from rich.progress import track
from pathlib import Path
import logging

# Setup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

# Logging
logging.basicConfig(
    filename='scrape_1001fonts.log',
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s',
)

# Folders
fonts_folder = Path("fonts")
fonts_folder.mkdir(exist_ok=True)

data = []

# Get all page links
main_url = 'https://www.1001fonts.com/'
r = req.get(main_url, headers=headers)
soup = Soup(r.content, 'html5lib')
last_page = int(soup.find('li', class_='end-page page-item').text)
all_links = [f'https://www.1001fonts.com/?page={i}' for i in range(1, last_page + 1)]

# Scrape each page
for link in track(all_links, description="[cyan]🔎 Scraping font pages..."):
    try:
        r = req.get(link, headers=headers)
        soup = Soup(r.content, 'html5lib')
        font_container = soup.find('ul', class_='font-list')
        fonts_tags = font_container.find_all('li')

        for font in fonts_tags:
            try:
                title = font.h6.text.strip()
                font_img = 'https:' + font.picture.source['srcset']
                zip_link = 'https://www.1001fonts.com' + font.find('a', class_='btn btn-success')['href']

                font_id = str(uuid.uuid4())

                # Download preview image
                img_ext = font_img.split('.')[-1].split('?')[0]
                img_path = fonts_folder / f"{font_id}.{img_ext}"
                if not img_path.exists():
                    img_data = req.get(font_img, headers=headers).content
                    img_path.write_bytes(img_data)
                    logging.info(f"🖼️ Saved preview image for '{title}'")
                else:
                    logging.info(f"🖼️ Preview image already exists for '{title}'")

                # Store font metadata
                data.append({
                    'id': font_id,
                    'title': title,
                    'image': str(img_path),
                    'font_link': zip_link
                })
                logging.info(f"✅ Collected font '{title}'")

            except Exception as fe:
                logging.warning(f"⚠️ Error parsing a font tag: {fe}")

    except Exception as e:
        logging.warning(f"❌ Failed to scrape {link}: {e}")

# Save to JSON
json_path = 'fonts_data_1001fonts.json'
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

logging.info(f"📁 JSON file saved: {json_path}")
print(f"\n🎉 All fonts scraped! JSON saved to {json_path}")
