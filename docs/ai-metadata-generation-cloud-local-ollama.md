<!-- --- artushvision-engine-doc --- -->
---
title: "AI Metadata Generation: Cloud and Local Vision Models | ArtushVision AI"
description: "Professional AI photo and video tagging workstation. Features a 4-tier engine including Cloud (OpenRouter), Local (Ollama), Hybrid, and 2-Pass Local AI processing."
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

# AI Metadata Generation: Smart, Fast, and 100% Private

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Transform your photography workflow by replacing manual tagging with state-of-the-art Vision-Language Models (VLMs). ArtushVision AI "looks" at your media to instantly generate professional Titles, Descriptions, and Keywords.**

Unlike basic tools that rely on a single cloud API, ArtushVision AI offers an unprecedented level of control. Whether you require the speed of massive cloud batches or the absolute privacy of a local offline environment, the 4-Tier AI Engine adapts to your specific professional needs.

---

## 4-Tier AI Engine: Choose Your Processing Path

ArtushVision AI gives you complete freedom over where and how your data is processed.

Go to `Top Menu` → `File` → `Settings` → `Language and AI`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/language-and-ai.png" target="_blank" class="screenshot-link" style="max-width: 400px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/language-and-ai.png" alt="ArtushVision AI - Versatile AI - Language and AI Settings" style="width: 400px;" class="screenshot-img">
</a>

---
 
**Select AI Engine (Processing)**
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/4-tier-ai-engine.png" target="_blank" class="screenshot-link" style="max-width: 300px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/4-tier-ai-engine.png" alt="ArtushVision AI - Versatile AI Workflow Selection" style="width: 300px;" class="screenshot-img">
</a>

### 1. Cloud AI

Best for maximum speed and complex commercial SEO. Connect your [OpenRouter API key](/docs/cloud-ai-openrouter-api-setup.html) to access elite models such as `gemini-2.5-flash-lite`, `Claude 3.5 Sonnet`, or `GPT-4o`.

---

> **⚠️ IMPORTANT: Dynamic AI Model Deprecations & API Updates**
> Cloud AI models are constantly evolving. Third-party providers and API aggregators (such as OpenRouter) frequently update, replace, or deprecate older model endpoints to ensure optimal performance, security, and cost-efficiency. When an older AI model is officially retired, any saved AI Prompt Profile still pointing to that specific deprecated endpoint will fail and return an API connection error.
>
> **Action Required:** If your cloud AI processing suddenly stops working or throws an unexpected API error, the selected model has likely been deprecated. Open the **AI Profile Editor** (or check your global AI settings), select a current, active model from the dropdown list, and save your updated profile to restore immediate functionality.

---

* **Multi-Threading:** Process up to 15 assets simultaneously for high-volume batches.
* **Transparent AI Pricing and Live Cost Tracking**
    ArtushVision AI connects to OpenRouter on a pay-as-you-go basis, meaning you only pay for the API calls you actually make. The cost per image is microscopic (often fractions of a cent), and the application provides comprehensive tools to keep your spending under absolute control.

* **Instant Batch Pricing:** As soon as an AI analysis batch is completed, the application instantly displays the exact cost of that specific run directly in the success notification.

**Cloud AI processing:** `gemini-2.0-flash-001`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/cloud-ai-gemini-20-flash-001.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/cloud-ai-gemini-20-flash-001.png" alt="ArtushVision AI - Cloud AI processing with Gemini 2.0 Flash" width="100%" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

* **Detailed Analytics Dashboard:** Access the dedicated OpenRouter Statistics window from the top menu to monitor your complete usage history, total spent, and remaining available credit.

Go to `Top Menu` → `File` → `Open Router Statistic` to view your stats.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/open-router-statistic.png" target="_blank" class="screenshot-link" style="max-width: 500px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/open-router-statistic.png" alt="ArtushVision AI - Open Router Statistic" style="width: 500px;" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

* **Smart Estimations:** The software continuously calculates your average cost per processed photo and provides a live estimate of how many more assets you can analyze before needing to top up your balance.

---

### 2. Local AI

