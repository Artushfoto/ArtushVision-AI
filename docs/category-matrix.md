---
title: "Smart Category Mapping | ArtushVision AI"
description: "Master Categories in ArtushVision AI. Experience real-time tag bubbles, drag-and-drop mechanics, and lightning-fast sorting and culling."
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

# Category Mapping Matrix

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

The **Category Mapping Matrix** is a powerful feature designed to eliminate the tedious task of manually assigning different categories for each individual stock photo agency. Since every agency (Adobe Stock, Shutterstock, Dreamstime, etc.) uses its own unique category names or ID numbers, ArtushVision AI uses a unified "Master Category" system.

You only need to assign a category once, and the application will automatically translate it into the correct format for every agency during your CSV export or FTP upload.

**Working with categories in ArtushVision AI**

<video src="video/how-to-add-categories.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Working with categories">
  Video demonstration of ArtushVision AI: Learn how to seamlessly map, batch edit, and automatically assign metadata categories for microstock agencies.
</video>
<p><a href="video/how-to-add-categories.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## How to Assign Categories & Properties

You can assign categories to your files in two main ways:

### 1. Automatic AI Categorization
When running Cloud AI or Local AI analysis, the system can automatically select the best-fitting Master categories based on the image content. **To enable this, include the `{allowed_categories}` variable in your AI profile's prompt.** The AI will then choose exclusively from the allowed list in your matrix and instantly store the results in the metadata.

### 2. Manual & Batch Assignment
If you prefer manual control, want to adjust the AI's choices, or need to set specific metadata flags (like Country, Editorial, Mature 18+, Illustration, or AI Generated), you can do so easily:

*   **Detail Window (Single File):** Assigned categories, the Country tag, and active property flags are clearly displayed next to the Description. You can review them, see them neatly formatted, and easily remove any incorrect tags using the "×" button.
*   **Grid (Batch Edit):** Select multiple photos and click the **Categories** button in the Batch Edit bar. Here you can assign up to 3 Master categories, define the Country (auto-extracted from GPS or entered manually), and toggle property flags. Your changes will be applied to all selected photos instantly.

<video src="video/category-filter.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Working with categories">
  Video demonstration of ArtushVision AI: Automatically filter categories for microstock agencies and work with categories in detail window.
</video>
<p><a href="video/category-filter.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

---

## Smart Batch Editing Controls

When editing multiple files at once, ArtushVision AI provides advanced controls and safeguards to ensure you don't accidentally overwrite diverse metadata.

### "Apply/Change Categories" Safeguard
To prevent accidentally overwriting the unique categories of your photos when bulk editing other fields (like Country or Editorial status):
*   **Automatic Detection:** If your selected photos have *different* categories, the **`Apply/Change categories`** checkbox at the top of the dialog will default to **unchecked** (`False`), and the categories list will be disabled.
*   **Preserving Existing Data:** As long as this remains unchecked, the program bypasses the 3-category limit check and leaves the original categories of all photos completely untouched.
*   **Explicit Overwriting:** If you *do* want to unify and apply the same categories to all selected photos, simply check the box, select up to 3 categories, and apply.

### Three-State (Tristate) Property Flags
Property flags (`Illustration`, `Editorial`, `18+ Mature`, `AI Generated`, `3D Render`) support three distinct states, giving you maximum control over mixed batches:

| Checkbox State | Visual Appearance | Action on Save |
| :--- | :---: | :--- |
| **Checked** | `[x]` | Force-sets the property to **True** for all selected photos. |
| **Unchecked** | `[ ]` | Force-sets the property to **False** for all selected photos. |
| **Partially Checked** | `[-]` | **Keep Existing:** Preserves the individual original values for each photo. |

*How to use it:* If your selected photos contain a mix of properties (e.g., only some are marked as `Editorial`), the checkbox will automatically initialize as **Partially Checked** `[-]`. Click it to force all to True, click again for False, or leave it as `[-]` to retain their current mixed states while you modify other properties.

---

## Visual Indicators: The `CAT` Badge

To give you a quick overview of your categorization progress, ArtushVision provides immediate visual feedback:
*   **CAT Badge:** As soon as a photo has at least one category assigned, a highly visible turquoise **`CAT` badge** appears on the image thumbnail in both the Grid and the Detail Window.
*   **Smart Tooltip:** Hovering your mouse over the `CAT` badge or specific asset flags instantly triggers a pop-up tooltip displaying the exact roster of assigned Master categories for that specific file.

---

## Category Matrix Editor

In this editor, you can define exactly how your Master categories map to specific agencies. Go to `Top Menu` → `File` → `Settings` → `Category Mapping Matrix`.

*   **Master Category:** Usually based on the highly detailed Dreamstime category system. This is the core category you (or the AI) will assign to your photos.
*   **Agency Columns:** Map the Master category to the corresponding categories for Adobe Stock, Shutterstock, Motion Elements, and others.
*   **Fully Customizable:** You can modify existing mappings, delete rows, or add entirely new columns if you start contributing to a new microstock agency.
*   **Smart Split:** For agencies like **Motion Elements**, the matrix distinguishes between `ME Photo` and `ME Video` categories, automatically selecting the correct one based on the file type you are processing.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/category-matrix.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/category-matrix.png" alt="ArtushVision AI - Category Mapping Matrix configuration interface in settings" width="100%" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

---

## Seamless CSV Export & FTP Integration

The true magic of the Category Matrix happens when you export your metadata.

In the **[CSV Template Editor](settings-configuration-customization.html#advanced-csv-template-editor)**, you can easily add dynamic columns for `Mapped Category 1`, `Mapped Category 2`, etc.

*   **Smart Auto-Mapping:** If you name your CSV template or FTP Server profile with the name of the agency (e.g., `"Shutterstock"` or `"Dreamstime"`), ArtushVision AI automatically understands the destination. It looks into your Category Matrix and populates the export with the exact category format required by that specific agency.
*   **Dreamstime ID Conversion:** For Dreamstime, you don't even need to memorize their category numbers. The app automatically converts text-based Master categories (like "Landscape" or "People") into Dreamstime's required numerical IDs during export.

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