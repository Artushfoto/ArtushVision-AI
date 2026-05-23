---
title: "Manual Editing and Detailed Photo View | ArtushVision AI Documentation"
description: "Master granular metadata control in ArtushVision AI. Learn about the keyword bubble system, linguistic tools, multilingual spell check, and interactive GPS mapping."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }

/* Profesionální styl pro klikací screenshoty */
.screenshot-link {
  display: block;
  margin: 20px auto;
  max-width: 100%;
  text-decoration: none;
}
.screenshot-img {
  width: 100%;
  height: auto;
  display: block;
  border: 1px solid #333;
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transition: opacity 0.2s;
}
.screenshot-img:hover {
  opacity: 0.95;
}

/* GitHub Téma vyhledávacího komponentu (Světlý i Tmavý režim) */
#flex-search-container {
  max-width: 500px;
  margin: 25px auto;
  position: relative;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
}

#flex-search-input {
  width: 100%;
  padding: 12px 16px;
  font-size: 14px;
  line-height: 20px;
  border-radius: 6px;
  box-sizing: border-box;
  transition: border-color 0.2s, box-shadow 0.2s, background-color 0.2s, color 0.2s;
  border: 1px solid #d0d7de;
  background-color: #f6f8fa;
  color: #24292f;
}

#flex-search-input::placeholder {
  color: #57606a;
  opacity: 1;
}

#flex-search-input:focus {
  outline: none;
  background-color: #ffffff;
  border-color: #0969da;
  box-shadow: 0 0 0 3px rgba(9, 105, 218, 0.3);
}

#flex-results-container {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  border-radius: 6px;
  list-style: none;
  padding: 0;
  margin: 8px 0 0 0;
  z-index: 100;
  max-height: 300px;
  overflow-y: auto;
  display: none;
  background-color: #ffffff;
  border: 1px solid #d0d7de;
  box-shadow: 0 8px 24px rgba(140, 149, 159, 0.2);
}

#flex-results-container li {
  border-bottom: 1px solid #d0d7de;
}

#flex-results-container li:last-child {
  border-bottom: none;
}

#flex-results-container li a {
  display: block;
  padding: 12px 16px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  color: #24292f;
  transition: background-color 0.1s, color 0.1s;
}

#flex-results-container li a:hover {
  background-color: #0969da;
  color: #ffffff;
}

#flex-results-container .no-results-msg {
  padding: 12px 16px;
  color: #57606a;
  font-style: italic;
  font-size: 14px;
}

@media (prefers-color-scheme: dark) {
  #flex-search-input {
    border: 1px solid #30363d;
    background-color: #0d1117;
    color: #c9d1d9;
  }
  #flex-search-input::placeholder {
    color: #8b949e;
  }
  #flex-search-input:focus {
    border-color: #58a6ff;
    box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.3);
  }
  #flex-results-container {
    background-color: #161b22;
    border: 1px solid #30363d;
    box-shadow: 0 8px 24px rgba(1, 4, 9, 0.8);
  }
  #flex-results-container li {
    border-bottom: 1px solid #21262d;
  }
  #flex-results-container li a {
    color: #c9d1d9;
  }
  #flex-results-container li a:hover {
    background-color: #1f6feb;
    color: #ffffff;
  }
  #flex-results-container .no-results-msg {
    color: #8b949e;
  }
}
</style>
</div>

# Detail Window Overview

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**While AI provides the speed, the Detailed Photo View provides the precision. ArtushVision AI offers a sophisticated environment for granular metadata refinement, ensuring every asset meets professional commercial standards.**

Double-click any image in the main grid to enter the Detailed Photo View. This dedicated workspace is designed for high-speed **manual editing**, linguistic verification, and geospatial accuracy.

The interface is divided into two main vertical panels with flexible splitters, allowing you to customize the layout exactly to your needs.


`Double-click any image in the main grid`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/detail-window-overview" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/detail-window-overview.png" alt="ArtushVision AI - Sample of Cloud AI Prompt" width="100%" class="screenshot-img">
  </a>

---

## Left Panel: Preview and Navigation
This section is dedicated to the photo itself and its technical information.

