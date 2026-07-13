---
title: "Smart Category Mapping, Metadata Editor"
description: "Master microstock categories with ArtushVision AI. Automate metadata tagging, batch edit properties, and map stock photography categories across agencies seamlessly."
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

# Microstock Category Mapping Matrix

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

The **Category Mapping Matrix** is a powerful microstock metadata feature designed to eliminate the tedious task of manually assigning different categories for each individual stock photo agency. Since every stock photography platform (Adobe Stock, Shutterstock, Dreamstime, etc.) uses its own unique category names or ID numbers, ArtushVision AI uses a unified "Master Category" system.

You only need to assign a category once, and the application will automatically translate it into the correct format for every agency during your CSV export or FTP upload workflow.

**Working with Microstock Categories in ArtushVision AI**

<video src="video/how-to-add-categories.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Automate Microstock Category Mapping & Metadata">
  Video demonstration of ArtushVision AI: Learn how to seamlessly map, batch edit, and automatically assign metadata categories for microstock agencies.
</video>
<p><a href="video/how-to-add-categories.mp4" target="_blank" style="font-size: 0.9em;">Watch tutorial: How to seamlessly map, batch edit, and automatically assign metadata categories (full size)</a></p>

---

## How to Assign Categories & Metadata Properties

You can assign categories to your stock image files in two main ways:

### 1. Automatic AI Categorization for Stock Photos
When running Cloud AI or Local AI analysis, the system can automatically select the best-fitting Master categories based on the image content. **To enable this, include the `{allowed_categories}` variable in your AI profile's prompt.** The AI will then choose exclusively from the allowed list in your matrix and instantly store the results directly in the file's metadata.

### 2. Manual & Batch Assignment of Metadata
If you prefer manual control, want to adjust the AI's choices, or need to set specific microstock metadata flags (like Country, Editorial, Mature 18+, Illustration, or AI Generated), you can do so easily:

*   **Detail Window (Single File):** Assigned categories, the Country tag, and active property flags are clearly displayed next to the Description. You can review them, see them neatly formatted, and easily remove any incorrect tags using the "×" button.
*   **Grid (Batch Edit):** Select multiple photos and click the **Categories** button in the Batch Edit bar. Here you can assign up to 3 Master categories, define the Country (auto-extracted from GPS or entered manually), and toggle property flags. Your changes will be applied to all selected photos instantly, streamlining your stock photography workflow.

<video src="video/category-filter.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Batch Filter and Edit Metadata Categories">
  Video demonstration of ArtushVision AI: Automatically filter categories for microstock agencies and work with categories in the detail metadata window.
</video>
<p><a href="video/category-filter.mp4" target="_blank" style="font-size: 0.9em;">Watch tutorial: How to filter categories and work with them in the metadata window (full size)</a></p>

---

## Smart Batch Editing Controls for Image Metadata

When editing multiple files at once, ArtushVision AI provides advanced batch editing controls and safeguards to ensure you don't accidentally overwrite diverse metadata across your stock portfolio.

### "Apply/Change Categories" Safeguard
To prevent accidentally overwriting the unique categories of your photos when bulk editing other fields (like Country or Editorial status):
*   **Automatic Detection:** If your selected photos have *different* categories, the **`Apply/Change categories`** checkbox at the top of the dialog will default to **unchecked** (`False`), and the categories list will be disabled.
*   **Preserving Existing Data:** As long as this remains unchecked, the program bypasses the 3-category limit check and leaves the original metadata categories of all photos completely untouched.
*   **Explicit Overwriting:** If you *do* want to unify and apply the same categories to all selected photos, simply check the box, select up to 3 categories, and apply.

### Three-State (Tristate) Property Flags
Property flags (`Illustration`, `Editorial`, `18+ Mature`, `AI Generated`, `3D Render`) support three distinct states, giving you maximum control over mixed microstock batches:

| Checkbox State | Visual Appearance | Action on Save |
| :--- | :---: | :--- |
| **Checked** | `[x]` | Force-sets the property to **True** for all selected photos. |
| **Unchecked** | `[ ]` | Force-sets the property to **False** for all selected photos. |
| **Partially Checked** | `[-]` | **Keep Existing:** Preserves the individual original metadata values for each photo. |

