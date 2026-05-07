# <center>ArtushVision AI<center>
### The Ultimate AI-Powered Metadata & Keywording Tool for Photographers and Videographers

![Version](https://img.shields.io/badge/Version-v2026.1.0-007abb) ![AI](https://img.shields.io/badge/AI-OpenRouter-ed7d31)

*"Intelligent metadata automation for your Travel, Home, and Stock photography workflow with state-of-the-art Vision AI."*

**ArtushVision AI** is a professional desktop application designed to streamline the workflow of photographers, videographers, and archivists. It leverages state-of-the-art Computer Vision AI (via OpenRouter) to automatically generate keywords, titles, and descriptions for **JPG, RAW, VIDEO, HEIC, TIFF, and PNG** assets, while providing robust tools for manual metadata management. Your data is always safe with automated backups and flexible export options to CSV and XMP sidecars, ensuring you never lose your progress or original file integrity.

> ⚡ **Exceptional Value:** Using our recommended model, **google/gemini-2.0-flash-001**, you can professionally describe approximately **100,000 to 150,000 photos for only $5** with perfect, high-quality results.
> 
> 📊 **Full Cost Control:** Monitor your budget with built-in **spending statistics**. The app provides real-time feedback on the exact cost of every single query.

Beyond AI automation, it offers a complete organization toolkit, including **star ratings, pick/reject flags, and color-coded labels** to help you curate and filter your media with ease. Full compatibility with **Adobe Lightroom, Bridge, Zoner, DigiKam and others**. We use industry-standard IPTC/XMP metadata that works everywhere.

### 🔗 Quick Links
* 📖 [ArtushVision AI - Overview](https://www.artushfoto.eu/Software/ArtushVisionAI)
* 📖 [ArtushVision AI - Basic workflow introduction video](https://www.artushfoto.eu/Software/ArtushVision-AI-basic-workflow)
* 📖 [ArtushVision AI - OpenRouter API Key Setup](https://www.artushfoto.eu/Software/OpenRouter-API-Key-Setup-Guide-for-Beginners)

---

### 📥 Get Started
* [**Download Free Fully Functional Lite Version**](https://www.artushfoto.eu/Software/Download-ArtushVision-AI) – Test the full professional workflow now.
* [**Purchase Lifetime License ($39.99)**](https://www.artushfoto.eu/Software/Purchase-ArtushVision-AI) – One-time payment, no monthly fees. Securely processed by Polar & Stripe.

[Already have a license? Manage or Deactivate your devices](https://www.artushfoto.eu/Software/Manage-ArtushVision-AI-License)

---

## 📋 Table of Contents
1. [ArtushVision AI Overview](#artushvision-ai)
2. [💰 Desktop Power vs. Cloud (Cost & Privacy)](#desktop-vs-cloud)
3. [📈 My Personal Journey: From Expeditions to Automation](#case-study-stock)
4. [✨ Real-World Accuracy: Madagascar Case](#ai-result-demo)
5. [1. Installation & Setup](#1-installation--setup)
6. [2. Interface Overview](#2-interface-overview)
7. [3. AI Analysis Workflow](#3-ai-analysis-workflow)
8. [4. Professional Advanced Tools](#6-advanced-features)
9. [5. Manual Editing & Detail View](#4-manual-editing--detail-view)
10. [6. Batch Operations](#5-batch-operations)
11. [🛡️ Why Professionals Choose ArtushVision AI](#why-professionals-choose)
12. [7. Settings & Configuration](#7-settings--configuration)
13. [8. Keyboard Shortcuts](#8-keyboard-shortcuts)

---

<div id="desktop-vs-cloud"></div>

## 💰 Desktop Application vs. Cloud Services
*Why a dedicated local workstation beats generic cloud uploaders every time.*

| Feature | Typical Online AI Tools | ArtushVision AI (Desktop) |
| :--- | :--- | :--- |
| **Advanced Metadata Management** | Not available / Limited | **Manual control over Title, Keywords, Ratings** |
| **JPG, RAW, Video, TIFF, PNG, HEIC Support** | Not available (JPG only) | **Full Native Support** |
| **Sync & Batch keywording** | Not available | **Sync Metadata & Batch Edit/Replace** |
| **Media Privacy** | Mandatory cloud upload | **Original files stay on your device.** |
| **Pricing Model** | Recurring Subscriptions | **Perpetual License (Only $39.99)** |
| **Cost per 10,000 Photos** | Expensive Credits ($$$) | **Ultra-low (~$0.50 via API)** |

### Cost Comparison (Example for 10,000 photos/year)
* **Online AI Services (Subscription):** ??? USD (High recurring cost)
* **ArtushVision AI (License + API):** ~$45 USD
    * *Gemini 2.0 Flash costs ~$0.50 for 10k assets.*

---

<div id="case-study-stock"></div>

## 📈 My Personal Journey: From Expeditions to Automation
> *"Coming back from a big trip brings a huge headache: a massive pile of over 20,000 RAW photos and videos from my GoPro, phone, and main camera. Typing out descriptions for each one by hand would take months. I needed a smart tool to skip the boring data entry."*

* **❌ The Old Way:** 2-3 mins per photo, ~600 hours of work, language struggles.
* **✅ The AI Way:** Smart recognition, 1,000+ photos tagged while grabbing coffee, consistent trip context using `{folder_context}`.

---

<div id="ai-result-demo"></div>

## ✨ Real-World Accuracy: Madagascar Case
![Portrait of a Woman, Madagascar](https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/sample.jpg)

**Location Identified:** Miandrivazo, Madagascar.

* **Title:** Woman with traditional face paint in Madagascar
* **Description:** Miandrivazo, Madagascar - November 2 2022: A smiling Malagasy woman with traditional face paint and beaded necklace.
* **Keywords:** Miandrivazo, Madagascar, local, woman, face paint, culture, tradition, portrait, beaded necklace, dark hair, curly hair, smile, travel, authentic... (50 tags generated)

---

## 1. Installation & Setup
### System Requirements
* **OS:** Windows 10/11 (64-bit).
* **Internet:** Required for AI analysis, maps, and online spell checking.
* **Dependencies:** Requires `ExifTool` and `FFmpeg` (bundled in the application folders).

### First Launch
1.  Run `ArtushVisionAI.exe`.
2.  **License:** Enter your key or use the Trial version (10 saves / 3 AI calls).
3.  **API Key:** Navigate to **File > API Key** and enter your [OpenRouter Key](https://openrouter.ai).

---

## 2. Interface Overview
### Top Toolbar
* **Profile:** Select AI prompts (Stock, Travel, Family, etc.).
* **Run AI:** Green play button starts analysis for selected images.
* **Absolute Priority AI Hint:** User hints (Latin names/locations) are treated as unquestionable facts.
* **Speed:** Parallel threads (1-20). Higher is faster but uses more CPU.
* **Flat View:** Toggle to see all files from subfolders in a single list.

### Filter Bar
* **Search:** Filter by text (Title, Description, Keywords, Filename).
* **Folder Filtering:** Isolate specific folders with photo counts.
* **Type Filter:** Show only RAW, JPG, Video, HEIF, TIFF, or PNG.

---

## 3. AI Analysis Workflow
1.  **Load Files:** Click **Load Folders** and select your directory.
2.  **Select Files:** Use `Shift+Click` or `Ctrl+Click`.
3.  **Choose Profile:** Select the profile matching your content.
4.  **Run:** Click **Run AI**. Monitor real-time costs and progress.

---

<div id="6-advanced-features"></div>

## 4. Professional Advanced Tools
### 🧠 Custom AI Profiles
* **🌍 AI Visual Geolocation:** AI recognizes landmarks from pixels or live GPS.
* **📝 Text & OCR Recognition:** Extract text from signs using `{text_ocr}`.
* **📸 Technical EXIF Analysis:** Inject `{camera_model}` or `{exposure_info}` for tech tags.
* **🛡️ Metadata Protection:** Preserves existing keywords and People tags.

### Available Variables for AI Prompts
| Variable | Description |
| :--- | :--- |
| `{user_hint}` | Manual hint entered in main window |
| `{folder_context}` | Name of the parent folder |
| `{filename}` | Original filename without extension |
| `{existing_keywords}` | Keywords already saved in the file |
| `{city}` / `{country}` | City and Country from live GPS |
| `{text_ocr}` | Text extracted visually from image |
| `{camera_model}` | Camera or Device model |
| `{exposure_info}` | Shutter, Aperture and ISO |

---

## 5. Manual Editing & Detail View
Double-click any image to enter the **Detail View**.
* **Text Fields:** Edit with real-time counters and spell check.
* **Keyword Bubbles:** Drag and drop to reorder, Blue (AI), Green (Manual), Black (Original).
* **Interactive Map:** Shows GPS location with zoom support.
* **Navigation:** Arrow keys move to the next/previous image.

---

## 6. Batch Operations
Toggle the **Batch Edit** panel (List icon) to modify hundreds of files:
* **Add/Remove:** Appends text or deletes specific words/tags.
* **Replace:** Use `Old->New` format or `Ctrl+H` dialog.
* **Smarter Rename:** Supports `{TITLE}`, `{DATE}`, `{CC}` (counter), `{FOLDER_NAME}`.

---

## 7. Settings & Configuration
* **Appearance:** Adjust thumbnail sizes, font scales, and field heights.
* **AI Diacritics:** Toggle to allow accents in AI outputs (perfect for family albums).
* **CSV Export:** Create templates for AdobeStock, Shutterstock, Alamy, etc.
* **GPS Provider:** Switch between OpenStreetMap and ArcGIS.

---

<div id="8-keyboard-shortcuts"></div>

## 8. Keyboard Shortcuts

### ⌨️ Main Window (Grid)
| Shortcut | Function |
| :--- | :--- |
| `Arrows` | Move in grid |
| `Shift + Arrows` | Range selection |
| `Ctrl + A` | Select all visible |
| `Ctrl + D` | Deselect all |
| `Delete` | Clear metadata of selected |
| `Ctrl + S` | Save selected |
| `Ctrl + C / V` | Copy / Paste metadata |
| `1 - 5` | Set Star Rating |
| `P / X / U` | Flag: Pick / Reject / Unflag |
| `6 - 0` | Color labels (Red, Yellow, Green, Blue, Purple) |

### 🖼️ Detail Window
| Shortcut | Function |
| :--- | :--- |
| `Ctrl + Enter` | Save and Close |
| `Ctrl + S` | Save (window remains open) |
| `Esc` | Close / Cancel |
| `← / →` | Previous / Next photo |
| `Ctrl + ← / →` | Forced navigation (while typing) |
| `M` | Show/Hide map panel |

### 🏷️ Tags (Bubbles) and Text
| Shortcut | Function |
| :--- | :--- |
| `Enter / ,` | Add typed tag |
| `Ctrl + A` | Select all tags in bubbles area |
| `Ctrl + Space` | Trigger autocomplete in text field |
| `Ctrl + Wheel` | Change bubble font size (Synonyms window) |

---
*© 2026 ArtushFoto. All rights reserved.*
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI0NjMwMTEzNV19
-->