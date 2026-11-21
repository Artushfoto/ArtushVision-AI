---
title: "Alamy Supertagger & CSV Autofill - Chrome Extension"
description: "Automate Alamy Image Manager metadata entry. Mark the first 10 Supertags automatically and autofill titles, descriptions, keywords, and categories from ArtushVision or custom CSV templates."
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

# Alamy Supertagger & CSV Autofill: Automate Your Stock Workflow

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Save hours of repetitive manual clicking in Alamy Image Manager. Automatically mark your top 10 Supertags and populate titles, descriptions, keywords, and categories from ArtushVision AI or any custom CSV template.**

Submitting content to **Alamy** often requires tedious manual steps inside the **Alamy Image Manager**—especially selecting the **first 10 Supertags** for every single image and manually mapping categories or metadata fields. 

The [**Alamy Supertagger & CSV Autofill**](https://chromewebstore.google.com/detail/alamy-supertagger-csv-aut/jfdfhcpmfeamolnbibjdoehepbopihlm) browser extension bridges this gap. While tailored for seamless integration with **ArtushVision AI** exports, it is built as a **100% universal tool** that works with any CSV spreadsheet formatted to a simple standard template.

---

## 1. Key Features & Universal CSV Support

Whether you generate metadata in ArtushVision AI, Excel, Google Sheets, or any other AI keywording software, this extension automates the final mile of your Alamy submission.

- **1-Click Top 10 Supertags:** Automatically selects and marks the first 10 keywords in your list as **Supertags**—eliminating hundreds of repetitive clicks per batch and boosting your commercial search visibility on Alamy.
- **Universal CSV Compatibility:** Works out-of-the-box with **ArtushVision AI CSV exports**, as well as **any custom CSV file** structured according to the standard template.
- **Complete Metadata & Category Autofill:** Reads your CSV file and automatically populates Titles, Descriptions, Keywords, and Alamy Categories directly into the web interface.
- **100% Local & Privacy-First:** All CSV parsing and DOM automation happen locally inside your browser. Your data and files are never uploaded to any external servers.
![alt text](images/alamy_supertagger.png)

---

## 2. Installation & Getting Started

Install the extension directly from the [**Chrome Web Store** ](https://chromewebstore.google.com/detail/alamy-supertagger-csv-aut/jfdfhcpmfeamolnbibjdoehepbopihlm)(compatible with Google Chrome, Microsoft Edge, Brave, and other Chromium-based browsers).

1. Visit the [**Chrome Web Store** ](https://chromewebstore.google.com/detail/alamy-supertagger-csv-aut/jfdfhcpmfeamolnbibjdoehepbopihlm)and click **Add to Chrome** on the *Alamy Supertagger & CSV Autofill* page.
2. Pin the extension icon to your browser toolbar for quick access.
3. Log in to your **Alamy Contributor Portal** and open **Alamy Image Manager**.

---

## 3. Using Universal CSV Templates

You do not need to be an ArtushVision AI user to benefit from automated CSV filling. Any spreadsheet exported as a UTF-8 CSV matching the template columns can be loaded into the extension.

### Standard CSV Structure
Ensure your CSV file contains the following header columns (case-insensitive matching supported):

| Column Name | Description | Example |
| :--- | :--- | :--- |
| **`Filename`** | Exact filename of the uploaded image on Alamy (with or without extension). | `IMG_4821.jpg` |
| **`Title`** | Main commercial title / caption for the image. | `Aerial view of autumn forest in misty mountains` |
| **`Description`** | Detailed editorial or commercial description (optional). | `Morning fog rolling over colorful autumn trees at sunrise.` |
| **`Keywords`** | Comma-separated list of keywords. **The first 10 tags will be marked as Supertags.** | `autumn, forest, fog, mountains, aerial, nature, trees, mist, sunrise, landscape` |
| **`Category`** | Primary Alamy category name (optional). | `Landscapes` |

> **Pro Tip for Supertags:** Alamy prioritizes the first 10 keywords marked as **Supertags**. Always place your 10 strongest, most descriptive keywords at the very beginning of your `Keywords` column!

---

## 4. Extension Interface & Controls

When you click the **Alamy Supertagger & CSV Autofill** icon while inside Alamy Image Manager, a clean control popup gives you full control over your batch:

- **Load CSV File:** Select your exported `.csv` file from ArtushVision AI or your custom spreadsheet. The extension immediately indexes all rows by filename.
- **Auto-Mark Top 10 Supertags:** Automatically checks the Supertag boxes for the first 10 keywords on the active image(s).
- **Autofill Metadata & Categories:** Matches the currently selected image in Alamy Image Manager with its corresponding row in your CSV and fills in all text fields and category dropdowns.
- **Batch Processing / Next Image:** Move smoothly through your uploaded batch without losing your loaded CSV state.

<video src="video/alamy-supertagger-workflow.mp4" width="100%" autoplay loop muted playsinline title="Alamy Supertagger & CSV Autofill - Full Workflow Demo">
  Alamy Supertagger & CSV Autofill - Full Workflow Demo.
</video>
<p><a href="video/alamy-supertagger-workflow.mp4" target="_blank" style="font-size: 0.9em;">Watch tutorial: Alamy Supertagger & CSV Autofill Workflow (full size)</a></p>

---

## 5. Recommended Alamy Submission Workflow

Prepare Metadata (ArtushVision AI or Custom CSV) ➔ Upload Images to Alamy Image Manager ➔ Load CSV in Extension ➔ Autofill & Supertag ➔ Review & Submit.

1. **Generate or Prepare Metadata:** Export your metadata CSV directly from **ArtushVision AI**, or prepare your own spreadsheet using the standard CSV template. Make sure your top 10 keywords are listed first.
2. **Upload Media to Alamy:** Upload your JPEGs or vectors to **Alamy Image Manager** as usual.
3. **Open the Extension:** Once your images appear in the manager grid or editor view, click the [**Alamy Supertagger**](https://chromewebstore.google.com/detail/alamy-supertagger-csv-aut/jfdfhcpmfeamolnbibjdoehepbopihlm) icon in your browser toolbar.
4. **Load Your CSV:** Import your `.csv` file into the extension.
5. [**Run Autofill & Supertagger:**](https://chromewebstore.google.com/detail/alamy-supertagger-csv-aut/jfdfhcpmfeamolnbibjdoehepbopihlm) Trigger the autofill and watch the extension populate your titles, descriptions, categories, keywords, and top 10 Supertags in seconds.
6. **Final Check & Submit:** Quickly verify the populated fields in Alamy Image Manager and submit your batch for QC!

---

### [Get Started Now]
- [Install Alamy Supertagger & CSV Autofill (Chrome Web Store)](#)
- [Download ArtushVision AI Free Lite Version](/docs/download-purchase.html)
- [Purchase ArtushVision AI Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

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

<!-- Odložené načtení Google Analytics pro maximální PageSpeed skóre -->
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