---
title: "Ollama Installation & Setup Guide | ArtushVision AI"
description: "Step-by-step instructions for installing Ollama to run local AI Vision and Text models completely offline with ArtushVision AI."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
</style>
</div>

# Ollama Installation & Setup Guide

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**To use the 100% private <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">Local AI</a> or <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">Hybrid AI</a> workflows in ArtushVision AI, you need to install Ollama. Ollama is a lightweight, secure background service that allows you to run powerful AI models directly on your hardware without sending any data to the cloud.**

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

[IMAGE: A screenshot of the Windows system tray showing the small Ollama alpaca icon running in the background.]

---

## Step 3: Verify It's Running

To ensure Ollama is working correctly and ready to connect with ArtushVision AI:

1. Check your **Windows System Tray** (the bottom-right corner of your screen near the clock). You should see the Ollama icon.
2. Open your web browser and type `http://localhost:11434` into the address bar.
3. If you see a simple blank page with the text **"Ollama is running"**, the installation was successful!

---

## Step 4: Connect with ArtushVision AI

You do not need to use the command line (Terminal) to download models. ArtushVision AI handles everything for you visually.

1. Open **ArtushVision AI**.
2. Navigate to **AI Mode Selection** and choose **<a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">Local AI (Ollama)</a>** or **<a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">Hybrid AI</a>**.
3. Click on the **[Local Model Manager](/docs/local-ai-model-manager-ollama.html)** icon in the interface.
4. From the built-in **Hub Browser**, you can now browse, download, and manage models (like `qwen2.5-vl:3b` for Vision tasks) with a single click.

---

## Troubleshooting

* **"Ollama not found" error in ArtushVision AI:** This means the background service is stopped. Search for "Ollama" in your Windows Start Menu and launch it. Wait a few seconds for the icon to appear in your system tray, then try again.
* **Slow Performance:** Local AI relies heavily on your computer's RAM and GPU (VRAM). For the best experience, close heavy applications (like modern games or heavy video renders) while running offline AI batches.

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

---

*ArtushVision AI - Professional precision and complete offline AI control.*