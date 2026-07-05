---
title: "Local AI Model Manager: Complete Offline Control | ArtushVision AI"
description: "Manage local Ollama AI models with our visual dashboard. Browse, download, and monitor Vision/Text models for secure, offline AI metadata tagging."
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

# Local AI Model Manager: Visual Dashboard for Ollama

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Running AI locally using <a href="/docs/ollama-installation-guide.html">Ollama</a> is the ultimate solution for professional stock photography contributors.** It offers 100% privacy for sensitive shoots and zero API costs.

However, managing AI models via a command-line terminal can be difficult. ArtushVision AI simplifies this with an integrated, desktop-class **Local AI Model Manager**. It provides a visual dashboard to browse, download, organize, and monitor your <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">local AI models</a> without terminal commands.

---

## Integrated Model Browser and Downloader

Skip the terminal. ArtushVision AI connects directly to your local <a href="/docs/ollama-installation-guide.html">Ollama</a> installation. For a complete guide, view our <a href="/docs/how-to-download-local-ai-models-via-ollama.html">Model Download Tutorial</a>.

* **Curated AI Models:** Browse our recommended list of high-performance Vision and Text models optimized for stock photography (e.g., **gemma4:e4b**, **llama3.2:3b**).
* **One-Click Downloads:** Enter any Ollama Model ID to trigger a download with a real-time progress monitor for data usage (MB/GB).

**Video: How to Download Local AI Models**

<video src="video/ai-model-downloading.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Local AI Model Management">
  ArtushVision AI - Visual model downloading demonstration.
</video>
<p><a href="video/ai-model-downloading.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## Smart AI Vision and Text Detection

ArtushVision's <a href="/docs/ai-metadata-generation-cloud-local-ollama.html">Agentic Workflows</a> optimize your metadata generation based on model capabilities.

* **Auto-Categorization:** The manager scans and labels models as **Vision** (image analysis) or **Text** (language processing) for better workflow integration.
* **Manual Control:** Easily toggle model types via the context menu for experimental or custom AI models.

---

## Technical Insights: Parameters, Quantization, and VRAM

[**Learn more about the gemma models family**: https://ollama.com/library/gemma4](https://ollama.com/library/gemma4)

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/gemma-models.webp" target="_blank" class="screenshot-link" style="max-width: 800px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/gemma-models.webp" alt="ArtushVision AI - Ollama Gemma Models Dashboard" style="width: 800px;" class="screenshot-img">
</a>

Optimize your hardware performance by understanding your AI engine:

* **Hardware Metrics:** Track model size, parameter count (e.g., 3B, 8B), and quantization levels directly in the grid.
* **Quantization Guide:** Understand how **Q4_0** (optimized) vs. **Q8_0** (high precision) affects your VRAM usage. Our dashboard helps you choose the best model for your GPU capacity.
* **Live VRAM Monitoring:** Monitor your GPU memory usage in real-time. The application prevents crashes by offering intelligent fallbacks if a model exceeds available VRAM.

---

## Efficient Model Organization

* **Custom Notes:** Keep track of model performance by adding custom notes for specific tagging tasks.
* **Smart Search:** Use the real-time search bar to filter through model names and your saved notes.
* **Disk Management:** Quickly free up space by deleting unused local models.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-model-management.webp" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-model-management.webp" alt="ArtushVision AI - Manage Local AI Models" width="100%" class="screenshot-img">
</a>

---

## How to Get Started with Local AI Models

1. **Browse:** Open the Model Manager and check our **Recommended** list of lightweight Vision models like `gemma4:e2b`.
2. **Configure:** Assign your downloaded model to an AI Profile in the <a href="/docs/advanced-ai-prompting-profiles-variables.html">Profile Editor</a>.
3. **Execute:** Run your AI workflows entirely offline with complete data privacy.

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