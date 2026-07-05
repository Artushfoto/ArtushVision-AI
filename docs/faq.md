webp---
title: "Frequently Asked Questions | ArtushVision AI Documentation"
description: "Professional answers to common questions about ArtushVision AI pricing, privacy, local AI setup, and technical requirements."
---
<div style="display: none;">
<style>
/* Skrytí záhlaví pro čistý webový vzhled */
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }

/* Celkové ladění dokumentu */
h1 { text-align: center; margin-bottom: 20px; color: #222; }
h2 { border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 40px; color: #444; scroll-margin-top: 20px; }

/* Rychlá navigace (Table of Contents) */
.faq-toc {
    background: #f8f9fa;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    padding: 20px;
    margin-bottom: 40px;
}
.faq-toc p { font-weight: bold; margin-top: 0; margin-bottom: 10px; color: #333; }
.faq-toc ul { margin: 0; padding-left: 20px; }
.faq-toc li { margin-bottom: 5px; }
.faq-toc a { color: #0366d6; text-decoration: none; font-weight: 500; }
.faq-toc a:hover { text-decoration: underline; color: #0056b3; }

/* Stylování FAQ harmoniky */
details {
margin-bottom: 12px;
padding: 15px;
border: 1px solid #e1e4e8;
border-radius: 6px;
transition: background 0.3s ease;
}
details[open] { background: #fcfcfc; border-color: #d1d5da; }
summary {
font-weight: 600;
cursor: pointer;
font-size: 1.05em;
outline: none;
color: #0366d6;
}
summary:hover { color: #0056b3; }
details p { margin-top: 15px; line-height: 1.6; color: #333; }
details ul { margin-top: 10px; color: #333; }
details li { margin-bottom: 5px; }
</style>
</div>

# Frequently Asked Questions (FAQ)

**Quick answers to help you master ArtushVision AI - from technical configuration to professional microstock workflows.**

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

---

<div class="faq-toc">
  <p>Table of Contents</p>
  <ul>
    <li><a href="#general-licensing-and-pricing">General, Licensing and Pricing</a></li>
    <li><a href="#ai-privacy-and-costs">AI Privacy and Costs</a></li>
    <li><a href="#workflow-and-compatibility">Workflow and Compatibility</a></li>
    <li><a href="#microstock-export--ftp-upload">Microstock Export & FTP Upload</a></li>
    <li><a href="#data-safety--languages">Data Safety & Languages</a></li>
    <li><a href="#technical-setup">Technical Setup</a></li>
  </ul>
</div>

## General, Licensing and Pricing

<details>
<summary>Is ArtushVision AI a subscription service?</summary>
<p>
No. ArtushVision AI follows a <b>perpetual license model</b>. You pay once ($39.99) and own the software forever. There are no recurring monthly fees. You only pay for the <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#1-cloud-ai">cloud AI</a> processing you actually use via your own API keys, or use <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#2-local-ai">Local AI</a> for free.
</p>
</details>

<details>
<summary>Can I get a refund if I don't like the software?</summary>
<p>
Due to the digital nature of the software and the availability of a fully functional free Lite version, <b>all sales are final</b>. We strongly encourage you to download the Trial (Lite) version to test compatibility and workflows on your hardware before purchasing. Refunds are only issued in rare cases of proven technical failure of the license activation.
</p>
</details>

<details>
<summary>Do I get free updates after purchasing?</summary>
<p>
Yes! Your purchase grants a lifetime license for the specific version series (e.g., v2026.x). You will receive all minor updates, performance upgrades, and bug fixes for free within this cycle. Major generational leaps (e.g., a future v2027 series) may require an optional upgrade fee.
</p>
</details>

<details>
<summary>How many computers can I use my license on?</summary>
<p>
Your personal Pro license can be activated on up to 2 of your own devices, allowing you to use ArtushVision AI on your desktop workstation and your travel laptop simultaneously.
</p>
</details>

<details>
<summary>What are the limitations of the Lite version?</summary>
<p>
The Lite version is a fully functional "<a href="/docs/free-trial-limits-and-testing.html">Trial</a>" designed for testing your entire workflow. It has no time limits, but it processes files in smaller batches (e.g., max 10 saves or 5 FTP uploads per session) and includes a subtle watermark in non-critical metadata fields. The Pro version removes all limits.
</p>
</details>

<details>
<summary>Which file formats can I process?</summary>
<p>
ArtushVision AI supports professional standards including:
</p>
<ul>
  <li><b>Images:</b> JPG, RAW (CR2, NEF, ARW, etc.), TIFF, webp, HEIC, WEBP.</li>
  <li><b>Video:</b> MP4, MOV, AVI, MKV.</li>
</ul>
</details>

---

## AI Privacy and Costs

<details>
<summary>Is my data private during analysis?</summary>
<p>
Privacy is our priority. In <b><a href="/docs/ai-metadata-generation-cloud-local-ollama.html#2-local-ai">Local AI mode</a></b>, your photos never leave your machine (processed via <a href="/docs/local-ai-model-manager-ollama.html">Local Model Manager</a>). In <b><a href="/docs/ai-metadata-generation-cloud-local-ollama.html#1-cloud-ai">Cloud mode</a></b>, only a temporary low-resolution thumbnail is sent to the AI provider - never your high-resolution originals.
</p>
</details>

<details>
<summary>How can it be so cheap compared to web tools?</summary>
<p>
By using an <a href="/docs/cloud-ai-openrouter-api-setup.html">OpenRouter API Key</a>, you pay the raw wholesale price of AI models (like Google Gemini). You bypass the 500%–1000% markups common in web-based subscription tools.
</p>
</details>

<details>
<summary>Do I need a high-end GPU for Local AI?</summary>
<p>
A dedicated NVIDIA GPU (RTX series) provides the best speed, but our <a href="/docs/local-ai-model-manager-ollama.html">Local AI engine</a> can also run on your CPU thanks to <a href="/docs/ollama-installation-guide.html">Ollama's</a> optimized architecture.
</p>
</details>

---

## Workflow and Compatibility

<details>
<summary>Will the AI overwrite my existing keywords?</summary>
<p>
No. You have absolute control. Using <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#smart-data-safeguards">Smart Protection</a>, you can tell the AI to only append new tags or use variables like <code>{existing_keywords}</code> to let the AI intelligently expand your work.
</p>
</details>

<details>
<summary>How do I optimize for Getty Images / <a href="/docs/getty-images-esp-metadata-optimizer.html">ESP</a>?</summary>
<p>
Use the integrated <a href="/docs/getty-images-esp-metadata-optimizer.html">Getty Resolver</a>. It validates your keywords against a <a href="/docs/getty-images-esp-metadata-optimizer.html#1-built-in-getty-master-dictionary--non-destructive-workflow">master dictionary</a> of 9,867+ commercial terms and uses Cloud AI for intelligent disambiguation to ensure a Near-Perfect Acceptance Rate without manual guesswork.
</p>
</details>

<details>
<summary>Does it work with Lightroom, Zoner, or Bridge?</summary>
<p>
Yes. ArtushVision AI writes metadata directly into JPGs or standard XMP sidecars. Simply use the "Read Metadata from File" command in your favorite organizer to see the changes. Check our <a href="/docs/metadata-compatibility-and-file-handling.html#seamless-integration-with-adobe-lightroom-and-other-managers">Software Compatibility</a> guide for more.
</p>
</details>

---

## Microstock Export & FTP Upload

<details>
<summary>Can ArtushVision AI upload my photos directly to stock agencies?</summary>
<p>
Absolutely. The application features a built-in <b>FTP Manager</b>. You can configure multiple FTP servers (Shutterstock, Adobe Stock, etc.) and upload your finished photos and videos with a single click. It even supports multi-threading and auto-retries for unstable connections.
</p>
</details>

<details>
<summary>Do I have to manually map categories for every single agency?</summary>
<p>
No. Thanks to the <b>Category Matrix</b>, you map your image to a "Master Category" once, and the app automatically translates it into the correct specific IDs or subcategories required by Shutterstock, Adobe Stock, Alamy, or MotionElements during the CSV export or FTP upload.
</p>
</details>

---

## Data Safety & Languages

<details>
<summary>What happens if the AI makes a mistake? Can I undo changes?</summary>
<p>
You are completely safe. First, the grid editor supports full <b>Undo/Redo (Ctrl+Z)</b>. Second, the software features a robust backup system: it can generate full CSV backups, save original JPG files with a <code>.original</code> extension, or write safely into separate <code>.xmp</code> sidecar files for your RAW images.
</p>
</details>

<details>
<summary>Do I need to install ExifTool or FFmpeg manually?</summary>
<p>
No, ArtushVision AI comes pre-bundled with local versions of both ExifTool (for metadata writing) and FFmpeg (for video frame extraction). It works out of the box, though you can point it to custom installations in the Settings if you prefer.
</p>
</details>

<details>
<summary>Can I generate keywords in languages other than English?</summary>
<p>
The application natively focuses on English, as it is the strict standard for global microstock agencies. However, the UI features built-in translation tooltips, an interactive synonym finder, and multilingual spellcheck. You can also customize your AI prompts to output text in your native language for personal or local archiving.
</p>
</details>

---

## Technical Setup

<details>
<summary>I get an "<a href="/docs/ollama-installation-guide.html">Ollama</a> not found" error. How to fix it?</summary>
<p>
Ensure <a href="/docs/ollama-installation-guide.html">Ollama is installed</a> and the service is running in your system tray. You can manage and download models directly through our <a href="/docs/local-ai-model-manager-ollama.html">Integrated Model Manager</a>.
</p>
</details>

<details>
<summary>My API key is active, but AI results are empty.</summary>
<p>
Check your <a href="/docs/cloud-ai-openrouter-api-setup.html">OpenRouter</a> credit balance (minimum $5 recommended) and ensure you haven't set a "per-request" limit that is too low. It is also possible that the selected model has changed or is temporarily unavailable; try switching to a different model. Follow our guide on how to <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#how-to-change-the-ai-model-cloud--local">change the AI model</a>.
</p>
</details>

<details>
<summary>How do I report a bug or unexpected behavior?</summary>
<p>
If you encounter a crash or an error, providing a debug log helps us investigate and fix the issue much faster. Please follow these steps:
</p>
<ol>
  <li>In the top application menu, go to <b>File &gt; Logging</b> and select <b>Debug (All)</b>.</li>
  <li>Repeat the exact action that caused the error so the application can record the background technical details.</li>
  <li>Go back to <b>File &gt; Logging</b> and click <b>Open Log File</b>. This will open a text file containing the error report.</li>
  <li>Take a screenshot of the application (especially if there is a visible error message or a visual glitch).</li>
  <li>Send the <b>saved log file</b> along with the <b>screenshots</b> and a <b>brief description</b> of what you were doing when the error occurred to our support email: <b>support [at] artushfoto [dot] eu</b>. Alternatively, you can create a new post in our <a href="https://github.com/Artushfoto/ArtushVision-AI/discussions">Community Forum</a>.</li>
</ol>
</details>

---

### Need more help?
Search the documentation pages directly or jump back to the main [Complete Documentation Index](/index.html#complete-documentation-index).

---

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[⭐ User Reviews & Testimonials](/docs/artushvision-reviews.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*