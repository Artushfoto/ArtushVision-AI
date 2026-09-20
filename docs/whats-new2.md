---
title: "What's New in ArtushVision AI | Release Notes & Features"
description: "Discover the latest updates in ArtushVision AI (v1.20). Explore Advanced SEO & Market Intelligence, Selling Score, Bestseller GAP analysis, Ground-Truth Verification, direct MP4 metadata injection, and bulk CSV export."
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

# What's New in ArtushVision AI (v1.20)

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[Frequently Asked Questions (FAQ)](/docs/faq.html)

**Welcome to the official release notes hub for ArtushVision AI. Update 1.20 marks a monumental leap forward: transforming ArtushVision AI from an intelligent metadata tagger into a comprehensive Commercial Market Intelligence and Strategic SEO Suite engineered exclusively for professional stock photographers and videographers.**

---

## Advanced SEO & Market Intelligence for Stock Photography

In version 1.20, keywording is no longer a guessing game. By coupling visual neural networks with our 340,000+ stock keyword market database (featuring real monthly search volumes and live competition numbers from Shutterstock and Adobe Stock), ArtushVision AI ensures your assets rank at the top of agency search engines where buyers actually spend money.

### The Three Pillars of ArtushVision Intelligence
Every keyword recommendation and score calculation is governed by three symbiotic dimensions:
1. **Visual & Semantic Ground-Truth:** Deep 768-dimensional BGE vector embeddings ensure that every suggested term directly correlates with the physical contents of your image or video.
2. **Real Market Demand & Search Volume:** Powered by real search counts and commercial query frequencies from major microstock agencies rather than arbitrary language model guesses.
3. **Buyer & Transactional Intent:** Prioritizes terms buyers actually type when ready to license (commercial phrases, conceptual business hooks, specific subjects) over low-converting descriptive fluff.

### Selling Score (10–99 Commercial Rating Engine)
ArtushVision AI now computes a unified, scientifically grounded **Selling Score** for every image and video:
* **Holistic Quality Evaluation:** Blends top-ranking commercial keywords, keyword density balance, query simulation curves, and title/description synergy.
* **Real-Time Dynamic Thumbnail Badges:** Color-coded badges right on your grid thumbnails instantly highlight the commercial readiness of hundreds of assets at a glance without having to open them individually.
* **Over-Optimization & Dilution Protection:** Penalizes keyword stuffing, redundant substrings, and keyword counts outside the sweet spot (25–35 terms).

### Intelligent SEO Sort & Strategic Positioning
Search engines on Adobe Stock and Shutterstock assign significantly greater algorithmic weight to your **first 10 to 15 keywords**:
* **Verdict Tier Clustering:** With one click (`⚡ SEO Sort` or `Ctrl+Shift+S`), high-converting **🔥 MUST USE** phrases and **✅ RECOMMENDED** terms are automatically elevated to primary ranking positions.
* **Automated Generic Cap:** Enforces a strict ceiling (maximum 3 generic core tags in the top 15 slots), preventing broad words like *nature*, *background*, or *animal* from displacing high-value long-tail phrases.

### Bestseller GAP Analysis
Find out what top-earning portfolios have that you are missing:
* **Competitive Intelligence:** Cross-references your image against top-performing bestselling assets in the same commercial niche.
* **Missing High-Yield Tags:** Identifies high-converting keywords frequently used by bestsellers that are completely absent from your metadata.
* **1-Click Insertion:** Add individual missing keywords or the entire missing gap set with a single click.

### Commercial Phrases Engine
Single words are saturated; multi-word commercial phrases make sales:
* **High-Converting Buyer Phrases:** Mines multi-word search queries (*"isolated on white"*, *"copy space"*, *"aerial view"*, *"wildlife in nature"*) directly from successful stock assets.
* **Topic-Noun Compatibility Filter:** Prevents mismatched modifier combinations while keeping multi-word phrases natural and commercially targeted.

### Market Discovery (Satellite Resolver)
Tap into high-demand keywords before the rest of the market catches up:
* **Untapped Microstock Niches:** Leverages vector cosine similarity over emerging buyer search queries to highlight high-demand, low-competition tags.
* **Early Trend Capitalization:** Pinpoints trending search trends before they become oversaturated with millions of competitor files.