*How to use it:* If your selected photos contain a mix of properties (e.g., only some are marked as `Editorial`), the checkbox will automatically initialize as **Partially Checked** `[-]`. Click it to force all to True, click again for False, or leave it as `[-]` to retain their current mixed states while you modify other properties.

---

## Visual Indicators: The Metadata `CAT` Badge

To give you a quick overview of your stock categorization progress, ArtushVision provides immediate visual feedback:
*   **CAT Badge:** As soon as a photo has at least one category assigned, a highly visible turquoise **`CAT` badge** appears on the image thumbnail in both the Grid and the Detail Window.
*   **Smart Tooltip:** Hovering your mouse over the `CAT` badge or specific asset flags instantly triggers a pop-up tooltip displaying the exact roster of assigned Master categories for that specific file.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/categories-badge.webp" target="_blank" class="screenshot-link" style="max-width: 500px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/categories-badge.webp" alt="ArtushVision AI metadata category badge on image thumbnail" style="width: 500px;" class="screenshot-img">
</a>

---

## Category Matrix Editor for Microstock Agencies

In this editor, you can define exactly how your Master categories map to specific stock photo agencies. Go to `Top Menu` → `File` → `Settings` → `Category Mapping Matrix`.

*   **Master Category:** Usually based on the highly detailed Dreamstime category system. This is the core category you (or the AI) will assign to your photos.
*   **Agency Columns:** Map the Master category to the corresponding categories for Adobe Stock, Shutterstock, Motion Elements, and others.
*   **Fully Customizable:** You can modify existing mappings, delete rows, or add entirely new columns if you start contributing to a new microstock agency.
*   **Smart Split:** For agencies like **Motion Elements**, the matrix distinguishes between `ME Photo` and `ME Video` categories, automatically selecting the correct one based on the file type you are processing.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/category-matrix.webp" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/category-matrix.webp" alt="ArtushVision AI Category Mapping Matrix editor configuring stock agency metadata" width="100%" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

---

## Seamless CSV Export & FTP Integration for Stock Agencies

The true magic of the Category Matrix happens when you export your metadata for stock agencies.

In the **[CSV Template Editor](settings-configuration-customization.html#advanced-csv-template-editor)**, you can easily add dynamic columns for `Mapped Category 1`, `Mapped Category 2`, etc.

*   **Smart Auto-Mapping:** If you name your CSV template or FTP Server profile with the name of the agency (e.g., `"Shutterstock"` or `"Dreamstime"`), ArtushVision AI automatically understands the destination. It looks into your Category Matrix and populates the export with the exact category format required by that specific microstock agency.
*   **Dreamstime ID Conversion:** For Dreamstime, you don't even need to memorize their category numbers. The app automatically converts text-based Master categories (like "Landscape" or "People") into Dreamstime's required numerical IDs during export.

---

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

## Need Help?

Search the documentation pages directly or jump back to the main [Complete Documentation Index](/index.html#complete-documentation-index).

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[⭐ User Reviews & Testimonials](/docs/artushvision-reviews.html)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*

<script>
  document.addEventListener("DOMContentLoaded", function() {
    let analyticsLoaded = false;

    function loadAnalytics() {
      if (analyticsLoaded) return;
      analyticsLoaded = true;

      // 1. Dynamické vložení externího skriptu gtag.js s NOVÝM ID
      var gtagScript = document.createElement('script');
      gtagScript.async = true;
      gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-KCZWMGZFJ5';
      document.head.appendChild(gtagScript);

      // 2. Inicializace nastavení Google Analytics s NOVÝM ID
      window.dataLayer = window.dataLayer || [];
      window.gtag = function(){ dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', 'G-KCZWMGZFJ5');

      // 3. Odstranění posluchačů událostí po úspěšném načtení
      document.removeEventListener('scroll', loadAnalytics);
      document.removeEventListener('mousemove', loadAnalytics);
      document.removeEventListener('touchstart', loadAnalytics);
    }

    // Spuštění při první skutečné interakci uživatele
    document.addEventListener('scroll', loadAnalytics, { passive: true });
    document.addEventListener('mousemove', loadAnalytics, { passive: true });
    document.addEventListener('touchstart', loadAnalytics, { passive: true });

    // Pojistka: Pokud uživatel do 5 sekund nic neudělá, načíst Analytics automaticky
    setTimeout(loadAnalytics, 5000);
  });
</script>