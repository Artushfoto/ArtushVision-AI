---
title: "ArtushVision AI Free Trial: Limits, Testing & Microstock Workflow"
description: "Discover the ArtushVision AI Free Trial (Lite version). Test hardware compatibility, API connections, and our AI microstock metadata workflow before buying."
keywords: "ArtushVision AI, free trial, AI microstock software, auto-tagging, image metadata generator, stock photography workflow, local AI, OpenRouter"
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

# ArtushVision AI Free Trial Version (Lite)

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**We believe in complete transparency. ArtushVision AI offers a free, non-expiring Lite version so you can thoroughly test the AI microstock keywording software on your own hardware and verify your API connections before committing to a purchase.**

Because ArtushVision AI is a robust desktop application that utilizes both cloud APIs and local processing power, we strongly encourage every user to download the Trial version first. Test the workflow, ensure it fits your needs, and experience the automated AI image generation firsthand.

---

## Why Test Our AI Auto-Tagging Software Before You Buy?

Ensure a seamless experience by verifying your environment setup using the free Trial version.

* **Hardware Compatibility:** Verify that the application runs smoothly on your operating system and that local tools (like ExifTool and FFmpeg) execute correctly on your machine.
* **API Configuration:** Test your connection to <a href="/docs/cloud-ai-openrouter-api-setup.html">OpenRouter (Cloud AI)</a> or your local <a href="/docs/ollama-installation-guide.html">Ollama installation (Local AI)</a> to ensure prompts and models respond as expected for image metadata generation.
* **Workflow Integration:** Experiment with the <a href="/docs/settings-configuration-customization.html#the-category-matrix">Category Matrix</a>, <a href="/docs/global-stock-distribution-ftp.html#agency-profiles-and-server-groups">FTP Profiles</a>, and CSV generation to confirm the software perfectly aligns with your specific microstock distribution needs.
* **Test It First:** While thoroughly tested internally, some bugs might still slip through. **Any discovered issues will be patched as a top priority.**

---

## Free Trial Version Limitations & Features

The Trial version contains **no time limits** and grants access to all premium features, meaning you can use it forever. However, it enforces strict per-session usage limits to prevent commercial abuse. 

To reset the limits, you must restart the application.

* **AI Generation Limit:** You can process a maximum of **3 photos or videos** using our AI metadata generator (Cloud, Local, or Hybrid) per application run.
* **Metadata Saving Limit:** You can save EXIF/IPTC metadata changes to a maximum of **10 unique files** per application run.
* **FTP Upload Limit:** Limited to **5 unique assets** via the <a href="/docs/global-stock-distribution-ftp.html">FTP Uploader</a> per application run. You can distribute these 5 files to as many stock photography agencies and in as many batches as you like.
* **Getty Optimizer Limit:** You can optimize and translate keywords for a maximum of **3 unique assets** via the <a href="/docs/getty-images-esp-metadata-optimizer.html">Getty Images ESP Optimizer</a> per application run.

If you select a larger batch of photos than the limit allows, the application will intelligently offer to process only the permitted amount so you do not lose your work.

***NOTE***: *Run Without Limits: You can run the application indefinitely with absolutely no usage caps. If ArtushVision AI ends up saving you valuable time and money in your microstock workflow, consider purchasing a full license to unlock its peak potential and support further development.*

---

## Upgrading to ArtushVision AI PRO

Once you have verified that ArtushVision AI meets your professional standards, you can unlock unlimited processing instantly.

* **Lifetime License:** The PRO version is sold as a one-time purchase lifetime license for microstock contributors. No hidden subscriptions.
* **Instant Activation:** Purchase your license key on our website and enter it via **License > Activate License** in the top menu. The application will instantly remove all session limits without requiring a reinstallation.

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