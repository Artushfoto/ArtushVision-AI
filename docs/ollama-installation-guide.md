---
title: "Ollama Installation & Setup Guide | ArtushVision AI"
description: "Step-by-step instructions for installing Ollama to run local AI Vision and Text models completely offline with ArtushVision AI."
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

# Ollama Installation & Setup Guide

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**To use the 100% private [Local AI](/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path) or [Hybrid AI](/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path) workflows in ArtushVision AI, you need to install Ollama. Ollama is a lightweight, secure background service that allows you to run powerful AI models directly on your hardware without sending any data to the cloud.**

Follow this simple guide to get Ollama running on your Windows machine in under 3 minutes.

---

## Step 1: Download Ollama

1. Open your web browser and go to the official Ollama website: **[https://ollama.com/download](https://ollama.com/download)**
2. Click the **Download for Windows** button.
3. Wait for the `OllamaSetup.exe` file to finish downloading.

---

## Step 2: Install the Application

1. Locate the downloaded `OllamaSetup.exe` in your Downloads folder and double-click to run it.
2. Click **Install** in the setup window. No complex configuration is required—the installer handles everything automatically.
3. Once the installation is complete, Ollama will automatically start running in the background.

<!-- [IMAGE: A screenshot of the Windows system tray showing the small Ollama alpaca icon running in the background.] -->

---

## Step 3: Verify It's Running

To ensure Ollama is working correctly and ready to connect with ArtushVision AI:

1. Check your **Windows System Tray** (the bottom-right corner of your screen near the clock). You should see the Ollama icon.
2. Open your web browser and type `http://localhost:11434` into the address bar.
3. If you see a simple blank page with the text **"Ollama is running"**, the installation was successful!

---

## Step 4: Connect with ArtushVision AI

You do not need to use the command line (Terminal) to download models. ArtushVision AI handles everything for you visually. For a complete step-by-step walkthrough on how to choose and fetch models, please refer to our dedicated [Model Download Guide](/docs/how-to-download-local-ai-models-via-ollama.html).

1. Open **ArtushVision AI**.
2. Navigate to **AI Mode Selection** and choose **[Local AI (Ollama)](/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path)** or **[Hybrid AI](/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path)**.
3. Click on the **[Local Model Manager](/docs/local-ai-model-manager-ollama.html)** icon in the interface.
4. From the built-in **Hub Browser**, you can now [browse, download, and manage models](/docs/how-to-download-local-ai-models-via-ollama.html) (like `gemma4:e4b` for Text/Vision tasks) with a single click.

---

## Troubleshooting

* **"Ollama not found" error in ArtushVision AI:** This means the background service is stopped. Search for "Ollama" in your Windows Start Menu and launch it. Wait a few seconds for the icon to appear in your system tray, then try again.
* **Slow Performance:** Local AI relies heavily on your computer's RAM and GPU (VRAM). For the best experience, close heavy applications (like modern games or heavy video renders) while running offline AI batches.

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

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-9CH7W6CRCH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-9CH7W6CRCH');
</script>