---
title: "Frequently Asked Questions | ArtushVision AI Documentation"
description: "Professional answers to common questions about ArtushVision AI pricing, privacy, local AI setup, and technical requirements."
---
<div style="display: none;">
<style>
/* Skrytí záhlaví pro čistý webový vzhled */
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }

/* Celkové ladění dokumentu */
h1 { text-align: center; margin-bottom: 40px; color: #222; }
h2 { border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 40px; color: #444; }

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
details ul { margin-top: 10px; }
</style>
</div>

# Frequently Asked Questions (FAQ)

**Quick answers to help you master ArtushVision AI—from technical configuration to professional microstock workflows.**

---

## General and Pricing

<details>
<summary>Is ArtushVision AI a subscription service?</summary>
<p>
No. ArtushVision AI follows a <b>perpetual license model</b>. You pay once ($39.99) and own the software forever. There are no recurring monthly fees. You only pay for the <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">cloud AI</a> processing you actually use via your own API keys, or use <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">Local AI</a> for free.
</p>
</details>

<details>
<summary>What are the limitations of the Lite version?</summary>
<p>
The Lite version is a fully functional "trial" designed for testing your entire workflow. It has no time limits, but it processes files in smaller batches and includes a subtle watermark in non-critical metadata fields. The Pro version removes all limits and watermarks.
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
Privacy is our priority. In <b><a href="/docs/ai-metadata-generation-cloud-local-ollama.html#2-local-ai">Local AI mode</a></b>, your photos never leave your machine (processed via <a href="/docs/local-ai-model-manager-ollama.html">Local Model Manager</a>). In <b><a href="/docs/ai-metadata-generation-cloud-local-ollama.html#1-cloud-ai">Cloud mode</a></b>, only a temporary low-resolution thumbnail is sent to the AI provider—never your high-resolution originals.
</p>
</details>

<details>
<summary>How can it be so cheap compared to web tools?</summary>
<p>
By using an <a href="/docs/cloud-ai-openrouter-api-setup.html">OpenRouter API Key</a>, you pay the raw wholesale price of AI models (like Google Gemini). You bypass the 500%–1000% markups common in web-based subscription tools.
</p>
</details>

<details>
<summary>Do I need a high-end GPU for <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">Local AI</a>?</summary>
<p>
A dedicated NVIDIA GPU (RTX series) provides the best speed, but our <a href="/docs/local-ai-model-manager-ollama.html#deep-technical-insights">Local AI engine</a> can also run on your CPU thanks to <a href="/docs/ollama-installation-guide.html">Ollama's</a> optimized architecture.
</p>
</details>

---

## Workflow and Compatibility

<details>
<summary>Will the AI overwrite my existing keywords?</summary>
<p>
No. You have absolute control. Using <a href="/docs/manual-editing-detailed-photo-view.html#advanced-protection-logic">Smart Protection</a>, you can tell the AI to only append new tags or use variables like `{existing_keywords}` to let the AI intelligently expand your work.
</p>
</details>

<details>
<summary>How do I optimize for Getty Images / <a href="/docs/getty-images-esp-metadata-optimizer.html">ESP</a>?</summary>
<p>
Use the integrated <a href="/docs/getty-images-esp-metadata-optimizer.html">Getty Optimizer</a>. It validates your keywords against a <a href="/docs/getty-images-esp-metadata-optimizer.html#built-in-master-dictionary">master dictionary</a> of 11,000+ commercial terms to ensure 100% acceptance rates without manual guesswork.
</p>
</details>

<details>
<summary>Does it work with Lightroom, Zoner, or Bridge?</summary>
<p>
Yes. ArtushVision AI writes metadata directly into JPGs or standard XMP sidecars. Simply use the "Read Metadata from File" command in your favorite organizer to see the changes. Check our <a href="/docs/batch-operations-metadata-library-management.html#synchronized-file-operations">Batch Operations</a> guide for more.
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
Check your <a href="/docs/cloud-ai-openrouter-api-setup.html">OpenRouter</a> credit balance (minimum $5 recommended) and ensure you haven't set a "per-request" limit that is too low. Follow our <a href="/docs/cloud-ai-openrouter-api-setup.html">OpenRouter Setup Guide</a> for precise settings.
</p>
</details>

---

### Need more help?

* [Full AI Workflow Documentation](/docs/ai-metadata-generation-cloud-local-ollama.html)
* [Advanced Prompting Guide](/docs/advanced-ai-prompting-profiles-variables.html)
* [Global FTP Distribution Guide](/docs/global-stock-distribution-ftp.html)

---

### [Get Started Now]

* [Download Free Lite Version](https://www.artushfoto.eu/Software/Download-ArtushVision-AI)
* [Purchase Lifetime License - $39.99](https://www.artushfoto.eu/Software/Purchase-ArtushVision-AI)

---

*ArtushVision AI - Engineered for absolute control and professional metadata precision.*