Best for 100% privacy, non-disclosure agreement (NDA) shoots, and zero API costs. The application integrates directly with your local [Ollama](/docs/ollama-installation-guide.html) installation (see our [Ollama Setup Guide](/docs/ollama-installation-guide.html) if you haven't installed it yet).

* **Total Privacy:** Photos never leave your local hardware; no internet connection is required.
* **Live VRAM Monitoring:** The status bar actively tracks GPU memory usage to ensure stability during local processing.

**Local AI Batch Processing** (Ollama Model: `gemma4:e4b`)

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-gemma4e4b.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-gemma4e4b.png" alt="ArtushVision AI - Local AI Batch Processing" width="100%" class="screenshot-img">
  </a>
<div style="height: 15px;"></div>

**Local AI Detail Window:** Processing a single photo using an **AI hint for accurate Yacare Caiman** identification (Ollama Model: `gemma4:e4b`)

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-gemma4e4b-edit-window-processing-hint.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-gemma4e4b-edit-window-processing-hint.png" alt="ArtushVision AI - Local AI Detail Window" width="100%" class="screenshot-img">
  </a>

### 3. Hybrid AI

An intelligent agentic pipeline that combines privacy with high-end SEO formatting.
* **Local Analysis:** A local model extracts raw visual descriptions on your PC.
* **Cloud Synthesis:** Only the extracted text is sent to a fast cloud model to format it into professional, comma-separated keywords and titles.

**Using Hybrid AI in Detail Window:** Processing a single photo using **Local Vision** and **Cloud Text** for perfect formatting (Ollama Local AI Vision: `qwen3-vl:4b` + Cloud AI: `gemini-2.0-flash-001`)

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/hybrid-ai-qwen3-vl4b-and-gemini-20-flash-001.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/hybrid-ai-qwen3-vl4b-and-gemini-20-flash-001.png" alt="ArtushVision AI - Using Hybrid AI in Detail Window" width="100%" class="screenshot-img">
  </a>

### 4. Two-Step Local AI

Designed for high-quality offline results on consumer-grade GPUs (e.g., 8GB VRAM).

* **Resource Management:** The system loads a Vision model to describe the image, unloads it, and then loads a Text model for SEO formatting. This prevents hardware crashes while maintaining elite output quality.

**Two Step Local AI Detail Window:** Processing a single photo using **Local Vision** and **Local Text** for perfect formatting (Ollama local AI Vision: `qwen3-vl:4b` + Ollama Local AI text: `aispin/qwen2.5-7b-instruct-abliterated-v2.q4_k_s.gguf`)

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/2pass-ai-qwen3-vl4b-qwen25-7b-instruct.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/2pass-ai-qwen3-vl4b-qwen25-7b-instruct.png" alt="ArtushVision AI - Two Step Local AI Detail Window" width="100%" class="screenshot-img">
  </a>

---

### How to change the AI Model (Cloud & Local)?

Changing your AI model gives you ultimate flexibility—allowing you to balance speed, cost, and privacy. You can use fast, free Local AI models for bulk processing and switch to advanced Cloud models for complex tasks.

Here is how to access and change the model via your AI Profile:

1. In the main top toolbar, click the **⚙ Profile Editor** button to open your active AI Profile.
2. Locate the **AI Model** input field in the editor window.
3. Click the **Magnifying Glass icon (🔍)** right next to the input field.
4. This will open the **Integrated Model Manager**, where you can easily:
   * Browse the catalog of **Cloud AI** models from OpenRouter (including their prices and specifications).
   * Browse, manage, and download **Local AI** models directly from the Ollama Hub.
5. Once you select a model from the list, the field will automatically update with the correct ID. Click **Save** (or *Save as...* to create a new profile) to apply the changes.

*💡 Tip for Getty Images workflow: You can also change your custom Cloud AI model on the fly directly inside the **Interactive Getty Resolver** window. Just use the model dropdown menu located in its top toolbar.*

Go to `Top Toolbar` → `Gear button ` next to the profile selector → `Magnifying Glass icon `

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/change-ai-model.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/change-ai-model.png" alt="ArtushVision AI - How to Change AI Model" width="100%" class="screenshot-img">
  </a>

---

## Context-Aware Prompting: The AI Knows Your Gear

Generic AI tools produce generic metadata. ArtushVision AI injects technical background context into every prompt to ensure specific and accurate results.

* **[Global AI Hint:](/docs/advanced-ai-prompting-profiles-variables.html#basic-and-contextual-variables)** Input a specific fact—such as a Latin species name—into the [Global Hint field.](/docs/advanced-ai-prompting-profiles-variables.html#basic-and-contextual-variables) The AI treats this as an absolute fact and prioritizes it in the generated metadata.
* **[Smart Geolocation:](/docs/settings-configuration-customization.html#maps-and-reverse-geocoding)** GPS coordinates are translated via [OpenStreetMap or ArcGIS](/docs/settings-configuration-customization.html#maps-and-reverse-geocoding) into City and Country names, allowing the AI to include specific location context automatically.
* **[Technical EXIF Injection:](/docs/advanced-ai-prompting-profiles-variables.html#technical--exif-parameters)** The AI is informed of the camera model, lens settings, and exposure data (e.g., DJI Mavic 3, f/2.8, ISO 100). It uses this to add relevant tags like drone photography or shallow depth of field.
* **[Category Matrix Integration:](/docs/settings-configuration-customization.html#the-category-matrix)** The engine ensures generated keywords align with your selected commercial [Master Categories](/docs/settings-configuration-customization.html#the-category-matrix).

**Prompt Editor**

Go to `Top Toolbar` → `Gear button ` next to the profile selector

  <a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/prompt-editor-gear.png" target="_blank" class="screenshot-link" style="max-width: 600px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/prompt-editor-gear.png" alt="ArtushVision AI - Prompt Editor" style="width: 600px;" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

**Cloud AI Prompt Editor**
  <a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/cloud-ai-profile-editor.png" target="_blank" class="screenshot-link" style="max-width: 600px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/cloud-ai-profile-editor.png" alt="ArtushVision AI - Cloud AI Profile Editor Setup" style="width: 600px;" class="screenshot-img">
</a>


**Hybrid AI Prompt Editor**
  <a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/hybrid-ai-profile-editor.png" target="_blank" class="screenshot-link" style="max-width: 600px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/hybrid-ai-profile-editor.png" alt="ArtushVision AI - Hybrid AI Profile Editor Setup" style="width: 600px;" class="screenshot-img">
</a>

---

## Native Video Analysis and Economy Mode

ArtushVision AI provides native support for video assets (.mp4, .mov), eliminating the need for manual video tagging.

* **Smart Frame Extraction:** The built-in FFmpeg engine extracts between 3 and 20 keyframes from across the video timeline to capture the entire story.
* **Economy Mode (Collage):** To save on Cloud API costs, the application stitches extracted frames into a single high-quality collage. The AI analyzes the entire storyline in a single request, reducing token usage by up to 90%.

Go to `Top Menu` → `File` → `Settings` → `Video and RAW`

  <a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/video-analysis-economy-mode.png" target="_blank" class="screenshot-link" style="max-width: 400px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/video-analysis-economy-mode.png" alt="ArtushVision AI - Video Analysis Modes" style="width: 400px;" class="screenshot-img">
</a>

---

## Smart Data Safeguards

The application is built with a safety-first philosophy to protect your existing work.

* **Original Word Preservation:** If you have already added custom titles or keywords, the AI will intelligently append its findings without overwriting your manual data.
* **Hallucination Guard:** A robust regex engine validates AI responses. If a model fails to return a valid structure, the app rescues and formats the data safely.
* **Diacritics Control:** Toggle accents on or off based on your target market, ensuring compatibility with strict international stock agency databases.

---

## How the Agentic AI Workflow Operates:

1. **Select Media:** Highlight photos and videos in your project grid.
2. **Apply Context:** Use the Global Hint for specific session details or client names.
3. **Execute:** Run the AI analysis using your preferred Local or Cloud engine.
4. **Review and Save:** Watch the real-time progress as the application merges commercial metadata directly into your assets.

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
<!-- --- artushvision-engine-doc --- -->