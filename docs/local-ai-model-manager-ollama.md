---
title: "Local AI Model Manager: Complete Offline Control | ArtushVision AI"
description: "Manage your local Ollama AI models with a visual dashboard. Browse, download, and monitor Vision and Text models for professional offline metadata tagging."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
table { width: 100%; margin-bottom: 20px; border-collapse: collapse; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
</style>
</div>

# Local AI Model Manager: Complete Offline Control

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Running AI locally using [Ollama](ollama-installation-guide.md) is the ultimate solution for professional stock contributors. It offers 100% privacy for sensitive shoots (like boudoir or unreleased commercial products) and zero API costs.**

However, managing models via a command-line terminal can be intimidating. ArtushVision AI solves this with a fully integrated, desktop-class **[Local Model Manager](local-ai-model-manager-ollama.md)**. It gives you a visual dashboard to browse, download, organize, and monitor your [local AI](ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path) models without ever touching the command line.

[IMAGE: A wide screenshot of the [Local AI](ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path) Models ([Ollama](ollama-installation-guide.md)) window, showing the table with Model ID, Size, Parameters, Quantization, Type, and the editable Notes column.]

---

## Integrated Hub Browser and Downloader
Skip the terminal. ArtushVision AI connects directly to your local [Ollama](ollama-installation-guide.md) installation and the global [Ollama](ollama-installation-guide.md) Hub.

* **Curated Recommendations:** Not sure where to start? Open the **Recommended** browser to see a curated list of the best Vision and Text models currently available for stock photography (like **Qwen2.5-VL** or **Llama 3.2**), complete with descriptions of their specific strengths.
* **Direct Downloads:** Type any Model ID (e.g., `moondream:latest`) and hit Download. Watch the real-time progress bar with human-readable data (MB/GB) directly in the UI.

[IMAGE: A screenshot of the [Ollama](ollama-installation-guide.md) Hub Browser showing the download progress dialog, transfer rates, and the curated list of recommended models.]

---

## Smart Vision and Text Detection
ArtushVision's advanced Agentic Workflows require knowing exactly what a model is capable of.

* **Auto-Detection:** The manager automatically scans your downloaded models and categorizes them as **Vision** (models that can "see" images) or **Text** (language-only models), color-coding them in the grid for easy identification.
* **Manual Override:** If you are testing a brand-new or experimental model that the application doesn't recognize yet, simply right-click the model and use the context menu to manually toggle its type.

---

## Deep Technical Insights
Understand exactly what is running on your machine and how it impacts your hardware performance.

* **Hardware Specs at a Glance:** The grid displays crucial technical data for every model, including its physical **Size (GB)**, total **Parameters** (e.g., 3B, 8B, 72B), and **Quantization** level (e.g., Q4_0, Q8_0).
* **Live VRAM Monitor:** Located in the main application status bar, a live hardware monitor tracks your GPU VRAM usage. If a model exceeds your graphics card's memory, the application intelligently falls back to CPU RAM and provides a warning.

[IMAGE: A close-up of the main application bottom status bar, highlighting the [Ollama](ollama-installation-guide.md) VRAM: 4.2 GB / 8.0 GB indicator.]

---

## Personal Notes and Organization
When testing multiple models, it is essential to track which one performed best for specific tasks.

* **Custom Notes:** Double-click the **Note** column next to any model to open a pop-up text editor. Record your findings (e.g., "Excellent for OCR" or "Fast but generic descriptions").
* **Smart Search:** The real-time search bar at the top of the manager searches through both model names and your custom notes, helping you find the perfect model for the job instantly.
* **Clean Uninstallation:** Free up disk space by deleting outdated models with a single click using the trash can icon.

---

## How to use Local Models in 3 Steps:

1. **Browse and Download:** Open the Model Manager, click **Recommended**, and download a small Vision model like `qwen2.5-vl:3b`.
2. **Assign to Profile:** Open the AI Profile Editor and assign your newly downloaded model to a Local or Hybrid workflow.
3. **Run Offline:** Disconnect from the internet and watch the AI seamlessly tag your photos in total privacy.

---

### [Get Started Now]
* [Download Fully Functional Lite Version](https://www.artushfoto.eu/Software/Download-ArtushVision-AI)
* [Purchase Lifetime License - $39.99](https://www.artushfoto.eu/Software/Purchase-ArtushVision-AI)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

---
*ArtushVision AI - Professional precision and complete offline AI control.*
