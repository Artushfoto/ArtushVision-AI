---
title: "AI Metadata Generation: Cloud and Local Vision Models | ArtushVision AI"
description: "Professional AI photo and video tagging workstation. Features a 4-tier engine including Cloud (OpenRouter), Local (Ollama), Hybrid, and 2-Pass Local AI processing."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }

</style>
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
</style>
</div>

# AI Metadata Generation: Smart, Fast, and 100% Private

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Transform your photography workflow by replacing manual tagging with state-of-the-art Vision-Language Models (VLMs). ArtushVision AI "looks" at your media to instantly generate professional Titles, Descriptions, and Keywords.**

Unlike basic tools that rely on a single cloud API, ArtushVision AI offers an unprecedented level of control. Whether you require the speed of massive cloud batches or the absolute privacy of a local offline environment, the 4-Tier AI Engine adapts to your specific professional needs.

[IMAGE:  A wide screenshot showing the main image grid and the detailed AI Prompt Editor, highlighting the AI Engine Mode selection.]

---

## 4-Tier AI Engine: Choose Your Processing Path

ArtushVision AI gives you complete freedom over where and how your data is processed.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/4-tier-ai-engine.png" target="_blank" class="screenshot-link" style="max-width: 300px;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/4-tier-ai-engine.png" alt="ArtushVision AI - Versatile AI Workflow Selection" style="width: 300px;" class="screenshot-img">
</a>

### 1. Cloud AI

Best for maximum speed and complex commercial SEO. Connect your [OpenRouter API key](/docs/cloud-ai-openrouter-api-setup.html) to access elite models such as Google Gemini 2.0 Flash, Claude 3.5 Sonnet, or GPT-4o.

* **Multi-Threading:** Process up to 15 assets simultaneously for high-volume batches.
* **Transparent AI Pricing and Live Cost Tracking**
    ArtushVision AI connects to OpenRouter on a pay-as-you-go basis, meaning you only pay for the API calls you actually make. The cost per image is microscopic (often fractions of a cent), and the application provides comprehensive tools to keep your spending under absolute control.

* **Instant Batch Pricing:** As soon as an AI analysis batch is completed, the application instantly displays the exact cost of that specific run directly in the success notification.

**Cloud AI processing: gemini-2.0-flash-001**
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/cloud-ai-gemini-20-flash-001.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/cloud-ai-gemini-20-flash-001.png" alt="ArtushVision AI Interface" width="100%" class="screenshot-img">
</a>

* **Detailed Analytics Dashboard:** Access the dedicated OpenRouter Statistics window from the top menu to monitor your complete usage history, total spent, and remaining available credit.

Go to `Top Menu` → `File` → `Open Router Statistic` to view your stats.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/open-router-statistic.png" target="_blank" class="screenshot-link" style="max-width: 500px;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/open-router-statistic.png" alt="ArtushVision AI - Open Router Statistic" style="width: 500px;" class="screenshot-img">
</a>

* **Smart Estimations:** The software continuously calculates your average cost per processed photo and provides a live estimate of how many more assets you can analyze before needing to top up your balance.

### 2. Local AI

Best for 100% privacy, non-disclosure agreement (NDA) shoots, and zero API costs. The application integrates directly with your local [Ollama](/docs/ollama-installation-guide.html) installation (see our [Ollama Setup Guide](/docs/ollama-installation-guide.html) if you haven't installed it yet).

* **Total Privacy:** Photos never leave your local hardware; no internet connection is required.
* **Live VRAM Monitoring:** The status bar actively tracks GPU memory usage to ensure stability during local processing.

**Local AI Batch Processing (Ollama Model: gemma4:e4b)**
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-gemma4e4b.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-gemma4e4b.png" alt="ArtushVision AI Interface" width="100%" class="screenshot-img">
  </a>

**Local AI Detail Window:** Processing a single photo using an **AI hint for accurate Caiman Yacare** identification (Ollama Model: gemma4:e4b)
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-edit-window-processing.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/local-ai-edit-window-processing.png" alt="ArtushVision AI Interface" width="100%" class="screenshot-img">
  </a>

### 3. Hybrid AI

An intelligent agentic pipeline that combines privacy with high-end SEO formatting.
* **Local Analysis:** A local model extracts raw visual descriptions on your PC.
* **Cloud Synthesis:** Only the extracted text is sent to a fast cloud model to format it into professional, comma-separated keywords and titles.

**Using Hybrid AI in Detail Window:** Processing a single photo using **Local Vision** and **Cloud Text** for perfect formatting (Ollama Local AI Vision: qwen3-vl:4b + Cloud AI: google/gemini-2.0-flash-001)
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/hybrid-ai-qwen3-vl4b-and-gemini-20-flash-001.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ai-engines/hybrid-ai-qwen3-vl4b-and-gemini-20-flash-001.png" alt="ArtushVision AI Interface" width="100%" class="screenshot-img">
  </a>

### 4. Two-Step Local AI

Designed for high-quality offline results on consumer-grade GPUs (e.g., 8GB VRAM).

* **Resource Management:** The system loads a Vision model to describe the image, unloads it, and then loads a Text model for SEO formatting. This prevents hardware crashes while maintaining elite output quality.

**Local AI Detail Window: Processing a single photo using Local Vision and Local Text for perfect formatting (Ollama: gemma4:e2b + qwen2.5:7b)**

---

## Context-Aware Prompting: The AI Knows Your Gear

Generic AI tools produce generic metadata. ArtushVision AI injects technical background context into every prompt to ensure specific and accurate results.

* **Global AI Hint:** Input a specific fact—such as a Latin species name—into the [Global Hint](/docs/advanced-ai-prompting-profiles-variables.html#basic-and-contextual-variables) field. The AI treats this as an absolute fact and prioritizes it in the generated metadata.
* **Smart Geolocation:** GPS coordinates are translated via [OpenStreetMap or ArcGIS](/docs/settings-configuration-customization.html#maps-and-reverse-geocoding) into City and Country names, allowing the AI to include specific location context automatically.
* **Technical EXIF Injection:** The AI is informed of the camera model, lens settings, and exposure data (e.g., DJI Mavic 3, f/2.8, ISO 100). It uses this to add relevant tags like drone photography or shallow depth of field.
* **[Category Matrix](/docs/settings-configuration-customization.html#the-category-matrix) Integration:** The engine ensures generated keywords align with your selected commercial [Master Categories](/docs/settings-configuration-customization.html#the-category-matrix).

[IMAGE: A screenshot of the Profile Editor showing prompt variables like camera_model, gps_raw, and user_hint inserted into a system prompt.]

---

## Native Video Analysis and Economy Mode

ArtushVision AI provides native support for video assets (.mp4, .mov), eliminating the need for manual video tagging.

* **Smart Frame Extraction:** The built-in FFmpeg engine extracts between 3 and 20 keyframes from across the video timeline to capture the entire story.
* **Economy Mode (Collage):** To save on Cloud API costs, the application stitches extracted frames into a single high-quality collage. The AI analyzes the entire storyline in a single request, reducing token usage by up to 90%.

[IMAGE: A visual comparison of Economy Mode—a grid collage of video frames next to the resulting AI-generated keywords.]

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
