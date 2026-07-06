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
  width: 230px; /* Zmenšeno pro jistotu, že se vejdou vedle sebe */
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
  margin: 15px 0 25px 0; /* Změněno auto na 0 pro zarovnání vlevo */
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

<main>

<h1 style="text-align: left; margin-top: 0; padding-top: 0; font-size: 2.2em;">ArtushVision AI | Professional Metadata Automation</h1>

<div style="width: 100%; max-width: 1200px; margin: 0 auto 20px auto; border: 1px solid #333; border-radius: 6px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); overflow: hidden; background-color: #253544; line-height: 0;">
  <object type="image/svg+xml" data="artushvision.svg" style="width: 100%; height: auto; aspect-ratio: 841.89 / 210.47; display: block; pointer-events: auto !important; outline: none; border: none; margin: 0; padding: 0;">
    <img src="artushvision.svg" alt="ArtushVision AI Software Features - Smart Microstock Tagging" />
  </object>
</div>

<hr>

<div class="hero-split">
  <div class="hero-text">
    <p style="font-size: 1.1em; line-height: 1.5; margin-top: 0;"><strong>The Ultimate AI-Powered Workstation for Metadata, Asset Management, and Global &amp; FTP Distribution.</strong></p>
    
    <blockquote style="margin: 20px 0 20px 0; font-size: 0.95em; color: #57606a; padding-left: 15px; border-left: 4px solid #0969da; font-style: italic;">
      "ArtushVision AI has rapidly evolved into the <strong>Swiss Army Knife of metadata management</strong>... From handling keywording of raw files, resolving the annoying Lightroom habit of sorting keywords alphabetically, to providing a smooth solution for the Getty/iStock controlled vocabulary... <strong>this is very hard to beat.</strong>"
      <br>
      <span style="display: block; margin-top: 8px; font-style: normal; font-size: 0.85em; font-weight: 600; color: #24292f;">
        &mdash; Steven Heap, BackyardSilver (<a href="/docs/artushvision-reviews.html" title="Read full user reviews">Read Full Review &rarr;</a>)
      </span>
    </blockquote>
    
    <div style="display: flex; gap: 15px; flex-wrap: wrap;">
      <a href="/docs/download-purchase.html" class="btn btn-primary">Download Free Trial</a>
      <a href="/docs/download-purchase.html#buy-lifetime-license" class="btn btn-success">Buy License - $39.99</a>
    </div>
  </div>
  
  <div class="hero-image">
    <a href="artushvision.webp" target="_blank" rel="noopener noreferrer" class="screenshot-link" style="margin: 0;">
      <img src="artushvision.webp" alt="Detail of ArtushVision AI split-screen workflow" width="2005" height="1333" loading="lazy" class="screenshot-img" />
    </a>
  </div>
</div>

<hr>

<div class="privacy-callout">
  <h2>🔒 100% Offline Privacy for Travel, Home &amp; Personal Archives</h2>
  <p>
    Protect your family memories, private travel logs, and sensitive client shoots. By running advanced Vision models entirely <strong>locally on your own hardware</strong>, your images are analyzed right on your graphics card. <strong>No photos ever leave your computer</strong>, zero data is uploaded to corporate clouds, and absolute data logging privacy is fully guaranteed.
  </p>
</div>

<hr>

<p><strong>STOP paying rent</strong> for your software or credits. For just $39.99, the price of a <strong>casual dinner for two</strong>, you get a powerful tool that is yours forever. <strong>No expensive monthly subscriptions</strong>, no strings attached. Run it <strong>completely offline for maximum privacy</strong>, or connect to <strong>cloud AI</strong> whenever you need it with <strong>total control</strong> over your usage and costs. <strong>It’s a one-time investment that pays for itself in just two hours of saved work.</strong></p>

<hr>

<h2>The 3-Step Production Workflow</h2>

<p>ArtushVision AI eliminates the friction between editing software, AI tagging, and final asset organization:</p>