*   **Image Preview:** Displays the photo. It first instantly loads a smaller thumbnail from the cache, followed by a smooth (fade-in) display of the full-resolution image or a generated preview from RAW/video files.
*   **Info Strip:** A persistently displayed label below the photo containing the filename and key EXIF data:
    *   *Example:* `ISO 100 | f/8.0 | 1/250s | 50mm`
    *   It also shows the resolution (e.g., 6000x4000) and file size in megabytes.
*   **Information Badges:** If the photo has specific properties (GPS, XMP sidecar, Video, corrupted data, TTP Upload, etc.), corresponding micro-icons are displayed directly in the left column.
*   **Navigation (‹ and ›):** Large round buttons (or keyboard arrows) allow you to seamlessly browse through all photos in the current grid without needing to close the window. Metadata, the image, and the map update instantly.

---

## 2. Right Panel: Main Toolbar
This toolbar is used to trigger actions for the currently displayed photo.

*   **Profile and AI Hint:** 
    *   *Profile:* Selects the set of instructions for the Artificial Intelligence.
    *   *Hint:* Specific text (e.g., exact location, rare animal species) that the AI will consider when analyzing this specific photo.
*   **Run AI:** The primary button (colored based on the current mode: Cloud/Local/Hybrid) that performs the image analysis and populates the Title, Description, and Keywords fields.
*   **Quick Action Buttons:**
    *   **Getty...:** Opens the Getty Optimizer tool for tag translation and commercial mapping.
    *   **Show on map:** Opens the photo's location in a large external browser.
    *   **EXIF data:** Opens a table with a complete list of all raw EXIF/IPTC data.
    *   **Restore:** Discards unsaved changes and reloads fresh data from the file on disk (or XMP/CSV backup).
    *   **Open / Rename:** System functions to open the photo in an external editor or change the filename (including XMP sidecars).
*   **OK / Cancel:** The **OK** button confirms your changes, writes them back to the main grid, and initiates saving.

---

## 3. Metadata Editing Fields
Three main blocks (Title, Description, Keywords). The height of each block can be vertically adjusted using the splitters.

*   **Field Headers:** Display character and word counters (`Chars | Words`). They turn red if stock photo limits are exceeded.
*   **Quick Clear and Copy:** Each header has a cross (`×`) for instantly clearing the field and a clipboard icon to copy its content. The keywords section also features an **All** button to copy all metadata at once.
*   **Rating and Sorting (next to Title):** 
    *   Five-star rating (1-5 ★).
    *   Flag (Pick / Reject).
    *   Color label (Red, Yellow, Green, etc.).
*   **Categories (next to Description):** The `✎ Categories` button shows and allows you to edit up to 3 Master Categories (stock photography categories, Editorial, Mature, etc.) and the assigned country.
*   **Keywords:**
    *   The **AZ ↓** button sorts tags alphabetically.
    *   The **Keywords** checkbox toggles between plain text editing and interactive bubbles.
    *   **Local Undo/Redo (`↩` / `↪`):** Dedicated step history buttons exclusively for the tags of the current photo.
*   **Translator and Spellcheck:** The editors fully support spell checking, underlining typos, and showing translations on hover (can be toggled via the *Translate* option). Double-clicking a word opens the Synonyms and spelling suggestions window.

---

## 4. Interactive Map (Map View)
If the photo contains GPS coordinates, a map background is displayed at the bottom of the right panel.

*   **Instant Loading:** The map utilizes browser rendering engine *pre-warming*. When browsing photos, the map updates smoothly without annoying flickering or delays.
*   **Show/Hide:** The map can be toggled on or hidden using the globe button 🌍 located in the keywords header.
*   **Map Modes:** In the global application settings, you can choose whether you prefer Google Maps or OpenStreetMap as your provider.

---

### Professional Workflow in 3 Steps:

1. **Double-Click to Refine:** Open the Detail View for any asset that requires specific manual attention.
2. **Reorder and Verify:** Use the bubble system to prioritize keywords and use the spell-checker to ensure professional quality.
3. **Save and Synchronize:** Click Save to commit changes to the XMP metadata, making them instantly available for Lightroom, Bridge, or the <a href="/docs/global-stock-distribution-ftp.html">Smart FTP Uploader</a>.

---

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*