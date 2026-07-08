--- 
title: "Bi-directional Metadata Synchronization for Adobe Lightroom & More | ArtushVision AI"
description: "Ensure seamless bi-directional metadata synchronization with Adobe Lightroom, Zoner Photo Studio, and digiKam using ArtushVision AI's XMP sidecar workflow."
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

# Metadata Compatibility and File Handling in ArtushVision AI

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**ArtushVision AI utilizes the industry-standard ExifTool for reading and writing metadata. To ensure seamless bi-directional synchronization with the most popular photo editors and file managers, the application writes information in parallel across multiple metadata standards (XMP, IPTC, and EXIF).**

The application is fully compatible out-of-the-box with software such as **Adobe Lightroom, Zoner Photo Studio, digiKam, ACDSee**, and native **Windows Explorer**.

---

## Core Text Metadata Synchronization

When saving text information, the data is synchronously written into both the modern XMP and the legacy IPTC standards to ensure older systems and stock agencies read them perfectly.

* **Universal Title and Description:** Titles are written into `XMP-dc:Title`, `IPTC:ObjectName`, `XMP-photoshop:Headline`, and `XPTitle` (for Windows). Descriptions map directly to `XMP-dc:Description`, `IPTC:Caption-Abstract`, and `XPComment`.
* **Smart Keyword Management:** Tags are distributed to `XMP-dc:Subject`, `IPTC:Keywords`, and Lightroom's specific `XMP-lr:HierarchicalSubject`. The application automatically deduplicates words and strips empty tags during both reading and writing processes.

---

## Ratings, Flags, and Color Labels Synchronization

Every photo management software historically uses slightly different tags for organization. ArtushVision AI bridges these gaps and ensures your sorting logic is never lost.

* **Universal Star Ratings (1–5):** The app reads ratings in multiple formats and writes them to all supported standards simultaneously. This includes Adobe Lightroom (`XMP-xmp:Rating`), Zoner Photo Studio (`XMP-znr:Rating`), ACDSee, and Windows Explorer (`MicrosoftPhoto:Rating`, which is automatically translated from the 1-99 scale to 1-5 stars).
* **Pick and Reject Flags:** Flags are highly dependent on specific software ecosystems. ArtushVision AI fully supports the two main ones: Adobe Lightroom (`XMP-xmpDM:Pick` and `XMP-xmpDM:Good`) and digiKam (`XMP-digiKam:PickLabel`).
* **Color Labels:** Colors (Red, Yellow, Green, Blue, Purple) are saved as standard text strings (`XMP-xmp:Label`) and simultaneously converted to numerical priority (`XMP-photoshop:Urgency`) for legacy software compatibility.

---

## File Handling and XMP Sidecar Strategy

