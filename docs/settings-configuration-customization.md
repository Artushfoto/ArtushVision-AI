---
title: "Settings and Configuration Guide | ArtushVision AI Documentation"
description: "Customize ArtushVision AI to your specific professional needs. Learn about workspace customization, CSV template editing, category matrix mapping, and geocoding settings."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
</style>
</div>

# Settings and Configuration

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**ArtushVision AI is designed to be highly adaptable. The Settings panel allows you to tailor the application interface, AI behavior, and distribution logic to match your specific professional photography or videography workflow.**

The configuration suite is divided into several specialized tabs, each focusing on a different aspect of the metadata and distribution process.

[IMAGE: A wide screenshot of the Settings window showing the navigation sidebar with tabs like Workspace, AI, CSV Editor, and Maps.]

---

## Workspace and UI Customization

A comfortable workspace is essential for long editing sessions. ArtushVision AI allows you to adjust the interface to suit your monitor size and visual preferences.

* **Thumbnail Management:** Adjust the height and quality of grid thumbnails. Smaller thumbnails allow for more assets on screen, while larger ones are better for visual verification.
* **Typography and Layout:** Customize global font sizes and the height of metadata fields. This is particularly useful for managing long descriptions or extensive keyword lists.
* **Theme and Visibility:** Toggle specific UI elements to reduce clutter and focus strictly on the metadata fields you use most frequently.

---

## AI and Video Tuning

Fine-tune how the AI engine interacts with your media, especially when dealing with complex video files.

* **Video Frame Logic:** Set the number of keyframes (3 to 20) the internal FFmpeg engine extracts for analysis. More frames provide more context but increase processing time.
* **Economy Mode (Collage) Configuration:** Enable or disable the automatic stitching of video frames into collages to optimize <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">Cloud AI</a> token usage and reduce costs.
* **Model Context Limits:** Define the VRAM limits for <a href="/docs/local-ai-model-manager-ollama.html">local Ollama models</a> to ensure the application remains stable based on your specific GPU hardware.

---

## Language, Spell Check, and Autocomplete

Ensure your metadata is flawless and quickly entered with advanced linguistic tools. ArtushVision AI provides comprehensive text assistance tailored to your workflow.

* **Dual-Language Spell Check:** Set both a primary and a secondary language (e.g., English and Spanish) to simultaneously detect typos across bilingual metadata without switching settings.
* **Smart Autocomplete:** Speed up manual data entry with predictive text. You can also enable online suggestions (via Google/Datamuse) to pull in contextually relevant words and corrections as you type.
* **Hover Translation:** Select a target language to instantly translate AI-generated or existing keywords simply by hovering your mouse over them.
* **Diacritics Control:** Choose whether the AI should output text with or without diacritics (accents), ensuring compatibility with stock agencies that have strict character formatting rules.

---

## Advanced CSV Template Editor

The CSV Editor is a powerful tool for reverse-engineering agency requirements or creating custom export formats for internal databases.

* **Template Mapping:** Load an existing CSV file from any agency, and the application will help you map its columns to ArtushVision AI fields (Title, Keywords, Categories, etc.).
* **Custom Headers:** Define specific header names required by niche stock agencies or private archives.
* **Export Presets:** Save your mappings as presets that can be instantly assigned to different FTP servers in the <a href="/docs/global-stock-distribution-ftp.html">Distribution module</a>.

[IMAGE: A close-up of the CSV Editor tab showing the column mapping interface and the Load Template button.]

---

## The Category Matrix

The [Category Matrix](#the-category-matrix) is the translation engine of ArtushVision AI. It ensures that your internal organization is correctly interpreted by different stock agencies.

* **ID Mapping:** Enter the specific numerical or text IDs used by agencies like Adobe Stock, Shutterstock, or Dreamstime for various categories.
* **Media Type Logic:** Apply different category rules for Photo and Video assets, ensuring each media type is funneled into the correct commercial bin.
* **Master Category Definition:** Create your own set of Master Categories that serve as the source for all agency-specific translations.

---

## Maps and Reverse Geocoding

Accurate location data is critical for editorial and travel photography. ArtushVision AI uses real-world map data to prevent AI hallucinations.

* **Map Provider Selection:** Choose between OpenStreetMap or ArcGIS as your primary visual mapping engine.
* **Reverse Geocoding Logic:** The application automatically translates GPS coordinates into readable City, State, and Country names. This text is then fed to the AI to provide geographical context for keyword generation.
* **Language Preferences:** Set the preferred language for location names to ensure consistency in your metadata.

[IMAGE: A screenshot of the Maps configuration tab showing the API provider selection and the geocoding toggle.]

---

## UI Color Customization and Theming

Personalize your workspace for maximum visual comfort during long editing sessions using the Advanced Color Palette Editor. You have full control over the visual feedback of the application in both Dark and Light modes.

* **Keyword Color Coding:** Assign custom colors to instantly distinguish between Original (loaded from file), AI-Generated, and Manually Edited keywords directly in the grid.
* **Interface Colors:** Freely adjust the colors of application backgrounds, input fields, buttons, and grid elements to reduce eye strain.
* **Validation Alerts:** Set specific error highlight colors that will instantly alert you whenever strict agency limits (such as maximum title length or keyword count) are exceeded.

---

## Complete System Backup and Migration

Protect your entire customized configuration or seamlessly migrate your workflow to a new workstation using the all-in-one Export Settings feature.

* **One-Click Export:** Instantly pack your custom AI profiles (prompts), CSV export templates, category matrices, and UI color preferences into a single, portable ZIP archive.
* **Vocabulary Preservation:** The backup safely includes your custom User Dictionary (`user_dict.txt`), ensuring your specialized microstock terminology and translated terms are never lost.
* **Seamless Restoration:** Use the Import Settings button on any computer to unpack your archive. The application will automatically restart and perfectly restore your fully customized environment in seconds.
* **Security in Mind:** Sensitive data such as your OpenRouter API key and local license activation are securely bundled, utilizing Windows DPAPI protection to keep your credentials safe during the transfer.

---

### Professional Workflow in 3 Steps:

1. **Define Your Workspace:** Adjust the UI and thumbnail sizes to match your hardware and visual comfort.
2. **Configure Translation Logic:** Set up your [CSV templates](#advanced-csv-template-editor) and [Category Matrix](#the-category-matrix) to automate agency-specific requirements.
3. **Calibrate AI and Maps:** Fine-tune frame extraction and geocoding to ensure the highest possible metadata accuracy.

---

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*