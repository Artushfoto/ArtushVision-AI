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
* **Economy Mode (Collage) Configuration:** Enable or disable the automatic stitching of video frames into collages to optimize Cloud AI token usage and reduce costs.
* **Model Context Limits:** Define the VRAM limits for [local Ollama models](local-ai-model-manager-ollama.md) to ensure the application remains stable based on your specific GPU hardware.

---

## Advanced CSV Template Editor
The CSV Editor is a powerful tool for reverse-engineering agency requirements or creating custom export formats for internal databases.

* **Template Mapping:** Load an existing CSV file from any agency, and the application will help you map its columns to ArtushVision AI fields (Title, Keywords, Categories, etc.).
* **Custom Headers:** Define specific header names required by niche stock agencies or private archives.
* **Export Presets:** Save your mappings as presets that can be instantly assigned to different FTP servers in the [Distribution module](global-stock-distribution-ftp.md).

[IMAGE: A close-up of the CSV Editor tab showing the column mapping interface and the Load Template button.]

---

## The Category Matrix
The Category Matrix is the translation engine of ArtushVision AI. It ensures that your internal organization is correctly interpreted by different stock agencies.

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

## Backup and Data Safety
Protect your work with automated redundancy settings.

* **Automatic Backups:** Enable the application to create safety copies of your XMP sidecars, CSV files, and even original JPGs during the saving process.
* **Version Control:** Maintain a history of your metadata changes to prevent accidental data loss during [batch operations](batch-operations-metadata-library-management.md).

---

### Professional Workflow in 3 Steps:
1. **Define Your Workspace:** Adjust the UI and thumbnail sizes to match your hardware and visual comfort.
2. **Configure Translation Logic:** Set up your CSV templates and Category Matrix to automate agency-specific requirements.
3. **Calibrate AI and Maps:** Fine-tune frame extraction and geocoding to ensure the highest possible metadata accuracy.

---

### [Get Started Now]
* [Download Free Lite Version](https://www.artushfoto.eu/Software/Download-ArtushVision-AI)
* [Purchase Lifetime License - $39.99](https://www.artushfoto.eu/Software/Purchase-ArtushVision-AI)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

---
*ArtushVision AI - Professional precision and complete configuration control.*
