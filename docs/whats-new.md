---
title: "What's New in ArtushVision AI | Release Notes & Features"
description: "Discover the latest updates in ArtushVision AI (v1.10). Explore offline Ollama Vision models, Getty Images dictionary integration, and automated FTP microstock distribution."
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

# What's New in ArtushVision AI (v1.10)

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[Frequently Asked Questions (FAQ)](/docs/faq.html)

**Welcome to the official release notes hub for ArtushVision AI. We constantly update our desktop software with smarter AI photo tagging, deeper XMP metadata integration, and lightning-fast optimization tools driven by professional stock photography contributor feedback.**

Find out what has changed in the latest build (v1.10) and how these new advanced features can accelerate your daily keywording, culling, and multi-agency microstock distribution workflow.

<!-- [IMAGE: images/whats-new-hero-banner.png] -->

---

## Major Microstock Automation Enhancements

Update 1.10 is the biggest milestone in the application's development so far. It brings absolute independence with local AI support, professional microstock export tools, and advanced metadata management. 

Here is an overview of the most important additions:

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

* **[Interactive AI Mapping (Getty Resolver)](/docs/getty-images-esp-metadata-optimizer.html#interactive-ai-resolver-and-disambiguation):** An advanced visual table that checks your keywords against the massive Getty Master Dictionary (>9,867 approved commercial terms). You can edit, format, and split original and new words directly in-line using the [Getty Images ESP Metadata Optimizer](/docs/getty-images-esp-metadata-optimizer.html).
* **[Intelligent Semantic Disambiguation Assistant](/docs/getty-images-esp-metadata-optimizer.html#interactive-ai-resolver-and-disambiguation):** The Cloud AI engine can study the visual context of your photo and automatically decide which precise meaning of a word to select (e.g., reliably distinguishing a 'crane' bird from a 'crane' construction machine).
* **[Persistent User Dictionary](/docs/getty-images-esp-metadata-optimizer.html#built-in-master-dictionary):** The system features personal memory. Once you manually map a missing keyword or a custom name to an existing term from the Master database, the application remembers it for all future exports.
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
* **FTP Profiles and Status Badges:** Group your servers into custom FTP Profiles (e.g., "Video" or "Main Stock"). Uploaded agencies are then permanently visualized as colored micro-badges directly on the grid thumbnails for each photo and can be actively filtered using Smart Grid Filters and Search.

---

## Desktop UI and Linguistic Performance Updates

* **Advanced Undo/Redo Engine:** Made a mistake during a massive batch edit? The application now features a robust, 200-step local Undo/Redo stack (`Ctrl+Z` / `Ctrl+Y`). It perfectly restores not just text, but also keyword colors, star ratings, and rejection flags.
* **Lightroom Keyword Order Restoration:** Added a new **"Restore keywords and order after LR Export"** context menu action. This recovers the exact original sequence of keywords using `XMP-artush:KeywordOrder` metadata, fixing any keyword shuffling caused by Lightroom export pipelines.


### System & Interface Polish
* **Non-Destructive Keyword Sets & Predefined Presets:** Create, manage, and batch-apply custom preset combinations of tags (e.g., for specific locations or studio environments) that undergo instant deduplication and live spell checking. The application now comes preloaded with **24 curated predefined keyword sets** (including Landscape, Drone, Travel, Food, Plants, Animals, and more) to immediately boost your workflow.
* **Bi-Directional Lightroom & Zoner Integration:** All stars, flags, and custom tags map perfectly to standard XMP namespaces (like `XMP-dc`, `XMP-lr`), allowing seamless catalog synchronization via Adobe's "Read Metadata from Files" command. We have also added complete rating and color label synchronization for Zoner Photo Studio, ensuring seamless metadata exchange across Lightroom, Zoner Photo Studio, and ArtushVision AI.
* **Settings Backup & Migration:** Added a full, one-click ZIP backup of all custom profiles, AI prompts, and CSV templates, utilizing secure Windows DPAPI encryption to safely package credentials.

---

### [Get Started Now]
* Download Free Lite Version
* Purchase Lifetime License - $39.99

---

← Back to ArtushVision AI Home

❓ Frequently Asked Questions (FAQ)

💬 Support, Bugs & Community Forum

---

*ArtushVision AI - Stability and precision for professional photography workflows.*