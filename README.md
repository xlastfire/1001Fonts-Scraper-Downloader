# 🎯 1001Fonts-Scraper-Downloader

A two-step Python project that helps you scrape font metadata and preview images from **[1001fonts.com](https://www.1001fonts.com/)**, filter them manually, and download only the desired fonts automatically.

---

## ✨ Features

- 🔍 Scrape all font names, images, and direct ZIP download links.
- 🖼️ Download font preview images and store them in the `font/` folder.
- 🧹 Easily review images and delete unwanted fonts.
- ⬇️ Download filtered font ZIPs using a separate downloader script.
- ⚡ Uses `concurrent.futures` and `rich` for fast performance with beautiful progress bars.
- 🧠 Avoids re-downloading already available files.
- 📁 Organized into clean folders and JSON metadata for extensibility.

---

## 🧠 How It Works

### 📄 Step 1: Run `1001font_scraper.py`

This script will:

1. Scrape all paginated font listings from 1001fonts.com.
2. Extract:
   - Font title
   - Direct font ZIP download link
   - Preview image link
3. Assign a **unique ID** for each font.
4. Save all data into `fonts_data_1001fonts.json`.
5. Download and save preview images into the `font/` folder, named by their unique ID (e.g., `abc123.png`).

---

### 📄 Step 2: Run `1001font_downloader.py`

After you manually **review and delete** preview images you don't want:

1. This script loads `fonts_data_1001fonts.json`.
2. It checks for each font:
   - If the preview image still exists → keep.
   - If the ZIP file is already downloaded → skip.
   - If not downloaded → download into `downloaded_fonts/`, named by unique ID.

✅ You get only the fonts you want, without duplicates!

---

## 📦 Project Structure

```
1001Fonts-Scraper-Downloader/
├── 1001font_scraper.py           # Step 1: Scrape metadata and preview images
├── 1001font_downloader.py        # Step 2: Download ZIP font files
├── requirements.txt              # Python dependencies
├── readme.md                     # This documentation
├── fonts_data_1001fonts.json     # Auto-generated JSON of font metadata
├── font/                         # Preview images downloaded here
└── downloaded_fonts/             # ZIP files downloaded here
```

---

## 🛠️ Requirements

Install all required Python libraries using:

```bash
pip install -r requirements.txt
```

> **Python 3.7+ recommended**

---

## 📥 Example Entry in `fonts_data_1001fonts.json`

```json
{
  "id": "abc123",
  "title": "Cool Font",
  "font_image": "https://www.1001fonts.com/path-to-image.png",
  "font_link": "https://www.1001fonts.com/download/cool-font.zip"
}
```

---

## 🚀 Usage

### 🔎 Step 1 - Scrape and Save Fonts

```bash
python 1001font_scraper.py
```

This will populate:

- `fonts_data_1001fonts.json`
- Preview images inside `font/`

🔍 **Manually delete** unwanted font previews from the `font/` folder.

---

### 📥 Step 2 - Download Selected Fonts

```bash
python 1001font_downloader.py
```

Only the fonts whose preview images still exist will be downloaded into the `downloaded_fonts/` folder.

---

## 🧹 Cleanup Tip

After downloading, you may optionally clean up the `font/` folder if not needed anymore.

---

## 💡 Use Cases

- Curate your own font collection 🎨
- Offline font library for design projects 💻
- Font previews for typography research 🔠

---

## 📌 Notes

- This project is for **educational and personal use**.
- Always respect the site's Terms of Service.

---


## 🧑‍💻 Author

Made with ❤️ by [@xlastfire](https://github.com/xlastfire)
