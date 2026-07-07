---
title: "Smart Grid Filters & Search: Portfolio Metadata Management"
description: "Master large-scale photo portfolios with advanced grid filters, real-time search, metadata validation logic, and 3-state FTP distribution filters."
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

# Smart Grid Filters and Search: Total Control Over Huge Portfolios

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Managing a batch of thousands of photos and videos requires precision. ArtushVision AI features a multi-layered filtering system that combines real-time text search, advanced metadata logic, and visual micro-badges to provide absolute clarity over your entire portfolio.**

Finding specific files—such as those missing a description or those not yet uploaded to a particular agency—is no longer a manual task. The filtering suite ensures you always know exactly which assets require your attention.

**Real-time Smart Search inside Image Grid**

<video src="video/search.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Real-time Smart Search">
  ArtushVision AI - Smart Search Function.
</video>
<p><a href="video/search.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## Precision Search and Limit Validation

The top-bar search engine works in real-time, highlighting your target words directly inside the grid text fields in bright yellow for instant verification.

* **Scoped Search:** Search across all fields or restrict your query strictly to Titles, Descriptions, or Keywords to prevent false positives.
* **Validation Filters:** Instantly isolate files marked as "Exceeded Limits" (e.g., descriptions too long for specific stock agencies) or those containing "Misspelled Words". The application automatically colors problematic fields red.
* **File Type and Folder Isolation:** Quickly filter by format (RAW, HEIC, TIFF, webp, Video) or focus on a single subfolder without losing your overall progress in the project.

<!-- [IMAGE: A close-up screenshot of the Advanced Metadata Filter dialog, showing the Has / Hasn't logic dropdowns.] -->

---

## Advanced Metadata and Category Logic

Beyond basic text search, ArtushVision AI allows for complex queries based on the presence or absence of specific metadata, which is crucial for preparing stock batches.

* **Blank Field Detection:** Instantly identify all assets that do not have a Title, Description, or Keywords assigned.
* **[Category Matrix Filter](category-matrix.html):** Filter the grid to show only photos belonging to a specific Master Category (e.g., "Business") while excluding others (e.g., "Editorial").
* **Getty Status Integration:** Isolate photos that are fully Getty Optimized versus those requiring action in the [Interactive Resolver](getty-images-esp-metadata-optimizer.html).

---

## Three-State FTP Distribution Filter

Integrated directly with the [Smart FTP](global-stock-distribution-ftp.html) Uploader, this dedicated filter allows you to view your portfolio based on its commercial distribution history.

* **Not Uploaded:** Show only files that have not yet been sent to a specific target agency (e.g., Adobe Stock).
* **Uploaded:** Show assets that are already safely confirmed on the server.
* **Ignore State:** Hide files that you deliberately choose not to send to a specific agency (e.g., excluding editorial content from agencies that do not accept it).

<!-- [IMAGE: A screenshot of the Advanced FTP Filter dialog showing the selection for agencies like Shutterstock and Freepik.] -->

---

## Visual Grid Badges

ArtushVision AI provides instant feedback through colorful micro-badges stamped directly onto the photo cards in the main grid.

| Badge Type | Description |
| :--- | :--- |
| **Format & Data** | Indicates if a file is VIDEO, RAW, contains GPS coordinates, or has XMP/CSV backups. |
| **Category (CAT)** | Hover over the teal CAT badge to see a tooltip listing all assigned Master Categories. |
| **Agency Letters** | Circular letters (S, A, D, etc.) show exactly which FTP servers the file has reached. |
| **Status Markers** | Color-coded dots indicating if a file is Unchanged, Modified, Saved, or contains an Error. |

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/badges.webp" target="_blank" class="screenshot-link" style="max-width: 800px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/badges.webp" alt="ArtushVision AI Visual Grid Badges for Metadata Tracking" style="width: 800px;" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

---

## Master Your Workflow in 3 Steps:

1. **Load and Flatten:** Load thousands of files across multiple subfolders and switch to Flat View to see them in a single unified grid.
2. **Apply Advanced Logic:** Use the "Advanced Metadata Filter" to isolate files without keywords and the "Type" filter to restrict results to Video assets.
3. **Batch Edit:** Select the isolated files (Ctrl+A), use the AI Engine to generate the missing data using batch actions, and clear the filters (Esc) to return to your organized project.

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

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-9CH7W6CRCH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-9CH7W6CRCH');
</script>