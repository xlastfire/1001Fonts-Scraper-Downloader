import requests
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from rich.progress import Progress, BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn
import logging

# Setup
json_file = 'fonts_data_1001fonts.json'
output_dir = Path('downloaded_fonts')
output_dir.mkdir(exist_ok=True)

# Logging
logging.basicConfig(
    filename='download_fonts_1001fonts.log',
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s',
)

# Load font data
with open(json_file, 'r', encoding='utf-8') as f:
    fonts = json.load(f)

headers = {
    'User-Agent': 'Mozilla/5.0'
}


def download_font(font, progress, task_id):
    font_id = font['id']
    font_url = font['font_link']
    zip_path = output_dir / f"{font_id}.zip"

    if zip_path.exists():
        logging.info(f"📦 Already downloaded: {font_id}")
        progress.update(task_id, completed=1)
        return

    try:
        with requests.get(font_url, headers=headers, stream=True, timeout=30) as r:
            r.raise_for_status()
            total = int(r.headers.get('Content-Length', 0))
            progress.update(task_id, total=1)

            with open(zip_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        logging.info(f"✅ Downloaded: {font['title']} ({font_id})")
    except Exception as e:
        logging.error(f"❌ Failed: {font['title']} ({font_id}) - {e}")
    finally:
        progress.update(task_id, completed=1)


# Download with concurrent threads
with Progress(
    "[progress.description]{task.description}",
    BarColumn(),
    DownloadColumn(),
    TransferSpeedColumn(),
    TimeRemainingColumn()
) as progress:

    task = progress.add_task("📥 Downloading fonts...", total=len(fonts))

    with ThreadPoolExecutor(max_workers=8) as executor:
        for font in fonts:
            executor.submit(download_font, font, progress, task)

print("🎉 All available fonts downloaded!")