* **Non-Destructive RAW and Video Metadata:** To guarantee maximum safety of your original data, the application *never* writes directly into RAW files (CR2, NEF, ARW, DNG) or Videos (MP4, MOV). All metadata is safely stored in adjacent `.xmp` sidecar files.
* **XMP Naming Conventions:** ArtushVision AI fully supports and reads both recognized naming standards: the basic standard (`filename.xmp`) and Adobe Lightroom's extended standard (`filename.CR2.xmp`). When creating a new XMP file, existing EXIF data is automatically copied from the original RAW/Video to prevent technical data loss.
* **Direct JPG, TIFF, and webp Writing:** Standard image formats receive metadata directly into the file to prevent data fragmentation. If a legacy XMP sidecar already exists for a JPG, the app automatically merges it, renames it, and archives it to prevent future loading collisions. (You can edit these templates in the [Advanced CSV Template Editor](/docs/settings-configuration-customization.html#advanced-csv-template-editor).)

---

## ArtushVision AI Specific Metadata Fields

The application stores its internal tracking data in standard text fields so it remains readable and persistent even in other editors.

* **FTP Upload History:** The list of stock agencies where a photo was successfully uploaded is safely stored in the `IPTC:TransmissionReference` and `XMP-photoshop:TransmissionReference` fields.
* **Category Mapping:** Selected agency categories are saved into supplemental fields (`XMP-photoshop:SupplementalCategories` and `IPTC:SuppCategory`).
* **Internal Flags:** System flags (e.g., AI Generated, Editorial, Mature) are embedded into `IPTC:SpecialInstructions` and `XMP-photoshop:Instructions` using a safe bracket format.
* **Keyword Order Preservation:** The `XMP-artush:KeywordOrder` tag is a custom metadata field engineered specifically for ArtushVision to prevent Adobe Lightroom from destroying your keyword sequence by auto-sorting them alphabetically. Because keyword order is crucial for stock photography SEO, this tag automatically backs up the active sequence as a comma-separated string upon every single save in ArtushVision, ensuring any newly adjusted order is immediately updated. If your keywords get alphabetized during a Lightroom export, the **Restore original keyword order after LR export** feature reads this tag to restore the exact positions, while safely appending any newly added keywords to the end of the list.

---

## Visual Status Badges and File Management

Keep track of your technical data and backup states without ever opening a properties dialog. ArtushVision AI displays small informational micro-badges directly on your image thumbnails in both the grid and detail views.

* **File Type and Geolocation:** Instantly identify special media types with dedicated **RAW** and **VIDEO** badges, or see if a file contains embedded coordinates with the **GPS** badge.
* **Backup Trackers:** Know your data is safe at a glance. The application highlights files that have a dedicated **XMP** sidecar, an original backup file (**ORIG**), or are safely backed up in a spreadsheet (**CSV**).
* **Distribution and AI Tags:** Track your workflow visually. The **CAT** badge indicates successfully mapped categories, the **GETTY** badge highlights optimized terms, and tiny agency micro-badges (e.g., S, A, F) show your complete FTP upload history.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/badges.webp" target="_blank" class="screenshot-link" style="max-width: 600px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/badges.webp" alt="ArtushVision AI visual status badges on image thumbnails" loading="lazy" style="width: 600px;" class="screenshot-img">
</a>

---

## Seamless Integration with Adobe Lightroom and Other Managers

Keep your master catalog perfectly in sync. ArtushVision AI writes all tags and edits into industry-standard XMP sidecars, ensuring your non-destructive workflow remains intact.

* **Non-Destructive XMP Workflow:** All metadata edits are safely stored in external sidecar files, keeping your original RAW assets completely untouched.
* **Two-Way Synchronization:** Made changes directly in Lightroom or other software? No problem. To pull external edits (like new ratings, color labels, or descriptions) back into ArtushVision AI, simply select the affected photos in the grid, right-click, and choose **Restore original from disk**. Alternatively, you can click **Refresh from Disk** in the Detail window or just reload the entire folder.
* **Restore Original Keyword Order:** Adobe Lightroom often reshuffles or alphabetizes your keyword lists when metadata is synced or exported. ArtushVision AI automatically saves your custom optimized tag order inside `XMP-artush:KeywordOrder`. Simply right-click the selected photos in the main grid and choose **Restore keywords and order after LR Export** to automatically sort them back. Any new keywords you manually added in Lightroom in the meantime are safely preserved and appended to the very end of the list.
* **Instant Catalog Synchronization:** To apply your AI-generated keywords and edits back to your master catalog, simply select the modified photos in your software's grid and reload the metadata:
  * **Adobe Lightroom:** Right-click the selected assets and choose **Metadata > Read Metadata from Files**.
  * **Capture One:** Right-click the selected assets and choose **Load Metadata**.
  * **digiKam:** Select the assets, go to the top menu **Item**, and choose **Read Metadata from File**.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/lightroom-metadata.webp" target="_blank" class="screenshot-link" style="max-width: 100%; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/lightroom-metadata.webp" alt="ArtushVision AI - Syncing and reading metadata from Adobe Lightroom" loading="lazy" style="width: 100%;" class="screenshot-img">
</a>

*ArtushVision AI - Universal XMP Support: Fits Seamlessly Into Your Existing Ecosystem.*

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