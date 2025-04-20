
# 🧠 1001Fonts Scraper & Downloader

This repository contains scripts for scraping and downloading fonts from **[1001fonts.com](https://www.1001fonts.com/)**. The process is divided into two steps:

1. **Scrape Font Metadata and Images**
2. **Download Font ZIP Files**

---

## 📁 Project Structure

```
.
├── 1001fonts/
│   ├── scrape_1001fonts.py          # Step 1: Scrape 1001fonts metadata + preview images
│   ├── download_fonts_1001fonts.py  # Step 2: Download 1001fonts zip fonts
│   ├── font/                        # Preview images saved here
│   ├── downloaded_fonts/            # Final zip files go here
│   └── fonts_data_1001fonts.json    # Font metadata from 1001fonts
│
├── README.md                        # You're here!
└── requirements.txt
```

---

## 📦 Install Dependencies

To install the required libraries for this project, run the following command:

```bash
pip install -r requirements.txt
```

**requirements.txt**:

```
requests
beautifulsoup4
html5lib
rich
```

---

## 🔤 1001Fonts Workflow

### Step 1: Scrape Font Data from 1001fonts

To scrape font metadata (name, image, download link) and preview images:

```bash
cd 1001fonts
python scrape_1001fonts.py
```

- This script will scrape the font listings from 1001fonts.
- The metadata (such as font names, preview images, download links) will be saved to `fonts_data_1001fonts.json`.
- Preview images will be saved to the `font/` folder.

---

### Step 2: Download Font ZIP Files

To download the font ZIP files:

```bash
python download_fonts_1001fonts.py
```

- This script will check whether each font ZIP file has already been downloaded.
- If not, it will download the ZIP file and save it to the `downloaded_fonts/` folder.

**Note**: Before running the downloader, you can manually remove unwanted font previews from the `font/` folder. The downloader will only download ZIP files for the remaining fonts.

---

## 🎯 Summary

- **Step 1 (Scraping)**: Scrapes metadata and saves font preview images.
- **Step 2 (Downloader)**: Downloads font ZIP files if not already downloaded.

---

## 🧹 Clean-up Before Download

Before starting the downloading process:
- Go to the `font/` folder and remove any unwanted font preview images.
- This ensures that only the selected fonts' ZIP files are downloaded.

---

## 🖤 Happy Scraping & Font Hunting!

If you have any questions or issues, feel free to open an issue in the repository.