<ol>
  <li><strong>Load &amp; Cull:</strong> Open thousands of RAW or JPG files across multiple subfolders instantly using the <strong>Flat View</strong>, filter out the noise, and organize your batch using native Lightroom-compatible star ratings and color labels.</li>
  <li><strong>Generate &amp; Resolve:</strong> Trigger the <strong>Cloud or 100% Private Local AI</strong> to build high-converting titles and tags. Run the <strong>built-in AI/Offline Getty Resolver</strong> to automatically match official commercial taxonomies and clear homonym ambiguities in seconds.</li>
  <li><strong>Automated FTP Upload:</strong> Select your pre-saved Agency Profile and hit Upload. The software manages multi-threaded transfers, dynamically generates agency-specific CSV files on-the-fly, and automatically stamps your grid with visual success badges.</li>
</ol>

<hr>

<h2>Why ArtushVision AI?</h2>

<ul>
  <li><strong><a href="/docs/ai-metadata-generation-cloud-local-ollama.html">Versatile AI Engine</a>:</strong> Choose between ultra-fast and accurate Cloud AI via OpenRouter or <strong>100% Private Local AI</strong> running fully offline. Keep personal archives, home family photos, travel journals, or sensitive unreleased commercial shoots completely safe on your local drive with zero cloud logging and zero API costs.</li>
  <li><strong><a href="/docs/smart-manual-keywording-batch-editing.html">Advanced Manual Keywording</a>:</strong> Take total control. Manually add, drag-and-drop reorder, or delete keyword bubbles, and easily assign relevant categories. Features real-time word counters, synonyms lookup, and multilingual spellcheck suggestions.</li>
  <li><strong><a href="/docs/category-matrix.html">Smart Category Mapping</a>:</strong> A customizable translation matrix that maps your internal metadata categories directly into agency-specific requirements (Adobe Stock, Dreamstime, etc.) with separate internal logic for Photo vs. Video assets.</li>
  <li><strong><a href="/docs/getty-images-esp-metadata-optimizer.html">Getty Images Keyword Optimizer &amp; Resolver</a>:</strong> Validate keywords instantly against a built-in Master Dictionary of <strong>9,867+</strong> controlled Getty commercial terms. Choose between <strong>fast and intuitive manual validation</strong> or <strong>AI-powered optimization</strong> - available both for individual items and in <strong>batches</strong> - to ensure consistent, near-perfect acceptance rates.</li>
  <li><strong><a href="/docs/global-stock-distribution-ftp.html">Smart FTP Distribution</a>:</strong> Simultaneously upload files to multiple stock agencies with automated, agency-specific CSV metadata generation on-the-fly.</li>
  <li><strong><a href="/docs/metadata-compatibility-and-file-handling.html">Universal Compatibility</a>:</strong> Background integration using industry-standard formats compatible with Adobe Lightroom, Bridge, Zoner Photo Studio, and digiKam. ArtushVision AI lets you easily restore your original <strong>custom keyword order</strong> after Lightroom reshuffles it during export, safely appending any newly added tags to the end of the list.</li>
</ul>

<hr>

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

<p><strong>ArtushVision AI Main Grid Workspace</strong></p>
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/grid-overview.webp" target="_blank" rel="noopener noreferrer" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/grid-overview.webp" alt="ArtushVision AI Workspace showing automated metadata generation" width="3066" height="1885" class="screenshot-img" loading="lazy" />
</a>

<hr>

<h2>Cost Comparison: Own Your Tools</h2>

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

<blockquote style="margin: 20px 0; padding-left: 15px; border-left: 4px solid #d0d7de; color: #57606a;">
  <p><strong>Exceptional Value:</strong> Describe up to <strong>10,000 photos for only $6</strong> with perfect, high-quality results.<br>
  <strong>Full Cost Control:</strong> Monitor your budget with built-in <strong>spending statistics</strong> (6-decimal precision).</p>
