---
title: "What's New in ArtushVision AI | Release Notes & Features"
description: "Discover the latest updates in ArtushVision AI (v1.10). Explore offline Ollama Vision models, Getty Images dictionary integration, and automated FTP microstock distribution."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
</style>
</div>

# What's New in ArtushVision AI (v1.10)

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[Frequently Asked Questions (FAQ)](faq.html)

**Welcome to the official release notes hub for ArtushVision AI. We constantly update our desktop software with smarter AI photo tagging, deeper XMP metadata integration, and lightning-fast optimization tools driven by professional stock photography contributor feedback.**

Find out what has changed in the latest build (v1.10) and how these new advanced features can accelerate your daily keywording, culling, and multi-agency microstock distribution workflow.

[IMAGE: images/whats-new-hero-banner.png]

---

## Major Microstock Automation Enhancements

Update 1.10 is the biggest milestone in the application's development so far. It brings absolute independence with local AI support, professional microstock export tools, and advanced metadata management. 

Here is an overview of the most important additions:

### Local, Hybrid, and 2-Pass Offline Vision AI
The application no longer relies solely on cloud APIs. We have fully integrated the Ollama system, allowing you to run powerful AI models to process your sensitive (or massive) batches of photos 100% locally, for free, and in complete privacy.

* **Three Independent AI Photo Tagging Engines:** * **Local AI**: Run standard visual analysis on your local hardware with zero API costs (see the [Ollama Installation Guide](ollama-installation-guide.html)).
    * **Hybrid AI (Local Vision + Cloud Text)**: *Our recommended mode*. Your graphics card securely and freely performs the demanding visual analysis. The extracted text metadata is then sent to a cheap but highly intelligent cloud model for lightning-fast SEO formatting. Learn more in the [AI Metadata Generation Guide](ai-metadata-generation-cloud-local-ollama.html).
    * **Enhanced Local AI (2-Pass Offline)**: Maximum quality completely offline. First, a local Vision model reads the photo, then a *second* specialized local text model creates a perfect JSON with keywords.
* **2-Pass Batch Processing:** A special background batching architecture that prevents GPU VRAM overload and drastically speeds up processing times for thousands of RAW files.
* **Live VRAM/RAM Hardware Monitor:** A live memory consumption indicator located in the bottom status bar, tracking real-time load of your active Ollama models.

### Integrated Local AI Model Manager for Ollama
AI model management is now fully integrated directly into the ArtushVision user interface. No need to open the Windows terminal or command line.

* **Curated Recommended Models Catalog:** Browse and download the best available Vision and Text models for photography analysis with a single click directly from the [Local AI Model Manager](local-ai-model-manager-ollama.html).
* **Smart Management and Detection:** The downloaded models table shows physical size in GB, parameter count, and quantization level. The app automatically detects whether it is a Vision (image-to-text) or Text model.
* **Custom Personal Notes:** Double-click any model row to add your own performance tags and custom notes (e.g., "Best for illustrations" or "Fast descriptions").

### Getty Images Resolver and Custom Vocabulary Dictionary
A brand new set of linguistic tools designed to solve the hardest task in the microstock world: creating valid metadata that strictly complies with Getty Images / iStock ESP requirements.

* **Interactive AI Mapping (Getty Resolver):** An advanced visual table that checks your keywords against the massive Getty Master Dictionary (>11,000 approved commercial terms). You can edit, format, and split original and new words directly in-line using the [Getty Images ESP Metadata Optimizer](getty-images-esp-metadata-optimizer.html).
* **Intelligent Semantic Disambiguation Assistant:** The Cloud AI engine can study the visual context of your photo and automatically decide which precise meaning of a word to select (e.g., reliably distinguishing a 'crane' bird from a 'crane' construction machine).
* **Persistent User Dictionary:** The system features personal memory. Once you manually map a missing keyword or a custom name to an existing term from the Master database, the application remembers it for all future exports.

### Smart Category Matrix and Bulk Portfolio Management
No more manual sorting and categorizing for each stock agency separately.

* **Cross-Agency AI Category Mapping:** We created a flexible Category Matrix. The AI model receives a list of your "Master Categories" and assigns the best ones to the photo. These categories are then automatically translated into the correct numerical ID formats for Shutterstock, Adobe Stock, Alamy, or Motion Elements during export or upload via the [Settings and Configuration Guide](settings-configuration-customization.html#the-category-matrix).
* **Motion Elements (Video vs Photo Logic):** The matrix intelligently distinguishes photo and video formats, automatically funneling assets into the correct technical subcategories required by Motion Elements.
* **Bulk Adding from Image Grid:** A new Categories button in the batch edit bar opens a dialog for quick manual selection (up to 3 categories) for hundreds of selected photos at once. You can also define properties, model releases, and editorial flags in bulk using [Smart Manual Keywording and Culling](smart-manual-keywording-batch-editing.html).

### Smart FTP Manager and Automated One-Click CSV Generation
The entire stock photo and video upload process has been rewritten from the ground up to be fully independent, multi-threaded, and automated.

* **Assign CSV Template per Server:** In the FTP upload window, you can now assign a specific CSV template format to each agency profile (server).
* **One-Click Temporary CSV Generation:** When active, the app automatically takes the uploaded photos, generates a temporary CSV tailored to the specific agency, uploads the CSV file immediately after the media files, and then cleanly purges it from your computer. Read the complete setup in the [Global Stock Distribution & FTP Guide](global-stock-distribution-ftp.html).
* **Advanced Server Settings (Thread Limits):** The number of concurrent uploads (threads) is no longer global but set individually for each FTP server. You can safely send to Shutterstock with 10 photos at once, while limiting Zoonar to 1 thread to prevent connection blocks (`421 Too many connections`).
* **FTP Profiles and Status Badges:** Group your servers into custom FTP Profiles (e.g., "Premium Video" or "Main Stock"). Uploaded agencies are then permanently visualized as colored micro-badges directly on the grid thumbnails for each photo and can be actively filtered using [Smart Grid Filters and Search](smart-grid-filters-search.html).

---

## Technical Performance Updates

* **Settings Backup & Migration:** Added a full, one-click ZIP backup of all custom profiles, AI prompts, and CSV templates (see [Metadata Compatibility and File Handling](metadata-compatibility-and-file-handling.html)).
* **UI Safety Enhancements:** Unified validation limit colors and introduced 100% protection against AI API error states.
* **Zero UI Freezing:** Completely optimized grid memory to prevent application freezing when bulk-selecting or mass-editing thousands of high-resolution items simultaneously.

---

### [Get Started Now]

* [Download Latest Version](https://www.artushfoto.eu/Software/Download-ArtushVision-AI)
* [Purchase Lifetime License - $39.99](https://www.artushfoto.eu/Software/Purchase-ArtushVision-AI)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[Frequently Asked Questions (FAQ)](faq.html)

---

*ArtushVision AI - Professional precision and complete metadata automation.*