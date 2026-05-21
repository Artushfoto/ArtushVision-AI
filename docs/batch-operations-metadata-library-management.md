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

# Batch Operations: Surgical Precision for Massive Libraries

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Managing thousands of assets requires more than just AI—it requires powerful batch processing tools. ArtushVision AI provides a suite of operations designed to modify, rename, and organize your entire library with a few clicks.**

Efficiency in professional photography workflows is built on the ability to apply changes across large datasets simultaneously. Whether you need to fix a recurring typo or rename a day's worth of shooting, these tools ensure consistency across your project.

[IMAGE: A  screenshot of the Batch Operations window or the Search and Replace dialog showing a complex string manipulation.]

---

## Global Search and Replace (Ctrl+H)
The Global Search and Replace tool is a powerful engine for fixing metadata errors or updating information across your entire loaded project.

* **Targeted Manipulation:** Choose exactly which fields to affect—Title, Description, Keywords, or all of them at once.
* **Case Sensitivity:** Toggle between case-sensitive or insensitive matching to ensure precise string replacement.
* **Bulk Correction:** Ideal for updating brand names, fixing recurring spelling mistakes, or changing specific terminology across thousands of assets instantly.

---

## Smart Metadata Actions
Beyond simple text replacement, ArtushVision AI offers dedicated batch actions for structured metadata manipulation.

* **Bulk Add/Append:** Add specific keywords or phrases to the beginning or end of your existing metadata without disturbing the current content.
* **Bulk Remove:** Strip specific words or unwanted tags from hundreds of files in one operation.
* **Replace All:** Completely overwrite specific fields for a selected batch, useful when correcting whole sessions with new AI-generated or manual data.

---

## Dynamic Batch Rename
Organization starts with consistent file naming. The Batch Rename tool uses a dynamic placeholder system to create meaningful filenames based on the asset's own metadata.

* **Placeholder Logic:** Build filenames using variables such as `{TITLE}` (derived from metadata), `{DATE}` (from EXIF), and `{CC}` (automatic counter).
* **Sequential Numbering:** Ensure your files follow a perfect numerical sequence, regardless of their original filenames.
* **Live Preview:** View exactly how your files will be renamed before committing the changes to your hard drive.

[IMAGE: A close-up of the Rename dialog showing the pattern {DATE}_{TITLE}_{CC} and the resulting file preview.]

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