</blockquote>

<hr>

<h2>Complete Documentation Index</h2>

<div id="flex-search-container">
  <input type="text" id="flex-search-input" placeholder="Search documentation..." />
  <ul id="flex-results-container"></ul>
</div>

<h3>1. Getting Started</h3>
<ul>
  <li><a href="/docs/installation.html">System Requirements &amp; Installation</a></li>
  <li><a href="/docs/download-purchase.html">First Launch &amp; Activation</a></li>
  <li><a href="/docs/interface-overview.html">Interface Overview</a></li>
  <li><a href="/docs/detail-window-interface-overview.html">Detail Window Overview</a></li>
  <li><a href="/docs/cloud-ai-openrouter-api-setup.html">Cloud AI &amp; OpenRouter API Setup</a></li>
  <li><a href="/docs/local-ai-model-manager-ollama.html">Local AI Setup &amp; Integrated Model Manager</a></li>
</ul>

<h3>2. Core Workflows</h3>
<ul>
  <li><a href="/docs/ai-metadata-generation-cloud-local-ollama.html">Understanding AI Processing Modes (Cloud, Local, Hybrid)</a></li>
  <li><a href="/docs/how-to-download-local-ai-models-via-ollama.html">How to Download Local AI Models via Ollama</a></li>
  <li><a href="/docs/local-ai-model-manager-ollama.html">Local AI Model Manager: Complete Offline Control</a></li>
  <li><a href="/docs/advanced-ai-prompting-profiles-variables.html">Advanced AI Prompting, Profiles &amp; Variables</a></li>
  <li><a href="/docs/create-and-optimize-custom-ai-prompts.html">Create and Optimize Custom AI Prompts</a></li>
  <li><a href="/docs/smart-manual-keywording-batch-editing.html">Manual Editing, Multi-language Spellcheck &amp; Interactive Map</a></li>
  <li><a href="/docs/batch-operations-metadata-library-management.html">Batch Metadata Actions, Search &amp; Replace</a></li>
  <li><a href="/docs/category-matrix.html">Microstock Category Mapping Matrix</a></li>
  <li><a href="/docs/smart-grid-filters-search-metadata-management.html">Smart Grid Filters and Search</a></li>
</ul>

<h3>3. Professional Asset Distribution</h3>
<ul>
  <li><a href="/docs/getty-images-esp-metadata-optimizer.html">Getty Images ESP Metadata Optimizer &amp; Resolver</a></li>
  <li><a href="/docs/global-stock-distribution-ftp.html">Global Stock Distribution &amp; Multi-threaded FTP Suite</a></li>
  <li><a href="/docs/settings-configuration-customization.html#advanced-csv-template-editor">Dynamic CSV Template Mapping</a></li>
</ul>

<h3>4. Advanced Management</h3>
<ul>
  <li><a href="/docs/settings-configuration-customization.html">Workspace Theming, VRAM context tuning &amp; Data Safety</a></li>
</ul>

<hr>

<h3>Get Started Now</h3>
<ul>
  <li><a href="/docs/download-purchase.html">Download Free Lite Version</a></li>
  <li><a href="/docs/download-purchase.html#buy-lifetime-license">Purchase Lifetime License - $39.99</a></li>
</ul>

<hr>

<p>
  <a href="https://vision.artushfoto.eu">← Back to ArtushVision AI Home</a><br><br>
  <a href="/docs/faq.html">❓ Frequently Asked Questions (FAQ)</a><br><br>
  <a href="/docs/artushvision-reviews.html">⭐ User Reviews &amp; Testimonials</a><br><br>
  <a href="https://github.com/Artushfoto/ArtushVision-AI/discussions">💬 Support, Bugs &amp; Community Forum</a>
</p>

<hr>

<p><i>ArtushVision AI - Stability and precision for professional photography workflows.</i></p>

</main>

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