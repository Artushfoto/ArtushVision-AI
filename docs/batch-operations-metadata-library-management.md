<!-- --- artushvision-batch-doc --- -->
---
title: "Batch Operations and Library Management | ArtushVision AI Documentation"
description: "Master bulk metadata editing and file management. Learn how to use global search and replace, dynamic batch renaming, and synchronized file operations."
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

# Batch Operations (Batch Panel) in ArtushVision AI

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Managing thousands of assets requires more than just AI - it requires powerful batch processing tools. ArtushVision AI provides a suite of operations designed to modify, rename, and organize your entire library with a few clicks.**

Efficiency in professional photography workflows is built on the ability to apply changes across large datasets simultaneously. Whether you need to fix a recurring typo or rename a day's worth of shooting, these tools ensure consistency across your project.

The Batch Panel allows for lightning-fast modification of metadata across multiple selected photos at once. For any batch action to take place, the photos must be **selected** (e.g., using `Ctrl+A`, `Shift+Click`, or `Ctrl+Click`) and must be **visible** (i.e., not hidden by any currently active filter).

---

## Synchronized File Operations
Moving or deleting professional assets is risky if sidecar files are left behind. ArtushVision AI handles file management with "linked" logic.

* **Sidecar Synchronization:** When you Move or Copy a file within the application, it automatically brings along all associated `.xmp` and `.getty` sidecar files.
* **Safe Deletion:** Deleting an asset through the application ensures that the primary file and all its metadata sidecars are removed together, preventing "ghost" metadata files from cluttering your folders.
* **Folder Structure Integrity:** Maintain your organizational hierarchy while performing mass file migrations across different drives.

---

## Status Filtering and Batch Selection
To perform operations effectively, you must first isolate the right files. The Filter Bar works in tandem with Batch Operations.

* **Workflow Filtering:** Quickly select only files marked as Modified or Error to apply batch fixes.
* **Quality Control Filters:** Isolate files that have "Exceeded Limits" (e.g., too many keywords for Getty Images) and use batch actions to trim them down to compliance.
* **Selection Tools:** Use standard keyboard shortcuts (Shift+Click for ranges, Ctrl+A for all) to define the scope of your batch operation instantly.

**Using Smart Filters in ArtushVision AI**

<video src="video/smart-filters.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Smart Filters and Workflow Filtering">
  ArtushVision AI - Smart Filter Function.
</video>
<p><a href="video/smart-filters.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## Target Selection (Where the change should happen)
Before running an operation, use the **"Batch Edit: / Target:"** dropdown to choose which field the action applies to:
*   **Everywhere** – The action is applied to Title, Description, and Keywords simultaneously.
*   **Title** – Changes only the Title.
*   **Description** – Changes only the Description.
*   **Keywords** – Changes only the Keywords. *For keywords, smart formatting, deduplication, and whole-word matching (tags) are applied automatically.*

---

## Available Actions

### Add Text (+ Add)
Used to bulk insert new text into the selected photos.
*   **How it works:** You type the text into the input field and click the `+ Add` button.
*   The app will ask you where you want to insert the text: **At the beginning** or **At the end**.
*   *For Keywords:* The app automatically checks if the word is already present in the photo. It prevents duplicates and smartly inserts the text separated by a comma.

### Remove Text (- Remove)
Removes the specified text from all selected photos.
*   *For text fields (Title/Description):* Removes the specific text string (e.g., "and son").
*   *For Keywords:* If you enter words to remove (multiple words separated by commas are supported), the app reliably deletes the entire matching tags regardless of case sensitivity, and cleans up the formatting (commas) afterwards.

### ⇄ Replace (Ctrl+H)
Opens a dialog for advanced bulk text replacement.
*   In the **Find:** field, type what you want to change.
*   In the **Replace with:** field, type the new value.
*   You can check **Case Sensitive**.
*   **Replace All:** Applies the change immediately across all selected photos.
*   **Replace Next / Find Next:** Allows you to go through the selected photos sequentially and replace words one by one with immediate visual feedback.
*   *Alternative Quick Syntax:* You can also type `old word -> new word` directly into the main input field in the panel and click `⇄ Replace`.