### Ground-Truth Verification: Geo & Taxonomic Intelligence
Say goodbye to buyer complaints, agency rejections, and AI hallucinations:
* **Deterministic GPS Geocoding:** Reads EXIF coordinates and validates geographical keywords against an integrated offline reverse-geocoder (OpenStreetMap / ArcGIS). Completely prevents country hallucinations (e.g. tagging *Portugal* on a photo captured in *Prague*).
* **Biological Taxonomy & Species Conflict Guard:** Understands hypernym hierarchies (knowing an *Anhinga* is an *avian/water bird/wildlife*), while strictly rejecting conflicting species (preventing *falcon* or *hawk* from polluting an eagle image).
* **CLIP People Verification:** Neural detection verifies human presence. Empty landscapes safely retain the commercially lucrative tag *"no people"* while permanently blocking erroneous human tags (*portrait, man, crowd*).

### Synonyms Inspector & Buyer-Intent Autocomplete
* **Stock Autocomplete Suggestions:** Type or inspect any keyword to see real-time buyer autocompletions straight from microstock search bars.
* **Contextual Replacements & Definitions:** Inspect word definitions, explore high-yield synonyms, and perform 1-click swaps or additions.
* **Instant Multi-Language Translation:** Seamlessly translates tags across 20+ languages so international contributors can keyword with native confidence.

### Smart SEO Expand
* **Curated Low-Noise Suggestions:** Dynamically generates 10–15 top-tier related candidates tailored to your current seed keywords.
* **Visual Separation Layout:** Neatly separates new discovery suggestions from existing tags with an intuitive bubble gap interface.

### Explainable AI Verdicts & Quick Wins
* **Actionable Decision Badges:** Every tag is classified into transparent tiers:
  * **🔥 MUST USE:** Essential high-volume and high-relevance terms.
  * **✅ RECOMMENDED:** High-converting commercial terms.
  * **⚠️ OPTIONAL:** Purely descriptive or contextual tags.
  * **❌ AVOID:** Redundant substrings, species conflicts, or dead-trend terms.
* **Quick Wins Audit Bar:** Real-time diagnostics provide 1-click fixes for metadata health (e.g., removing redundant single words contained inside phrases).

---

## Complete Workflow & File Format Freedom

### Direct Metadata Write to Video MP4 / MOV (Lossless In-Place Injection)
ArtushVision AI now brings true native metadata management to stock videographers:
* **No Re-encoding, Sub-Second Speed:** Patches XMP metadata directly into ISOBMFF/QuickTime atoms (`moov/udta` & UUID boxes) in milliseconds without re-encoding video streams or altering visual quality.
* **Adobe Bridge & Agency Compatibility:** 100% compliant with Adobe Bridge, Adobe Premiere, DaVinci Resolve, Shutterstock, Adobe Stock, and Pond5.

### Universal Drag & Drop
* **Frictionless Ingestion:** Simply drag and drop entire folders, mixed batches of RAW images, JPGs, or MP4/MOV videos directly from Windows Explorer straight into the ArtushVision grid.

### Multiple CSV Export
* **One-Click Multi-Agency Distribution:** Export your selected assets into multiple custom agency CSV templates (e.g., Shutterstock, Adobe Stock, Pond5, Dreamstime) simultaneously in a single pass.
* **Template Memory:** Remembers your preselected agency targets for effortless recurring export routines.

---

## Previous Releases: What's New in ArtushVision AI (v1.10)

Update 1.10 was the milestone that introduced local offline AI models, Getty Images dictionary integration, and multi-threaded FTP uploads.

### Local, Hybrid, and 2-Pass Offline Vision AI
The application no longer relies solely on cloud APIs. We have fully integrated the Ollama system, allowing you to run powerful AI models to process your sensitive (or massive) batches of photos 100% locally, for free, and in complete privacy.

