---
title: "ArtushVision AI Interface Overview | Image Grid & Toolbars"
description: "Comprehensive guide to the ArtushVision AI user interface. Learn how to navigate the main image grid, top toolbars, filters, and batch editing panel."
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

# Interface Overview

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**The Image Grid is the central workspace of ArtushVision AI. Designed to handle thousands of high-resolution assets without stuttering, it provides immediate visual feedback, advanced batch editing, and an intuitive drag-and-drop interface for your metadata.**

Instead of hiding data in complex side panels, ArtushVision AI displays the Title, Description, and Keywords directly below every image. This allows you to review and edit entire batches of photos at a single glance.

## Top Toolbar
This bar provides basic application control and triggers AI operations:
*   **Profile:** Select an AI profile (e.g., *Standard Stock Photography*). This defines the instructions given to the AI. Click the Gear icon ⚙️ button to open the Profile Editor.
*   **[Absolute Priority AI Hint:](/docs/advanced-ai-prompting-profiles-variables.html#basic-and-contextual-variables)** Treats manual user hints (e.g., Latin names, specific animal species, obscure landmarks, or lesser-known objects) as unquestionable facts. When this hint is provided, the AI completely eliminates hallucinations, bypassing generic assumptions and strictly anchoring its analysis to your verified input. This is exceptionally useful for images lacking GPS data, where pinpointing the exact location or context from the visual alone would otherwise be nearly impossible.
*   [**Run Cloud AI / Local AI:**](/docs/ai-metadata-generation-cloud-local-ollama.html) The main green (or blue/orange) button to start the AI analysis for the selected photos.
*   **Columns:** Quickly change the number of columns in the grid. The **Auto** option dynamically adjusts the grid to fit the window size.
*   **Speed:** Number of concurrent threads for Cloud AI (recommended 5-15). Determines how many photos are analyzed simultaneously.
*   **Sorting:** Allows you to sort photos by name (A-Z, Z-A) or by date taken (oldest / newest).
*   **Flat View:** Displays all photos from all loaded folders in a single continuous list (hides folder separators).
*   [**Backup (CSV / XMP / JPG):**](/docs/settings-configuration-customization.html#backup-and-data-safety) Quick toggles that determine which backups should be created when saving changes.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/top-toolbar.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/top-toolbar.png" alt="ArtushVision AI - Top Toolbar" width="100%" class="screenshot-img">
</a>

## Filter & Search Bar
Tools for quick navigation and file selection within the current session:
*   **[Smart Search:](/docs/batch-operations-metadata-library-management.html#global-search-and-replace-ctrlh)** Filter by text with **Aa (Case Sensitivity)** and **Target Selector**.
*   **Folder:** Filters the view to show only a specific loaded folder.
*   [**Status Filter:**](/docs/batch-operations-metadata-library-management.html#status-filtering-and-batch-selection) Shows photos based on their current status (All, Selected, Todo, Done, Modified, Corrupted, Exceeded limits, FTP status, etc.).
*   **Type:** Restricts the view to specific file formats (JPG, RAW, Video, TIFF, HEIC, PNG).
*   **[Rating & Labels:](/docs/batch-operations-metadata-library-management.html#status-filtering-and-batch-selection)** Organize your workspace using **Star Ratings (1-5)**, **Color Labels**, and **Pick/Reject Flags** to quickly sort and identify your best shots.
*   **Search:** Full-text search. You can specify the target field (Everywhere, Title, Description, Keywords). Supports case sensitivity (Aa).
*   **Panel Toggles:** The rightmost buttons show/hide the side panels for *Rating* and *Batch Edit*.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/filter-bar.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/filter-bar.png" alt="ArtushVision AI - Filter Bar" width="100%" class="screenshot-img">
</a>

## Batch Edit Bar
The bottom slide-out bar allows for massive metadata operations across the entire selection at once.
*   **Target (Dropdown):** Determines whether the edit affects the Title, Description, Keywords, or All fields.
*   **Add (+):** Appends the specified text to the beginning, end, or as a new tag to all selected items. *Supports dynamic variables* (e.g., `{DATE}`, `{FOLDER_NAME}`, `{C}` as a counter).
*   **Remove (-):** Deletes a specific word or phrase from all selected items.
*   **Replace (⇄):** Opens the text replacement dialog (supports Find Next / Replace All). Can be triggered by `Ctrl+H`.
*   **Categories:** Allows bulk assignment of up to 3 Master Categories (stock photography categories) to the selected photos.
*   **Clear All (×):** Completely erases the chosen fields for the selection.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/toolbar-batch-edit.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/toolbar-batch-edit.png" alt="ArtushVision AI - Batch Edit Toolbar" width="100%" class="screenshot-img">
</a>

## Main Grid (The Image Grid)
The core of the application. Each card in the grid represents a single file and allows direct metadata editing.

### Visual States and Indicators (Cards)
Photo cards change their background color based on their current state:
*   **Gray / White:** Default state, no unsaved changes.
*   **Yellow:** *Modified* - The photo contains unsaved edits.
*   **Green:** *Saved* - Metadata has been successfully saved to disk
*   **Red:** *Error* - Validation error. The photo does not meet the minimum/maximum limits for characters or words (e.g., the title is too long).

### Information Badges
Micro-badges may appear below the photo thumbnail, indicating file properties:
*   **GPS:** The file contains GPS coordinates.
*   **XMP:** An XMP sidecar file with metadata exists for this file.
*   **ORIG:** A backup of the original file exists (from a previous save).
*   **CSV:** Data for this file is recorded in a CSV backup.
*   **RAW** / **VIDEO:** Indicates special file formats.
*   **GETTY:** Keywords have been optimized for Getty Images ESP.
*   **CAT:** Master categories have been assigned to the photo. (Hover to see the list).
*   ⚠️ **N/A:** Corrupted or unreadable file.

### Grid Editing Features
*   **Keywords (Bubbles):** Can be added using the `+` button. They support **Drag & Drop** (moving and reordering), even for multi-selection (Ctrl+Click, Ctrl+A).
    *   *Blue bubble:* Word generated by AI.
    *   *Green bubble:* Word manually added by the user.
    *   *Gray/White bubble:* Original word loaded from the file.
*   **Text Fields (Title/Description):** Automatically monitor character limits. Typos are underlined (red wavy line).
*   **Smart Sync:** Typing a word into the Title/Description when multiple photos are selected will intelligently append the text to all selected cards in real-time.
*   **Quick Clear:** The cross (×) in the field header clears the content of that specific field for the current (or all selected) photos.
*   **Copy & Paste Tools (Clipboard Icon):** Located in the field header for quickly copying the Title, Description, Tags, and Categories. You can dynamically paste these copied elements into **multiple selected files at once** (batch paste) and choose exactly which fields you want to inject (e.g., copy the entire metadata layout but apply only the Title and Description to the target files).

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/grid--function-overview.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/grid--function-overview.png" alt="ArtushVision AI - Main Grid Overview" width="100%" class="screenshot-img">
</a>

### Rating & Flags
Available on a dedicated panel (or via keyboard shortcuts):
*   **Stars (1-5):** Written to XMP/IPTC (compatible with Lightroom/Zoner).
*   **Flag (Pick/Reject):** Used for quick culling (Green = Picked, Red = Rejected).
*   **Color Labels:** Assignment of basic color labels.

### Operations and Context Menu (Right-Click)
Right-clicking on a card in the grid opens a context menu:
*   **Copy / Paste Metadata (Ctrl+C / Ctrl+V):** Transfers all metadata, including tags, from one photo to another or to a bulk selection.
*   **Run AI for Selected / Save Selected (Ctrl+S):** Targeted execution of actions for the local selection.
*   **Clear Metadata:** Option to delete all metadata or specific fields (Title only, Tags only).
*   **Lowercase:** Converts the text in the fields to lowercase letters.
*   **Rename File (F2):** Supports advanced batch renaming with variables (e.g., `{N}_{C}`).
*   **Copy / Move / Delete:** System file operations (including moving associated .xmp sidecar files).
*   **Show EXIF / Map:** Displays detailed technical data or the GPS location on a map.
*   **Getty Optimizer / Export CSV:** Advanced export features.

---

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[⭐ User Reviews & Testimonials](/docs/artushvision-reviews.html)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*