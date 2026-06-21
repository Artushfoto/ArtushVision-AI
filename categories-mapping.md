---
title: "Global Stock Distribution and Smart FTP Uploader | ArtushVision AI"
description: "Assigning Categories & Properties."
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

# Assigning Categories & Properties in ArtushVision AI

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

ArtushVision AI provides powerful tools to assign categories and property flags to your photos. You can do this individually or in batch mode for multiple selected images.

---

## 1. Category Matrix Setup
The **Category Matrix** acts as a translation layer between master categories and agency-specific categories (e.g. Shutterstock, Adobe Stock, Pond5, Getty, etc.).

* **Accessing the Editor**: Open the Category Matrix Editor to view and customize the mapping.
* **Layout and Features**:
  - The editor shows a grid mapping master categories to agency equivalents.
  - *Alamy column is excluded* from the defaults.
  - **Window Memory**: The Category Matrix window saves and restores its size and position (default size: `1000x700`), so it opens exactly where and how you left it.
  - **Customizable Mapping**: Changes made here determine how your assigned categories map when you export metadata via CSV templates or upload to agency portfolios.

---

## 2. Single Photo Editing
When editing a single photo:
1. Select a photo in the main grid to view its details.
2. In the right panel, you can assign categories (up to 3) from your predefined Category Matrix.
3. You can toggle binary metadata property checkboxes:
   - **Illustration**
   - **Editorial**
   - **18+ Mature**
   - **AI Generated**
   - **3D Render**

---

## 3. Batch Category & Properties Editing
To edit categories or properties for a selection of multiple photos:
1. Select the photos you want to edit in the grid.
2. Open the **Batch Edit** panel and click the **Categories** button.
3. A dialog will open containing the category selection list, a search/filter field, and the property checkboxes.

### 🌟 New Feature: "Apply/Change Categories" Safeguard
To prevent accidentally overwriting the diverse categories of your photos when bulk editing other fields:
* **The Checkbox**: An **`Apply/Change categories`** checkbox is located at the top of the dialog.
* **Automatic Detection**: If your selected photos have *different* categories, this checkbox will default to **unchecked** (`False`), and the categories list will be disabled. 
* **Preserving Existing Data**: As long as this checkbox remains unchecked, the program will bypass the 3-category limit check and leave the original categories of all selected photos completely untouched.
* **Overwriting Explicitly**: If you *do* want to apply the same categories to all selected photos, simply check the `Apply/Change categories` checkbox, select up to 3 categories from the list, and apply.

---

## 4. 🌟 New Feature: Three-State (Tristate) Property Flags
When batch editing, the property flags (`Illustration`, `Editorial`, `18+ Mature`, `AI Generated`, `3D Render`) support three states to give you maximum control:

| Checkbox State | Visual Appearance | Action on Save |
| :--- | :---: | :--- |
| **Checked** | `[x]` | Force-sets the property to **True** for all selected photos. |
| **Unchecked** | `[ ]` | Force-sets the property to **False** for all selected photos. |
| **Partially Checked** | `[-]` | **Keep Existing**. Preserves the individual values of this property for each photo. |

### How to use Tristate flags:
* If your selected photos contain a mix of properties (e.g., some are marked as `Editorial` and some are not), the checkbox will automatically initialize as **Partially Checked** `[-]`.
* If you want to make all of them editorial, click it until it is **Checked** `[x]`.
* If you want to remove editorial status from all of them, click it until it is **Unchecked** `[ ]`.
* If you want to leave their editorial status as is, but bulk edit other properties (like checking `Illustration` for all of them), leave the `Editorial` checkbox **Partially Checked** `[-]`.

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