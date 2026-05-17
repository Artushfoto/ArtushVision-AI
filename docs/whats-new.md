---
title: "What's New in ArtushVision AI | Release Notes"
description: "Explore the latest features, performance upgrades, and workflow enhancements in ArtushVision AI. Stay up to date with professional metadata automation."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
</style>
</div>

# What's New in ArtushVision AI

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[❓ Frequently Asked Questions (FAQ)](faq.html)

**Welcome to the release hub for ArtushVision AI. We constantly update the application with smarter automation, deeper metadata integration, and lightning-fast optimization tools driven by professional stock contributor feedback.**

Find out what has changed in the latest build and how these new features can accelerate your daily keywording and distribution workflow.

[IMAGE: images/whats-new-hero-banner.png]

---

## Main Features

# What's New in ArtushVision AI (v1.10)

Update 1.10 is the biggest milestone in the application's development so far. It brings absolute independence with local AI support, professional microstock export tools, and advanced metadata management. 

Here is an overview of the most important additions since version 1.02:

## Local, Hybrid, and 2-Pass Offline AI
The application no longer relies solely on cloud APIs. We have integrated the Ollama system, allowing you to process your sensitive (or massive) batches of photos 100% locally, for free, and in complete privacy.

*   **Three new independent AI Engines:** 
    *   **Local AI**: Standard analysis on local hardware.
    *   **Hybrid AI (Local Vision + Cloud Text)**: *Recommended mode*. Your graphics card securely and freely performs the demanding visual analysis (reading pixels). The extracted text is then sent to a cheap but highly intelligent cloud model for lightning-fast SEO formatting. 
    *   **Enhanced Local AI (2-Pass Offline)**: Maximum quality completely offline. First, a local Vision model reads the photo, then a *second* specialized local text model creates a perfect JSON with keywords.
*   **2-Pass Batching:** A special batch processing architecture that prevents VRAM overload and drastically speeds up the process.
*   **Live VRAM/RAM Monitor:** A live memory consumption indicator in the bottom bar showing the load of Ollama models.

## Integrated Model Manager for Ollama
AI model management is now fully integrated directly into the ArtushVision user interface. No need to open the terminal.

*   **Recommended Models Catalog:** Browse and download the best available models for visual and text analysis with a single click directly from the app.
*   **Smart Management and Detection:** The downloaded models table shows size in GB, parameter count, and quantization level. The app try automatically detects whether it is a Vision or Text model.
*   **Custom Notes:** Double-click any model to add your own tags and notes (e.g., "Best for illustrations").

## Getty Resolver and Custom Dictionary
A brand new set of tools designed to solve the hardest task in the microstock world: creating valid metadata for Getty Images / iStock.

*   **Interactive AI Mapping (Getty Resolver):** An advanced table that checks your keywords against the massive Getty Master Dictionary (>11,000 commercial terms). You can edit and split original and new words directly in-line.
*   **Intelligent Disambiguation (Assistant):** Cloud AI can study the context of your photo and automatically decide which meaning of a word to select (e.g., reliably distinguishing a 'crane' bird from a 'crane' machine).
*   **User Dictionary:** The system has a personal memory. Once you manually map a missing word or a custom name to an existing term from the Master database, the app remembers it for all future exports.

## Category Matrix and Bulk Management
No more manual sorting for each agency separately.

*   **Cross AI Mapping:** We created a Category Matrix. The AI model receives a list of "Master Categories" and assigns the best ones to the photo. These categories are then automatically translated into the correct ID formats for Shutterstock, Adobe Stock, Alamy, or Motion Elements during export or upload.
*   **Motion Elements (Video vs Photo):** The matrix intelligently distinguishes photo and video formats and sends them to the correct subcategories for ME.
*   **Bulk Adding from Grid:** A new Categories button in the batch edit bar opens a dialog for quick manual selection (up to 3 categories) for hundreds of selected photos at once. You can also define properties and editorial flags in bulk here.

## FTP Manager and One-Click Distribution with CSV
The entire stock photo upload process has been rewritten from the ground up to be fully independent and automated.

*   **Assign CSV Template to Server:** In the FTP upload window, you can now assign a specific CSV template format to each agency (server).
*   **One-Click Temp CSV:** When active, the app automatically takes the uploaded photos, generates a temporary CSV tailored to the specific agency, uploads the CSV file immediately after the photos, and then cleans it up from your computer.
*   **Advanced Server Settings (Threads):** The number of concurrent uploads (threads) is no longer global but set individually for each FTP server. You can safely send to Shutterstock with 10 photos at once, while limiting Zoonar to 1 thread to prevent blocks (421 Too many connections).
*   **Profiles and Badges:** You can create groups of servers (FTP Profiles). Uploaded agencies are then permanently visualized as colored micro-badges directly in the grid for each photo and can be actively filtered.

*** 
*(Other technical updates include a new full ZIP backup of all settings, limit color unification, 100% protection against AI error states, and the removal of UI freezing when bulk-selecting thousands of items).*




### [Get Started Now]

* [Download Latest Version](https://www.artushfoto.eu/Software/Download-ArtushVision-AI)
* [Purchase Lifetime License - $39.99](https://www.artushfoto.eu/Software/Purchase-ArtushVision-AI)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[❓ Frequently Asked Questions (FAQ)](faq.html)

---

*ArtushVision AI - Professional precision and complete metadata automation.*
