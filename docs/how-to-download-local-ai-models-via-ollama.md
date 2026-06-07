---
title: "How to Download Local AI Models via Ollama | ArtushVision AI"
description: "Step-by-step guide to downloading, managing, and organizing local AI Vision and Text models using Ollama in ArtushVision AI."
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

# How to Download Local AI Models via Ollama

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

To unlock the full potential of ArtushVision AI's **Enhanced Local AI** or **Hybrid AI** modes, you need to download the appropriate models to your computer. This guide will walk you through choosing, downloading, and organizing your local models directly through the internal Model Manager.

> ⚠️ **Important Prerequisite:** Before downloading any models, you must have Ollama installed and running in the background on your computer. If you haven't set it up yet, please follow our step-by-step [Ollama Installation & Setup Guide](/docs/ollama-installation-guide.html) first.
> 
> 💡 **Tip for Lite Version Users:** Running local models is a fantastic way to bypass cloud API constraints. To see how local models fit into your license tier, check out our [Free Trial Limits and Testing Guide](/docs/free-trial-limits-and-testing.html).

---

## 1. Find a Model on the Ollama Website

First, you need to select the specific model that matches your hardware and workflow needs.

* Open your web browser and navigate to the official [Ollama Library](https://ollama.com/search).
* Browse or search for models. Pay close attention to the model capabilities:
  * **Vision Models:** Required to analyze, describe, and tag images (e.g., `gemma4:e2b`, `qwen3-vl:4b`). These are critical for processing visual data and utilizing features like the [Absolute Priority AI Hint](/docs/advanced-ai-prompting-profiles-variables.html#basic-and-contextual-variables).
  * **Text Models:** Used for advanced metadata formatting, translations, and structuring tag taxonomies (e.g., `qwen2.5:7b`, `deepseek-r1:7b`).
* Once you find the desired model, copy its exact name including the parameter size tag (for example, copy `qwen3-vl:4b`, not just `qwen3-vl`).

**Finding a Model on the Ollama Website**
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ollama-models-search.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ollama-models-search.png" alt="Finding and copying the exact model name on the Ollama website library" class="screenshot-img">
</a>

**Copying the Exact Model Name**
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ollama-model-name-copy.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ollama-model-name-copy.png" alt="Copying the exact model name with size tags from the Ollama repository" class="screenshot-img">
</a>

---

## 2. Open the Internal Model Manager

* In ArtushVision AI, open the **Profile Editor**.
* Locate the **AI Model** input field and click the **Search Icon** next to it. This will open the internal AI Model Selection window.

---

## 3. Download the Model

* Look for the **Download New Model** section, located at the bottom of the Model Selection window.
* Paste the exact model name you copied from the Ollama website into the text field.
* Click the **Download** button.

**How to download Ollama Model**
<video src="video/ai-model-downloading.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Downloading Local AI Models" aria-label="Video guide showing how to download a local AI model through the internal Model Manager">
  ArtushVision AI - Demonstration of downloading a local AI model.
</video>
<p><a href="video/ai-model-downloading.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## 4. Monitor the Download Progress

* The application will connect to your local Ollama instance and initiate the download process.
* You will see a live download progress indicator displaying the transferred data in MB or GB alongside the download speed.
* Wait until the download is fully complete. Once finished, a success message will appear, and the model will automatically populate in your list of available models.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-model-model-downloading.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-model-model-downloading.png" alt="ArtushVision AI - Local model download interface showing live speed and progress" width="100%" class="screenshot-img">
</a>

---

## 5. Auto-Detection, Manual Override & Custom Notes

Once a model is successfully downloaded, the Model Manager automatically categorizes and organizes it for you:

### Auto-Detection & Manual Override
The manager automatically scans your downloaded models and categorizes them as **Text, Image** (models that can "see" images) or **Text** (language-only models), color-coding them in the grid for easy identification. If the system fails to recognize the model type automatically, you can verify the correct type on the official [Ollama website](https://ollama.com/search) and easily right-click the model in the list to configure its type **manually**.

### Adding Custom Notes
To keep your local AI environment organized, you can assign personal performance notes to any model:
* Locate your newly downloaded model in the manager's table.
* Double-click the cell in the **Note** column for that specific model.
* Type your custom description to document its real-world performance (e.g., *"Great for animal species and fine details"* or *"Fast text formatter, struggles with complex JSON"*).
* Press **Enter** or click away to save it. This helps you remember which specific subjects or tasks each model handles well and which it doesn't.

**Model Manager Grid & Custom Notes**
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-model-management.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-model-management.png" alt="ArtushVision AI - Local AI model manager grid with custom performance notes column" width="100%" class="screenshot-img">
</a>

---

## Next Steps & Related Documentation
* **Advanced Prompting:** Now that your models are ready, learn how to maximize their accuracy using [Advanced AI Prompting & Profiles](/docs/advanced-ai-prompting-profiles-variables.html).
* **Getty Integration:** Learn how to combine local AI text models with our [Automated Getty Mapping](/docs/advanced-ai-prompting-profiles-variables.html) to instantly match official agency taxonomies.

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