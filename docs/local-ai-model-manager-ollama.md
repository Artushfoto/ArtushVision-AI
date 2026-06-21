---
title: "Local AI Model Manager: Complete Offline Control | ArtushVision AI"
description: "Manage your local Ollama AI models with a visual dashboard. Browse, download, and monitor Vision and Text models for professional offline metadata tagging."
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

# Local AI Model Manager: Complete Offline Control

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Running AI locally using <a href="/docs/ollama-installation-guide.html">Ollama</a> is the ultimate solution for professional stock contributors. It offers 100% privacy for sensitive shoots (like boudoir or unreleased commercial products) and zero API costs.**

However, managing models via a command-line terminal can be intimidating. ArtushVision AI solves this with a fully integrated, desktop-class **Local Model Manager**. It gives you a visual dashboard to browse, download, organize, and monitor your <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">local AI</a> models without ever touching the command line.

---

## Integrated Hub Browser and Downloader

Skip the terminal. ArtushVision AI connects directly to your local <a href="/docs/ollama-installation-guide.html">Ollama</a> installation and the global Ollama Hub. For a complete walkthrough of this process, you can follow our detailed <a href="/docs/how-to-download-local-ai-models-via-ollama.html">Model Download Guide</a>.

* **Curated Recommendations:** Not sure where to start? Open the **Recommended** browser to see a curated list of the best Vision and Text models currently available for stock photography (like **gemma4:e4b** or **llama3.2:3b**), complete with descriptions of their specific strengths.
* **Direct Downloads:** Type any Model ID (e.g., `moondream:18b` or `gemma4:e4b`) and hit Download. Watch the real-time progress bar with human-readable data (MB/GB) directly in the UI.

**Downloading Local AI Models via Model Manager**

<video src="video/ai-model-downloading.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Downloading Local AI Models via Model Manager">
  ArtushVision AI - Visual model downloading demonstration.
</video>
<p><a href="video/ai-model-downloading.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## Smart Vision and Text Detection

ArtushVision's advanced <a href="/docs/ai-metadata-generation-cloud-local-ollama.html">Agentic Workflows</a> require knowing exactly what a model is capable of.

* **Auto-Detection:** The manager automatically scans your downloaded models and categorizes them as **Vision** (models that can "see" images) or **Text** (language-only models), color-coding them in the grid for easy identification.
* **Manual Override:** If you are testing a brand-new or experimental model that the application doesn't recognize yet, simply right-click the model and use the context menu to manually toggle its type.

---

## Deep Technical Insights

[**gemma models family**: https://ollama.com/library/gemma4](https://ollama.com/library/gemma4)

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/gemma-models.png" target="_blank" class="screenshot-link" style="max-width: 800px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/gemma-models.png" alt="ArtushVision AI - Ollama Gemma Models" style="width: 800px;" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

Understand exactly what is running on your machine and how it impacts your hardware performance.

* **Hardware Specs at a Glance:** The grid displays crucial technical data for every model, including its physical **Size (GB)**, total **Parameters** (e.g., 3B, 8B, 72B), and **Quantization** level (e.g., Q4_0, Q8_0).

> **What do Parameters and Quantization mean in local AI?**
> These two settings directly determine how "smart" your local AI model is and how much graphics card memory (VRAM) it requires. 
* **Parameters (e.g., 3B, 8B)** represent the size of the AI’s "brain" in billions - a higher number means better recognition of complex details but demands stronger hardware. 
* **Quantization (e.g., Q4_0, Q8_0)** is the compression level of that brain. Choosing a **Q4_0** or **Q4_K_M** version is the ultimate sweet spot: it shrinks the model size by roughly 70% for blazing-fast performance while retaining about 95% of its original accuracy, allowing it to run smoothly even on standard 8GB graphics cards (like an RTX 3060 Ti). If you have a powerful card with 12GB+ of VRAM and want absolute maximum precision, you can opt for the uncompressed **Q8_0** version.

* **Live VRAM Monitor:** Located in the main application status bar, a live hardware monitor tracks your GPU VRAM usage. If a model exceeds your graphics card's memory, the application intelligently falls back to CPU RAM and provides a warning.

---

## Personal Notes and Organization

When testing multiple models, it is essential to track which one performed best for specific tasks.

* **Custom Notes:** Double-click the **Note** column next to any model to open a pop-up text editor. Record your findings (e.g., "Excellent for OCR" or "Fast but generic descriptions").
* **Smart Search:** The real-time search bar at the top of the manager searches through both model names and your custom notes, helping you find the perfect model for the job instantly.
* **Clean Uninstallation:** Free up disk space by deleting outdated models with a single click using the trash can icon.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-model-management.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-model-management.png" alt="ArtushVision AI - Local AI model manager grid with personal performance notes" width="100%" class="screenshot-img">
</a>

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

[⭐ User Reviews & Testimonials](/docs/artushvision-reviews.html)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*