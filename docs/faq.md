<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }

/* Flexbox kontejner pro rozdělení vršku (Hero sekce) na poloviny */
.hero-split {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 30px;
  margin: 10px 0 40px 0;
}
.hero-text {
  flex: 1.1;
}
.hero-image {
  flex: 0.9;
}
@media (max-width: 900px) {
  .hero-split {
    flex-direction: column;
  }
}

/* Zelený Privacy Callout Box s plnou podporou pro Světlý i Tmavý režim - CELÁ ŠÍŘKA */
.privacy-callout {
  background-color: rgba(46, 164, 78, 0.08);
  border: 1px solid rgba(26, 127, 55, 0.3);
  border-radius: 6px;
  padding: 18px;
  margin: 25px 0;
  width: 100%;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
}
.privacy-callout h2 {
  color: #1a7f37;
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 15px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.privacy-callout p {
  margin: 0;
  font-size: 13.5px;
  color: #24292f;
  line-height: 1.5;
}

/* Profesionální styl pro klikací screenshoty */
.screenshot-link {
  display: block;
  width: 100%;
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

/* Tlačítka (Call to Action) - UŽŠÍ PRO LEPŠÍ ZOBRAZENÍ VEDLE SEBE */
.btn {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 230px; /* Zmenšeno pro jistotu, že se vejdou vedle sebe */
  max-width: 100%;
  padding: 10px 15px;
  font-size: 15px;
  font-weight: 600;
  text-align: center;
  text-decoration: none;
  border-radius: 6px;
  transition: background-color 0.2s, color 0.2s, box-shadow 0.2s;
  cursor: pointer;
  box-sizing: border-box;
}
.btn-primary {
  background-color: #0969da;
  color: #ffffff !important;
  border: 1px solid #0969da;
}
.btn-primary:hover {
  background-color: #0550ae;
  box-shadow: 0 3px 8px rgba(9, 105, 218, 0.2);
}
.btn-success {
  background-color: #2da44e;
  color: #ffffff !important;
  border: 1px solid #2da44e;
}
.btn-success:hover {
  background-color: #2c974b;
  box-shadow: 0 3px 8px rgba(45, 164, 78, 0.2);
}

/* GitHub Téma vyhledávacího komponentu - ZAROVNÁNO DOLEVA */
#flex-search-container {
  max-width: 500px;
  margin: 15px 0 25px 0; /* Změněno auto na 0 pro zarovnání vlevo */
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
  .privacy-callout {
    background-color: rgba(35, 134, 54, 0.15);
    border: 1px solid rgba(46, 164, 78, 0.4);
  }
  .privacy-callout h2 {
    color: #2ea44e;
  }
  .privacy-callout p {
    color: #c9d1d9;
  }
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

<h1 style="text-align: left; margin-top: 0; padding-top: 0; font-size: 2.2em;">ArtushVision AI | Professional Metadata Automation</h1>

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
<ul>
  <li><b>Images:</b> JPG, RAW (CR2, NEF, ARW, etc.), TIFF, PNG, HEIC, WEBP.</li>
  <li><b>Video:</b> MP4, MOV, AVI, MKV.</li>
</ul>
</p>
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
A dedicated NVIDIA GPU (RTX series) provides the best speed, but our <a href="/docs/local-ai-model-manager-ollama.html#deep-technical-insights">Local AI engine</a> can also run on your CPU thanks to <a href="/docs/ollama-installation-guide.html">Ollama's</a> optimized architecture.
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
Use the integrated <a href="/docs/getty-images-esp-metadata-optimizer.html">Getty Resolver</a>. It validates your keywords against a <a href="/docs/getty-images-esp-metadata-optimizer.html#1-built-in-master-dictionary--non-destructive-workflow">master dictionary</a> of 9,867+ commercial terms and uses Cloud AI for intelligent disambiguation to ensure a Near-Perfect Acceptance Rate without manual guesswork.
</p>
</details>

<details>
<summary>Does it work with Lightroom, Zoner, or Bridge?</summary>
<p>
Yes. ArtushVision AI writes metadata directly into JPGs or standard XMP sidecars. Simply use the "Read Metadata from File" command in your favorite organizer to see the changes. Check our <a href="/docs/metadata-compatibility-and-file-handling.html#seamless-adobe-lightroom-and-other-photo-management-software-compatibility">Software Compatibility</a> guide for more.
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
Ensure <a href="/docs/ollama-installation-guide.html">Ollama is installed</a> and the service is running in your system tray. You can manage and download models directly through our <a href="/docs/local-ai-model-manager-ollama.html#integrated-hub-browser-and-downloader">Integrated Model Manager</a>.
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
<ol>
  <li>In the top application menu, go to <b>File &gt; Logging</b> and select <b>Debug (All)</b>.</li>
  <li>Repeat the exact action that caused the error so the application can record the background technical details.</li>
  <li>Go back to <b>File &gt; Logging</b> and click <b>Open Log File</b>. This will open a text file containing the error report.</li>
  <li>Take a screenshot of the application (especially if there is a visible error message or a visual glitch).</li>
  <li>Send the <b>saved log file</b> along with the <b>screenshots</b> and a <b>brief description</b> of what you were doing when the error occurred to our support email: <b>support [at] artushfoto [dot] eu</b>. Alternatively, you can create a new post in our <a href="https://github.com/Artushfoto/ArtushVision-AI/discussions">Community Forum</a>.</li>
</ol>
</p>
</details>

---

### Need more help?

* [Full AI Workflow Documentation](/docs/ai-metadata-generation-cloud-local-ollama.html)
* [Advanced Prompting Guide](/docs/advanced-ai-prompting-profiles-variables.html)
* [Global FTP Distribution Guide](/docs/global-stock-distribution-ftp.html)

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