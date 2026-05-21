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

**Running AI locally using <a href="/docs/ollama-installation-guide.html">Ollama</a> is the ultimate solution for professional stock contributors. It offers 100% privacy for sensitive shoots (like boudoir or unreleased commercial products) and zero API costs.**

However, managing models via a command-line terminal can be intimidating. ArtushVision AI solves this with a fully integrated, desktop-class **Local Model Manager**. It gives you a visual dashboard to browse, download, organize, and monitor your <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">local AI</a> models without ever touching the command line.

[IMAGE: A wide screenshot of the Local AI Models (Ollama) window, showing the table with Model ID, Size, Parameters, Quantization, Type, and the editable Notes column.]

---

## Integrated Hub Browser and Downloader

Skip the terminal. ArtushVision AI connects directly to your local <a href="/docs/ollama-installation-guide.html">Ollama</a> installation and the global Ollama Hub. For a complete walkthrough of this process, you can follow our detailed <a href="/docs/how-to-download-local-ai-models-via-ollama.html">Model Download Guide</a>.

* **Curated Recommendations:** Not sure where to start? Open the **Recommended** browser to see a curated list of the best Vision and Text models currently available for stock photography (like **Qwen2.5-VL** or **Llama 3.2**), complete with descriptions of their specific strengths.
* **Direct Downloads:** Type any Model ID (e.g., `moondream:latest`) and hit Download. Watch the real-time progress bar with human-readable data (MB/GB) directly in the UI.

[IMAGE: A screenshot of the Ollama Hub Browser showing the download progress dialog, transfer rates, and the curated list of recommended models.]

**Integrated Ollama Hub Browser and Downloader**
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/local-model-model-downloading.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/local-model-model-downloading.png" alt="ArtushVision AI Interface" width="100%" class="screenshot-img">
</a>

---

## Smart Vision and Text Detection

ArtushVision's advanced <a href="/docs/ai-metadata-generation-cloud-local-ollama.html">Agentic Workflows</a> require knowing exactly what a model is capable of.

* **Auto-Detection:** The manager automatically scans your downloaded models and categorizes them as **Vision** (models that can "see" images) or **Text** (language-only models), color-coding them in the grid for easy identification.
* **Manual Override:** If you are testing a brand-new or experimental model that the application doesn't recognize yet, simply right-click the model and use the context menu to manually toggle its type.

---

## Deep Technical Insights

Understand exactly what is running on your machine and how it impacts your hardware performance.

* **Hardware Specs at a Glance:** The grid displays crucial technical data for every model, including its physical **Size (GB)**, total **Parameters** (e.g., 3B, 8B, 72B), and **Quantization** level (e.g., Q4_0, Q8_0).


> **What do Parameters and Quantization mean in local AI?**
> These two settings directly determine how "smart" your local AI model is and how much graphics card memory (VRAM) it requires. 
* **Parameters (e.g., 3B, 8B)** represent the size of the AI’s "brain" in billions - a higher number means better recognition of complex details but demands stronger hardware. 
* **Quantization (e.g., Q4_0, Q8_0)** is the compression level of that brain. Choosing a **Q4_0** or **Q4_K_M** version is the ultimate sweet spot: it shrinks the model size by roughly 70% for blazing-fast performance while retaining about 95% of its original accuracy, allowing it to run smoothly even on standard 8GB graphics cards (like an RTX 3060 Ti). If you have a powerful card with 12GB+ of VRAM and want absolute maximum precision, you can opt for the uncompressed **Q8_0** version.

* **Live VRAM Monitor:** Located in the main application status bar, a live hardware monitor tracks your GPU VRAM usage. If a model exceeds your graphics card's memory, the application intelligently falls back to CPU RAM and provides a warning.

[IMAGE: A close-up of the main application bottom status bar, highlighting the Ollama VRAM: 4.2 GB / 8.0 GB indicator.]

---

## Personal Notes and Organization

When testing multiple models, it is essential to track which one performed best for specific tasks.

* **Custom Notes:** Double-click the **Note** column next to any model to open a pop-up text editor. Record your findings (e.g., "Excellent for OCR" or "Fast but generic descriptions").
* **Smart Search:** The real-time search bar at the top of the manager searches through both model names and your custom notes, helping you find the perfect model for the job instantly.
* **Clean Uninstallation:** Free up disk space by deleting outdated models with a single click using the trash can icon.

---

## How to use Local Models in 3 Steps:

1. **Browse and Download:** Open the Model Manager, click **Recommended**, and download a small Vision model like `gemma4:e2b`. For step-by-step assistance, see our [Model Download Guide](/docs/how-to-download-local-ai-models-via-ollama.html).
2. **Assign to Profile:** Open the <a href="/docs/advanced-ai-prompting-profiles-variables.html">AI Profile Editor</a> and assign your newly downloaded model to a Local or Hybrid workflow.
3. **Run Offline:** Disconnect from the internet and watch the AI seamlessly tag your photos in total privacy.

---

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[📖 Step-by-Step Ollama Model Download Guide](/docs/how-to-download-local-ai-models-via-ollama.html)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*