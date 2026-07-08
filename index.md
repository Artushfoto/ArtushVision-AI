---
title: "ArtushVision AI | Professional Photo Metadata & Auto Keywording"
description: "The ultimate AI photo tagging and metadata workstation for stock, travel, and home photography. Optimize for Getty Images with Local & Cloud Vision AI."
---

<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }

/* Flexbox kontejner pro rozdělení vršku (Hero sekce) na poloviny */
.hero-split {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 30px;
  margin: 10px 0 40px 0;
}
.hero-text {
  flex: 1.1;
}
.hero-image {
  flex: 0.9;
}
@media (max-width: 900px) {
  .hero-split {
    flex-direction: column;
  }
}

/* Zelený Privacy Callout Box s plnou podporou pro Světlý i Tmavý režim - CELÁ ŠÍŘKA */
.privacy-callout {
  background-color: rgba(46, 164, 78, 0.08);
  border: 1px solid rgba(26, 127, 55, 0.3);
  border-radius: 6px;
  padding: 18px;
  margin: 25px 0;
  width: 100%;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
}
.privacy-callout h2 {
  color: #1a7f37;
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 15px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.privacy-callout p {
  margin: 0;
  font-size: 13.5px;
  color: #24292f;
  line-height: 1.5;
}

/* Profesionální styl pro klikací screenshoty */
.screenshot-link {
  display: block;
  width: 100%;
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

/* Tlačítka (Call to Action) - UŽŠÍ PRO LEPŠÍ ZOBRAZENÍ VEDLE SEBE */
.btn {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 230px;
  max-width: 100%;
  padding: 10px 15px;
  font-size: 15px;
  font-weight: 600;
  text-align: center;
  text-decoration: none;
  border-radius: 6px;
  transition: background-color 0.2s, color 0.2s, box-shadow 0.2s;
  cursor: pointer;
  box-sizing: border-box;
}
.btn-primary {
  background-color: #0969da;
  color: #ffffff !important;
  border: 1px solid #0969da;
}
.btn-primary:hover {
  background-color: #0550ae;
  box-shadow: 0 3px 8px rgba(9, 105, 218, 0.2);
}
.btn-success {
  background-color: #2da44e;
  color: #ffffff !important;
  border: 1px solid #2da44e;
}
.btn-success:hover {
  background-color: #2c974b;
  box-shadow: 0 3px 8px rgba(45, 164, 78, 0.2);
}

/* GitHub Téma vyhledávacího komponentu - ZAROVNÁNO DOLEVA */
#flex-search-container {
  max-width: 500px;
  margin: 15px 0 25px 0;
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
  .privacy-callout {
    background-color: rgba(35, 134, 54, 0.15);
    border: 1px solid rgba(46, 164, 78, 0.4);
  }
  .privacy-callout h2 {
    color: #2ea44e;
  }
  .privacy-callout p {
    color: #c9d1d9;
  }
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

<h1 style="text-align: left; margin-top: 0; padding-top: 0; font-size: 2.2em;">ArtushVision AI | Professional Metadata Automation</h1>

<div style="width: 100%; max-width: 1200px; margin: 0 auto 20px auto; border: 1px solid #333; border-radius: 6px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); overflow: hidden; background-color: #253544; line-height: 0;">
  <object type="image/svg+xml" data="artushvision.svg" title="ArtushVision AI Software Features - Smart Microstock Tagging" aria-label="ArtushVision AI Software Features - Smart Microstock Tagging" style="width: 100%; height: auto; aspect-ratio: 841.89 / 210.47; display: block; pointer-events: auto !important; outline: none; border: none; margin: 0; padding: 0;">
    <img src="artushvision.svg" alt="ArtushVision AI Software Features - Smart Microstock Tagging" />
  </object>
</div>

---

<div class="hero-split">
  <div class="hero-text">
    <p style="font-size: 1.1em; line-height: 1.5; margin-top: 0;"><strong>The Ultimate AI-Powered Workstation for Metadata, Asset Management, and Global &amp; FTP Distribution.</strong></p>
    
    <p style="font-size: 0.95em; margin: 10px 0;">Designed for smart photographers who are ready to abandon expensive cloud subscriptions and take back control. <strong><a href="/docs/artushvision-reviews.html">Read our user reviews and success stories &rarr;</a></strong></p>
    
    <blockquote style="margin: 20px 0 20px 0; font-size: 0.95em; color: #57606a; padding-left: 15px; border-left: 4px solid #0969da; font-style: italic;">
      "ArtushVision AI has rapidly evolved into the <strong>Swiss Army Knife of metadata management</strong>... From handling keywording of raw files, resolving the annoying Lightroom habit of sorting keywords alphabetically, to providing a smooth solution for the Getty/iStock controlled vocabulary... <strong>this is very hard to beat.</strong>"
      <br>
      <span style="display: block; margin-top: 8px; font-style: normal; font-size: 0.85em; font-weight: 600; color: #24292f;">
        &mdash; Steven Heap, BackyardSilver (<a href="https://backyardsilver.com/artushvision-ai-review-stock-photo-workflow/" title="Read full user reviews">Read Full Review &rarr;</a>)
      </span>
    </blockquote>
    
    <div style="display: flex; gap: 15px; flex-wrap: wrap;">
      <a href="/docs/download-purchase.html" class="btn btn-primary">Download Free Trial</a>
      <a href="/docs/download-purchase.html#buy-lifetime-license" class="btn btn-success">Buy License - $39.99</a>
    </div>
  </div>
  
  <div class="hero-image">
    <a href="artushvision.webp" target="_blank" rel="noopener noreferrer" class="screenshot-link" style="margin: 0;">
      <img src="artushvision.webp" alt="Detail of ArtushVision AI split-screen workflow" width="2005" height="1333" fetchpriority="high" class="screenshot-img" />
    </a>
  </div>
</div>

---

<div class="privacy-callout">
  <h2>🔒 100% Offline Privacy for Travel, Home &amp; Personal Archives</h2>
  <p>
    Protect your family memories, private travel logs, and sensitive client shoots. By running advanced Vision models entirely <strong>locally on your own hardware</strong>, your images are analyzed right on your graphics card. <strong>No photos ever leave your computer</strong>, zero data is uploaded to corporate clouds, and absolute data logging privacy is fully guaranteed.
  </p>
</div>

---

**Stop paying rent** for your software or credits. For just $39.99, the price of a **casual dinner for two**, you get a powerful tool that is yours forever. **No expensive monthly subscriptions**, no strings attached. Run it **completely offline for maximum privacy**, or connect to **cloud AI** whenever you need it with **total control** over your usage and costs. **It’s a one-time investment that pays for itself in just two hours of saved work.**

---

## The 3-Step Production Workflow

ArtushVision AI eliminates the friction between editing software, AI tagging, and final asset organization:

1. **Load & Cull:** Open thousands of RAW or JPG files across multiple subfolders instantly using the **Flat View**, filter out the noise, and organize your batch using native Lightroom-compatible star ratings and color labels.
2. **Generate & Resolve:** Trigger the **Cloud or 100% Private Local AI** to build high-converting titles and tags. Run the **built-in AI/Offline Getty Resolver** to automatically match official commercial taxonomies and clear homonym ambiguities in seconds.
3. **Automated FTP Upload:** Select your pre-saved Agency Profile and hit Upload. The software manages multi-threaded transfers, dynamically generates agency-specific CSV files on-the-fly, and automatically stamps your grid with visual success badges.

---

## Key Features & Functionality

* **[Versatile AI Engine Modes & Customization](/docs/ai-metadata-generation-cloud-local-ollama.html)**
    * **Cloud AI:** High-speed cloud processing via OpenRouter. You maintain full control over your API usage through a **Built-in OpenRouter Dashboard**, paying only raw API prices with total transparency.
    * **Local AI (100% Free & Private):** Run standard visual analysis on your local hardware via Ollama. Perfect for sensitive shoots with zero API costs.
    * **Hybrid AI (Local Vision + Cloud Text):** Your local GPU performs the heavy visual analysis, and a cloud model structures the text. Peak SEO quality at wholesale prices.
    * **2-Pass Local AI:** Deep offline synthesis. A local Vision model reads the pixels, then a second specialized text model formats a perfect JSON completely offline.
    * **Customizable AI Prompts:** Tailor the program exactly to your unique needs. Modify system prompts to guide the AI's descriptive style and adapt to your photography niche.

* **[Getty Images Optimizer (Master ESP Tool)](/docs/getty-images-esp-metadata-optimizer.html)**
    * **Near-Perfect Acceptance:** Map your tags against a built-in Master Dictionary of 9,867+ approved terms using a dedicated Vision Model followed by a Text Model pass.
    * **Interactive Getty Resolver:** Available for both Single and Batch modes with visual context highlighting and term splitting.
    * **Semantic AI Disambiguation:** The AI analyzes image context to solve homonyms (e.g., automatically distinguishing a "crane" bird from a "crane" construction machine).
    * **Non-Destructive Workflow:** Original metadata remains untouched; optimized terms are safely stored in separate XMP metadata.

* **[Manual Workflow & Ergonomics (Hands-On Control)](/docs/smart-manual-keywording-batch-editing.html)**
    * **Intuitive Drag & Drop Keywords:** Seamlessly drag and drop keyword bubbles to reorder them (vital for Adobe Stock top 10 priority weighting) or drag selected keywords directly between photos.
    * **Advanced Batch Metadata Application:** Select multiple files to bulk-add, overwrite, or clear Title, Description, and Keywords simultaneously.
    * **Smart Append Sync:** Type a keyword into a selection of hundreds of photos—the app injects it in real-time without overwriting their unique existing tags.
    * **Interactive Integrated Map:** Visually verify extracted GPS coordinates running reverse geocoding.
    * **Lightning-Fast Copy & Paste:** Use dedicated shortcuts to copy entire metadata blocks from one master image and paste them across an entire batch.
    * **Metadata Templates:** Save and load custom metadata presets for recurring shoots or specific studio setups.

* **[Global Distribution & Smart FTP Suite](/docs/global-stock-distribution-ftp.html)**
    * **Multi-Server Batch Uploads:** Configure individual thread limits per agency to prevent connection blocks (`421 Too many connections`).
    * **1-Click Automated CSV Upload:** Generates a temporary, agency-specific CSV with matching category IDs, uploads it alongside your media, and automatically purges it.
    * **Universal Category Mapping:** Pre-configured mapping for Adobe Stock, Shutterstock, and other major agencies.
    * **FTP Status Badges:** Successful uploads write micro-badges directly into XMP metadata for persistent tracking.

* **[Advanced Interface & Portfolio Organization](/docs/smart-grid-filters-search-metadata-management.html)**
    * **Blazing-Fast Image Grid:** Displays Titles, Descriptions, and Keywords directly below every card. Includes comprehensive Thumbnail Badges.
    * **Visual Status Indicators:** Color-coded states warn you in real-time about validation errors.
    * **Absolute Priority AI Hints:** Force the AI to treat your manual hints (obscure locations, Latin species) as absolute facts, completely eliminating hallucinations.
    * **Flat View:** Toggle a unified, continuous list view for all loaded subfolders simultaneously.

* **[Universal Metadata Compatibility & Linguistics](/docs/metadata-compatibility-and-file-handling.html)**
    * **100% EXIF/IPTC/XMP Compliant:** Data is written safely to sidecars or directly embedded, ensuring seamless interoperability with Adobe Lightroom, Bridge, and Capture One.
    * **Keyword Order Restoration:** Easily revert to your original keyword sequencing with a single click to protect manually sorted priority tags.
    * **Category Management:** Easily assign standard microstock categories to single images or entire batches to ensure full compliance with agency submission requirements.
    * **Auto-GPS Country Lookup:** Auto-translates GPS coordinates into readable city/country names via OpenStreetMap or ArcGIS.
    * **Dual-Language Spellcheck:** Validate against two dictionaries simultaneously without switching settings.

* **[Powerful Batch Operations & Configuration](/docs/batch-operations-metadata-library-management.html)**
    * **Smarter Batch Rename:** Rename thousands of files using dynamic variables like `{TITLE}`, `{CC}`, `{DATE}`, or `{FOLDER_NAME}`.
    * **Bulk Metadata Editing:** Smart Add/Remove/Replace with `Old -> New` syntax and `Ctrl+H` support.
    * **Ollama VRAM Context Tuning:** Optimize memory allocation based on your GPU hardware.
    * **Video Economy Mode:** Collage-based analysis to minimize API consumption and process video files efficiently.
    
---

<h2 align="center">💡 ZERO-RISK WORKFLOW: TRY BEFORE YOU BUY!</h2>

<table style="width: 100%; display: table; border-collapse: collapse;">
  <tr>
    <th style="width: 50%; text-align: center; padding: 12px;">
      <a href="/docs/download-purchase.html" class="btn btn-primary" style="margin: 0 auto;">Download Free Lite Version</a>
    </th>
    <th style="width: 50%; text-align: center; padding: 12px;">
      <a href="/docs/download-purchase.html#buy-lifetime-license" class="btn btn-success" style="margin: 0 auto;">Get Lifetime License</a>
    </th>
  </tr>
  <tr>
    <td style="text-align: center; padding: 10px;"><b>Fully Functional Version</b></td>
    <td style="text-align: center; padding: 10px;"><b>Only $39.99</b> (+ local VAT)</td>
  </tr>
  <tr>
    <td style="text-align: center; padding: 8px;">No time limits for testing</td>
    <td style="text-align: center; padding: 8px;">One-time payment &bull; No monthly fees</td>
  </tr>
</table>

<br />

<p align="center">
  <strong>Securely processed by Polar &amp; Stripe.</strong> <a href="/docs/manage-licence.html">Manage your licensed devices</a>
</p>

<hr>

**ArtushVision AI Main Grid Workspace**

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/grid-overview.webp" target="_blank" rel="noopener noreferrer" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/grid-overview.webp" alt="ArtushVision AI Workspace showing automated metadata generation" width="3066" height="1885" class="screenshot-img" loading="lazy" />
</a>

---

## Cost Comparison: Own Your Tools

<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
  <thead>
    <tr>
      <th style="border: 1px solid #d0d7de; padding: 8px; text-align: left;">Feature</th>
      <th style="border: 1px solid #d0d7de; padding: 8px; text-align: left;">Typical Online AI Tools</th>
      <th style="border: 1px solid #d0d7de; padding: 8px; text-align: left;">ArtushVision AI (Desktop App)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #d0d7de; padding: 8px;"><b>Media Privacy</b></td>
      <td style="border: 1px solid #d0d7de; padding: 8px;">Mandatory Cloud Upload</td>
      <td style="border: 1px solid #d0d7de; padding: 8px;">🔒 <b>100% Private (Local AI via Ollama)</b> or Thumbnail-only modes</td>
    </tr>
    <tr>
      <td style="border: 1px solid #d0d7de; padding: 8px;"><b>Format Support</b></td>
      <td style="border: 1px solid #d0d7de; padding: 8px;">JPG Only</td>
      <td style="border: 1px solid #d0d7de; padding: 8px;"><b>JPG, RAW, Video, TIFF, webp, HEIC</b></td>
    </tr>
    <tr>
      <td style="border: 1px solid #d0d7de; padding: 8px;"><b>Pricing Model</b></td>
      <td style="border: 1px solid #d0d7de; padding: 8px;">Recurring Subscriptions / Credits</td>
      <td style="border: 1px solid #d0d7de; padding: 8px;"><b>Perpetual License ($39.99)</b></td>
    </tr>
    <tr>
      <td style="border: 1px solid #d0d7de; padding: 8px;"><b>Cost (10,000 Photos)</b></td>
      <td style="border: 1px solid #d0d7de; padding: 8px;">High-tier monthly plans</td>
      <td style="border: 1px solid #d0d7de; padding: 8px;"><b>~$6</b> using Gemini Flash or <b>Free</b> utilizing Local AI</td>
    </tr>
  </tbody>
</table>

<hr>

> **Exceptional Value:** Describe up to **10,000 photos for only $6** with perfect, high-quality results.  
> **Full Cost Control:** Monitor your budget with built-in **spending statistics** (6-decimal precision).

<hr>

## Complete Documentation Index

<div id="flex-search-container">
  <input type="text" id="flex-search-input" placeholder="Search documentation..." />
  <ul id="flex-results-container"></ul>
</div>

### 1. Getting Started
* [System Requirements & Installation](/docs/installation.html)
* [First Launch & Activation](/docs/download-purchase.html)
* [Interface Overview](/docs/interface-overview.html)
* [Detail Window Overview](/docs/detail-window-interface-overview.html)
* [Cloud AI & OpenRouter API Setup](/docs/cloud-ai-openrouter-api-setup.html)
* [Local AI Setup & Integrated Model Manager](/docs/local-ai-model-manager-ollama.html)

### 2. Core Workflows
* [Understanding AI Processing Modes (Cloud, Local, Hybrid)](/docs/ai-metadata-generation-cloud-local-ollama.html)
* [How to Download Local AI Models via Ollama](/docs/how-to-download-local-ai-models-via-ollama.html)
* [Local AI Model Manager: Complete Offline Control](/docs/local-ai-model-manager-ollama.html)
* [Advanced AI Prompting, Profiles & Variables](/docs/advanced-ai-prompting-profiles-variables.html)
* [Create and Optimize Custom AI Prompts](/docs/create-and-optimize-custom-ai-prompts.html)
* [Manual Editing, Multi-language Spellcheck & Interactive Map](/docs/smart-manual-keywording-batch-editing.html)
* [Batch Metadata Actions, Search & Replace](/docs/batch-operations-metadata-library-management.html)
* [Microstock Category Mapping Matrix](/docs/category-matrix.html)
* [Smart Grid Filters and Search](/docs/smart-grid-filters-search-metadata-management.html)

### 3. Professional Asset Distribution
* [Getty Images ESP Metadata Optimizer & Resolver](/docs/getty-images-esp-metadata-optimizer.html)
* [Global Stock Distribution & Multi-threaded FTP Suite](/docs/global-stock-distribution-ftp.html)
* [Dynamic CSV Template Mapping](/docs/settings-configuration-customization.html#advanced-csv-template-editor)

### 4. Advanced Management
* [Workspace Theming, VRAM context tuning & Data Safety](/docs/settings-configuration-customization.html)

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

[📷 Developer's Photography Portfolio: artushfoto.eu](https://artushfoto.eu)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*

<script src="https://cdn.jsdelivr.net/gh/nextapps-de/flexsearch@0.7.31/dist/flexsearch.bundle.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function() {
  var searchInput = document.getElementById('flex-search-input');
  var resultsContainer = document.getElementById('flex-results-container');
  var indexTitle, indexContent;
  var documentsMap = {};

  if (!searchInput || !resultsContainer) return;

  indexTitle = new FlexSearch.Index({ tokenize: "forward", resolution: 9, depth: 1 });
  indexContent = new FlexSearch.Index({ tokenize: "forward", resolution: 5, depth: 1 });

  fetch('/search.json')
    .then(response => response.json())
    .then(data => {
      data.forEach((item, index) => {
        var id = index;
        documentsMap[id] = { title: item.title, url: item.url };
        indexTitle.add(id, item.title);
        indexContent.add(id, item.content || "");
      });
    })
    .catch(err => console.error("Search index compilation failed:", err));

  searchInput.addEventListener('input', function() {
    var query = this.value.trim();
    resultsContainer.innerHTML = '';
    
    if (query.length < 2) {
      resultsContainer.style.display = 'none';
      return;
    }

    var titleResults = indexTitle.search(query, { limit: 10 });
    var contentResults = indexContent.search(query, { limit: 10 });
    var scores = {};

    titleResults.forEach(id => { scores[id] = (scores[id] || 0) + 10; });
    contentResults.forEach(id => { scores[id] = (scores[id] || 0) + 1; });

    var sortedIds = Object.keys(scores).sort((a, b) => scores[b] - scores[a]);
    var finalIds = sortedIds.slice(0, 8);

    if (finalIds.length > 0) {
      finalIds.forEach(id => {
          var doc = documentsMap[id];
          if (!doc) return;
          var li = document.createElement('li');
          li.innerHTML = '<a href="' + doc.url + '">' + doc.title + '</a>';
          resultsContainer.appendChild(li);
        });
        resultsContainer.style.display = 'block';
      } else {
        resultsContainer.innerHTML = '<div class="no-results-msg">No documentation pages found</div>';
        resultsContainer.style.display = 'block';
      }
  });

  document.addEventListener('click', function(e) {
    if (e.target !== searchInput && e.target !== resultsContainer) {
      resultsContainer.style.display = 'none';
    }
  });

  searchInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      var firstLink = resultsContainer.querySelector('li a');
      if (firstLink) window.location.href = firstLink.href;
    }
  });
});
</script>

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