**Using Batch Operations in ArtushVision AI**

<video src="video/batch-operations.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Batch Operations and Bulk Text Replacement">
  ArtushVision AI - Batch Operation overview.
</video>
<p><a href="video/batch-operations.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

### ⌫ Clear Field
Completely and permanently deletes the content **only for the currently selected target** (e.g., clears only Descriptions for all selected photos, leaving Title and Keywords untouched).

### × Clear All
An extremely powerful function that absolutely wipes all descriptive metadata – **Title, Description, and Keywords** simultaneously for the selected photos. Furthermore, it completely clears the internal AI cache for that photo. Technical EXIF data and capture dates naturally remain intact.

### Categories
Used to batch assign microstock categories to selected photos.
*   You can assign a maximum of **3 categories**.
*   Also allows you to batch change **Country** info or content properties (Editorial, Illustration).
*   *Tip:* If you leave `<Keep existing>` selected, that specific property (e.g., Country) will remain unchanged for the individual photos during the batch edit.

---

## Dynamic Variables
In the input field for `Add` and `Replace`, you can use smart text variables that the app replaces with real data for each photo on the fly. This is excellent for automation!

Available variables:
*   `{DATE}` – Inserts today's date (e.g., 14.02.2026).
*   `{ORIG_DATE}` – Inserts the original capture date of the photo.
*   `{FOLDER_NAME}` – Inserts the name of the folder where the photo is currently located.
*   `{ORIG_FILENAME}` – Inserts the original filename (without extension).

**Counter Variables (Numbering):**
*   `{C}` – Inserts a number starting from 1 that increases with each subsequent photo (1, 2, 3...).
*   `{CC}`, `{CCC}`, etc. – The number of `C`s determines the number of zero-padded digits (e.g., `{CCC}` generates `001`, `002`).
*   `{C-5}` – Adding `-X` sets the starting number for the counter. For example, `{CC-10}` will generate `10`, `11`, `12`.

### Example in Practice:
If you choose the Title field and enter the following text to bulk add:
`Vacation in {FOLDER_NAME} {ORIG_DATE} - Photo {CC-1}`

The result on individual photos will be e.g.:
1. *Vacation in Croatia 12.08.2025 - Photo 01*
2. *Vacation in Croatia 13.08.2025 - Photo 02*

---

## Global Search and Replace (Ctrl+H)
The Global Search and Replace tool is a powerful engine for fixing metadata errors or updating information across your entire loaded project.

* **Targeted Manipulation:** Choose exactly which fields to affect—Title, Description, Keywords, or all of them at once.
* **Case Sensitivity:** Toggle between case-sensitive or insensitive matching to ensure precise string replacement.
* **Bulk Correction:** Ideal for updating brand names, fixing recurring spelling mistakes, or changing specific terminology across thousands of assets instantly.

---

## Useful Tips
1. **Safe Undo:** Every batch action (including Clear All) creates a restore point. If you make a mistake, simply press the `↶ Undo` button (or `Ctrl+Z`), and all data will revert to its original state.
2. **Combining with Filters:** Batch operations respect filters! If you filter photos `With Rating 5 ★` at the top, then press `Ctrl+A` and `+ Add`, the text will be added ONLY to those 5-star photos. The others in the folder remain untouched.
3. **Colors (Word Sources):** If you batch add text via this panel, the system correctly recognizes it as *Manually added* and colors it accordingly (green), while the original text keeps its original color.

---

### Professional Workflow in 3 Steps:
1. **Filter Your Scope:** Use the status and search filters to isolate the assets you need to modify.
2. **Launch Action:** Press Ctrl+H for search and replace, or use the right-click context menu for Batch Rename and Smart Actions.
3. **Verify and Save:** Review the changes in the grid and click Save All to commit the new metadata and filenames to your storage.

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
<!-- --- artushvision-batch-doc --- -->