* **Three Independent AI Photo Tagging Engines:**
    * **[Local AI](/docs/ai-metadata-generation-cloud-local-ollama.html#2-local-ai)**: Run standard visual analysis on your local hardware with zero API costs (see the [Ollama Installation Guide](/docs/ollama-installation-guide.html)).
    * **[Hybrid AI (Local Vision + Cloud Text)](/docs/ai-metadata-generation-cloud-local-ollama.html#3-hybrid-ai)**: Our recommended mode. Your graphics card securely and freely performs the demanding visual analysis. The extracted text metadata is then sent to a cheap but highly intelligent cloud model for lightning-fast SEO formatting. Learn more in the [AI Metadata Generation Guide](/docs/ai-metadata-generation-cloud-local-ollama.html).
    * **[Enhanced Local AI (2-Pass Offline)](/docs/ai-metadata-generation-cloud-local-ollama.html#4-two-step-local-ai)**: Maximum quality completely offline. First, a local Vision model reads the photo, then a *second* specialized local text model creates a perfect JSON with keywords.
* **2-Pass Batch Processing:** A special background batching architecture that prevents GPU VRAM overload and drastically speeds up processing times for thousands of RAW files.
* **Live VRAM/RAM Hardware Monitor:** A live memory consumption indicator located in the bottom status bar, tracking real-time load of your active Ollama models.
* **Remote Ollama Server Support:** Run visual analysis on a separate machine. In Settings, you can now specify a custom Ollama network API URL to connect to a powerful GPU server in your local network (LAN) instead of running it locally.

### [Integrated Local AI Model Manager for Ollama](/docs/local-ai-model-manager-ollama.html)
AI model management is now fully integrated directly into the ArtushVision user interface. No need to open the Windows terminal or command line.

* **Curated Recommended Models Catalog:** Browse and download the best available Vision and Text models for photography analysis with a single click directly from the [Local AI Model Manager](/docs/local-ai-model-manager-ollama.html).
* **Smart Management and Detection:** The downloaded models table shows physical size in GB, parameter count, and quantization level (recommending the **Q4_0** sweet spot for standard 8GB VRAM cards). The app automatically detects whether it is a Vision (image-to-text) or Text model.
* **Custom Personal Notes:** Double-click any model row to add your own performance tags and custom notes (e.g., "Best for illustrations" or "Fast descriptions, struggles with complex JSON").

### [Getty Images Resolver and Custom Vocabulary Dictionary](/docs/getty-images-esp-metadata-optimizer.html)
A brand new set of linguistic tools designed to solve the hardest task in the microstock world: creating valid metadata that strictly complies with Getty Images / iStock ESP requirements.

* **[Interactive AI Mapping (Getty Resolver)](/docs/getty-images-esp-metadata-optimizer.html):** An advanced visual table that checks your keywords against the massive Getty Master Dictionary (>9,867 approved commercial terms). You can edit, format, and split original and new words directly in-line using the [Getty Images ESP Metadata Optimizer](/docs/getty-images-esp-metadata-optimizer.html).
* **[Intelligent Semantic Disambiguation Assistant](/docs/getty-images-esp-metadata-optimizer.html#offline-resolving-local-semantics):** The Cloud AI engine can study the visual context of your photo and automatically decide which precise meaning of a word to select (e.g., reliably distinguishing a 'crane' bird from a 'crane' construction machine).
* **[Persistent User Dictionary](/docs/getty-images-esp-metadata-optimizer.html#1-built-in-getty-master-dictionary--non-destructive-workflow):** The system features personal memory. Once you manually map a missing keyword or a custom name to an existing term from the Master database, the application remembers it for all future exports.
* **Interactive Getty Term Badge Counters:** A dynamic badge on each photo thumbnail in the Getty Resolver shows the count of currently valid terms. The badge turns green when reaching the recommended 5 terms threshold and red if below it, allowing instant visual quality checks.
* **1-Click Batch Optimization:** Run automatic resolution on entire batches using a single click, instantly matching keywords against the Master dictionary and your personal memory.
* **Auto-Save & Sidecar State Persistence:** The resolver now automatically saves your progress into temporary sidecar JSON files, protecting your work from power loss or accidental window closures.

### [Smart Category Matrix and Bulk Portfolio Management](/docs/settings-configuration-customization.html#the-category-matrix)
No more manual sorting and categorizing for each stock agency separately.

* **Cross-Agency AI Category Mapping:** We created a flexible Category Matrix. The AI model receives a list of your "Master Categories" and assigns the best ones to the photo. These categories are then automatically translated into the correct numerical ID formats for Shutterstock, Adobe Stock, or Motion Elements during export or upload via the [Settings and Configuration Guide](/docs/settings-configuration-customization.html#the-category-matrix).
* **Motion Elements (Video vs Photo Logic):** The matrix intelligently distinguishes photo and video formats, automatically funneling assets into the correct technical subcategories required by Motion Elements.
* **Separate Motion Elements Categories:** The category matrix now maps distinct photo and video categories for Motion Elements, ensuring compliance with their technical upload guidelines.
* **Bulk Adding from Image Grid:** A new Categories button in the batch edit bar opens a dialog for quick manual selection (up to 3 categories) for hundreds of selected photos at once. You can also define properties, model releases, and editorial flags in bulk using [Smart Manual Keywording and Culling](/docs/smart-manual-keywording-batch-editing.html).

### [Smart FTP Manager and Automated One-Click CSV Generation](/docs/global-stock-distribution-ftp.html)
The entire stock photo and video upload process has been rewritten from the ground up to be fully independent, multi-threaded, and automated.

* **Assign CSV Template per Server:** In the FTP upload window, you can now assign a specific CSV template format to each agency profile (server).
* **One-Click Temporary CSV Generation:** When active, the app automatically takes the uploaded photos, generates a temporary CSV tailored to the specific agency, uploads the CSV file immediately after the media files, and then cleanly purges it from your computer. Read the complete setup in the [Global Stock Distribution & FTP Guide](/docs/global-stock-distribution-ftp.html).
* **[Advanced Server Settings (Thread Limits)](/docs/global-stock-distribution-ftp.html#per-server-multi-threading-and-auto-retry):** The number of concurrent uploads (threads) is no longer global but set individually for each FTP server. You can safely send to Shutterstock with 10 photos at once, while limiting Zoonar to 1 thread to prevent connection blocks (`421 Too many connections`).
* **One-Click Server Profile Duplication:** Easily duplicate existing FTP server configurations with a single click to set up multiple accounts or subfolders for the same stock agency.
* **[FTP Profiles and Status Badges:](/docs/global-stock-distribution-ftp.html#advanced-tracking-and-visual-status-badges)** Group your servers into custom FTP Profiles (e.g., "Video" or "Main Stock"). Uploaded agencies are then permanently visualized as colored micro-badges directly on the grid thumbnails for each photo and can be actively filtered using Smart Grid Filters and Search.

---

## Desktop UI and Linguistic Performance Updates

* **Advanced Undo/Redo Engine:** Made a mistake during a massive batch edit? The application now features a robust, 200-step local Undo/Redo stack (`Ctrl+Z` / `Ctrl+Y`). It perfectly restores not just text, but also keyword colors, star ratings, and rejection flags.
* **[Lightroom Keyword Order Restoration:](/docs/metadata-compatibility-and-file-handling.html#seamless-integration-with-adobe-lightroom-and-other-managers)** Added a new **"Restore keywords and order after LR Export"** context menu action. This recovers the exact original sequence of keywords using `XMP-artush:KeywordOrder` metadata, fixing any keyword shuffling caused by Lightroom export pipelines.

### System & Interface Polish
* **[Non-Destructive Keyword Sets & Predefined Presets:](/docs/smart-manual-keywording-batch-editing.html#keyword-sets-presets)** Create, manage, and batch-apply custom preset combinations of tags (e.g., for specific locations or studio environments) that undergo instant deduplication and live spell checking. The application now comes preloaded with **24 curated predefined keyword sets** (including Landscape, Drone, Travel, Food, Plants, Animals, and more) to immediately boost your workflow.
* **Bi-Directional Lightroom & Zoner Integration:** All stars, flags, and custom tags map perfectly to standard XMP namespaces (like `XMP-dc`, `XMP-lr`), allowing seamless catalog synchronization via Adobe's "Read Metadata from Files" command. We have also added complete rating and color label synchronization for Zoner Photo Studio, ensuring seamless metadata exchange across Lightroom, Zoner Photo Studio, and ArtushVision AI.
* **Settings Backup & Migration:** Added a full, one-click ZIP backup of all custom profiles, AI prompts, and CSV templates, utilizing secure Windows DPAPI encryption to safely package credentials.

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
