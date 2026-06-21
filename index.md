---
title: "ArtushVision AI | Professional Photo Metadata & Auto Keywording"
description: "The ultimate AI photo tagging and metadata workstation for stock, travel, and home photography. Optimize for Getty Images with local & cloud Vision AI."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }

/* Zelený Privacy Callout Box s plnou podporou pro Světlý i Tmavý režim */
.privacy-callout {
  background-color: rgba(46, 164, 78, 0.08);
  border: 1px solid rgba(26, 127, 55, 0.3);
  border-radius: 6px;
  padding: 18px;
  margin: 25px auto;
  max-width: 900px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
}
.privacy-callout h4 {
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
  .privacy-callout {
    background-color: rgba(35, 134, 54, 0.15);
    border: 1px solid rgba(46, 164, 78, 0.4);
  }
  .privacy-callout h4 {
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

# ArtushVision AI | Professional Metadata Automation

<p align="center">
  <strong>The Ultimate AI-Powered Workstation for Metadata, Asset Management, and Global &amp; FTP Distribution.</strong>
</p>

<div id="flex-search-container">
  <input type="text" id="flex-search-input" placeholder="Search documentation (e.g., FTP, Ollama, Getty, Manual)...">
  <ul id="flex-results-container"></ul>
</div>

---

> **WHAT IS NEW: (New version will be available soon)** Complete standalone autonomy. Run powerful Vision &amp; Text models **100% locally and privately via Ollama** with zero API costs, map keywords seamlessly against the official **Getty Images Controlled Vocabulary**, and automate distribution with **per-server multi-threaded FTP uploads** and dynamic CSV mapping. Read the full [v1.10 Release Notes](/docs/whats-new.html).

---

<!-- LOKÁLNÍ AI A PRIVÁTNÍ ARCHIVY - NOVÝ ČISTÝ ZELENÝ BOX -->
<div class="privacy-callout">
  <h4>🔒 100% Offline Privacy for Travel, Home &amp; Personal Archives</h4>
  <p>
    Protect your family memories, private travel logs, and sensitive client shoots. By running advanced Vision models entirely <strong>locally via Ollama</strong>, your images are analyzed right on your own graphics card. <strong>No photos ever leave your computer</strong>, zero data is uploaded to corporate clouds, and absolute data logging privacy is fully guaranteed.
  </p>
</div>

---

<h3 align="center">💡 ZERO-RISK WORKFLOW: TRY BEFORE YOU BUY!</h3>

<table style="width: 100%; display: table; border-collapse: collapse;">
  <tr>
    <th style="width: 50%; text-align: center; padding: 12px;"><a href="/docs/download-purchase.html">Download Free Lite / Commercial Version</a></th>
    <th style="width: 50%; text-align: center; padding: 12px;"><a href="/docs/download-purchase.html#buy-lifetime-license">Get Lifetime License</a></th>
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

<br>

<p align="center">
  <strong>Securely processed by Polar &amp; Stripe.</strong> &bull; <a href="https://polar.sh">Manage your licensed devices</a>
</p>

---

## The 3-Step Production Workflow

ArtushVision AI eliminates the friction between editing software, AI tagging, and final asset organization:

1. **Load &amp; Cull:** Open thousands of RAW or JPG files across multiple subfolders instantly using the **Flat View**, filter out the noise, and organize your batch using native Lightroom-compatible star ratings and color labels.
2. **Generate &amp; Resolve:** Trigger the **Cloud or 100% Private Local AI** to build high-converting titles and tags. Run the **Getty Images Resolver** to automatically match official commercial taxonomies and clear homonym ambiguities in seconds.
3. **Automated FTP Upload:** Select your pre-saved Agency Profile and hit Upload. The software manages multi-threaded transfers, dynamically generates agency-specific CSV files on-the-fly, and automatically stamps your grid with visual success badges.

---

## Why ArtushVision AI?

*   **[Versatile AI Engine](/docs/ai-metadata-generation-cloud-local-ollama.html):** Choose between ultra-fast and accurate Cloud AI via OpenRouter or **100% Private Local AI** running fully offline via Ollama. Keep personal archives, home family photos, travel journals, or sensitive unreleased commercial shoots completely safe on your local drive with zero cloud logging and zero API costs.
*   **[Advanced Manual Keywording](/docs/smart-manual-keywording-batch-editing.html):** Take total control. Manually add, drag-and-drop reorder, or delete keyword bubbles, and easily assign relevant categories. Features real-time word counters, synonyms lookup, and multilingual spellcheck suggestions.
*   **[Smart Category Mapping](/docs/categories.html):** A customizable translation matrix that maps your internal metadata categories directly into agency-specific requirements (Adobe Stock, Dreamstime, etc.) with separate internal logic for Photo vs. Video assets.
* **[Getty Images Keyword Optimizer & Resolver](/docs/getty-images-esp-metadata-optimizer.html):** Validate keywords instantly against a built-in Master Dictionary of **9,867+** controlled Getty commercial terms. Choose between **fast and intuitive manual validation** or **AI-powered optimization** - available both for individual items and in **batches** - to ensure consistent, near-perfect acceptance rates.
*   **[Smart FTP Distribution](/docs/global-stock-distribution-ftp.html):** Simultaneously upload files to multiple stock agencies with automated, agency-specific CSV metadata generation on-the-fly.
*   **[Universal Compatibility](/docs/metadata-compatibility-and-file-handling.html):** Background integration using industry-standard formats compatible with Adobe Lightroom, Bridge, Zoner Photo Studio, and digiKam.

---

**ArtushVision AI Workspace**
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/grid-overview.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/grid-overview.png" alt="ArtushVision AI Interface" width="100%" class="screenshot-img">
</a>

---

## Cost Comparison: Own Your Tools

| Feature | Typical Online AI Tools | ArtushVision AI (Desktop App) |
| :--- | :--- | :--- |
| **Media Privacy** | Mandatory Cloud Upload | 🔒 **100% Private (Local AI via Ollama)** or Thumbnail-only modes |
| **Format Support** | JPG Only | **JPG, RAW, Video, TIFF, PNG, HEIC** |
| **Pricing Model** | Recurring Subscriptions / Credits | **Perpetual License ($39.99)** |
| **Cost (10,000 Photos)** | High-tier monthly plans | **~$0.30** using Gemini Flash or **$0.003** utilizing Local AI |

---

> **Exceptional Value:** Describe up to **150,000 photos for only $5** with perfect, high-quality results.
> **Full Cost Control:** Monitor your budget with built-in **spending statistics** (6-decimal precision).

---

## Complete Documentation Index

### 1. Getting Started
- [System Requirements &amp; Installation](/docs/installation.html)
- [First Launch &amp; Activation](/docs/download-purchase.html)
- [Interface Overview](/docs/interface-overview.html)
- [Detail Window Overview](/docs/detail-window-interface-overview.html)
- [Cloud AI &amp; OpenRouter API Setup](/docs/cloud-ai-openrouter-api-setup.html)
- [Local AI Setup &amp; Integrated Model Manager](/docs/local-ai-model-manager-ollama.html)

### 2. Core Workflows
- [Understanding AI Processing Modes (Cloud, Local, Hybrid)](/docs/ai-metadata-generation-cloud-local-ollama.html)
- [Advanced AI Prompting, Profiles &amp; Variables](/docs/advanced-ai-prompting-profiles-variables.html)
- [Manual Editing, Multi-language Spellcheck &amp; Interactive Map](/docs/smart-manual-keywording-batch-editing.html)
- [Batch Metadata Actions, Search &amp; Replace](/docs/batch-operations-metadata-library-management.html)
- [Smart Grid Filters and Search](/docs/smart-grid-filters-search-metadata-management.html)


### 3. Professional Asset Distribution
- [Getty Images ESP Metadata Optimizer &amp; Resolver](/docs/getty-images-esp-metadata-optimizer.html)
- [Global Stock Distribution &amp; Multi-threaded FTP Suite](/docs/global-stock-distribution-ftp.html)
- [Dynamic CSV Template Mapping](/docs/settings-configuration-customization.html#advanced-csv-template-editor)

### 4. Advanced Management

- [Workspace Theming, VRAM context tuning &amp; Data Safety](/docs/settings-configuration-customization.html)

---

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs &amp; Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

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