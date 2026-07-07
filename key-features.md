---
title: "Getty Images ESP Metadata Optimizer | ArtushVision AI Documentation"
description: "Master the Getty Images ESP Controlled Vocabulary. Learn how to use the Master Dictionary, AI Resolver, and automated keyword translation."
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

## ArtushVision AI v1.10 Released – Desktop AI Microstock Tagger with 100% Private Local AI & Getty ESP Optimizer

**ArtushVision AI** is a native desktop application designed to handle thousands of high-resolution photos and videos without stuttering. It gives you total control over your metadata, writes directly to XMP/IPTC sidecars, and automates multi-agency distribution.

With the release of **v1.10**, we are introducing full offline autonomy via Ollama and a dedicated Getty Images Controlled Vocabulary engine.

---

### Key Features & Functionality

*   **Versatile AI Engine Modes & Customization**
    *   **Cloud AI:** High-speed cloud processing via OpenRouter (gemini-2.5-flash-lite, GPT-4o, Claude 3.5 Sonnet ...). You maintain full control over your API usage through a **Built-in OpenRouter Dashboard**, allowing you to monitor token costs directly within the app and pay only raw API prices with total transparency.
    *   **Local AI (100% Free & Private):** Run standard visual analysis on your local hardware via Ollama. Perfect for sensitive shoots (personal archives, home family photos, travel journals, or sensitive unreleased commercial shoots) with zero API costs.
    *   **Hybrid AI (Local Vision + Cloud Text):** Your local GPU performs the heavy visual analysis, and a cloud model structures the text. Peak SEO quality at wholesale prices.
    *   **2-Pass Local AI:** Deep offline synthesis. A local Vision model reads the pixels, then a second specialized text model formats a perfect JSON completely offline.
    *   **Customizable AI Prompts:** Tailor the program exactly to your unique needs. Modify system prompts to guide the AI's descriptive style, enforce specific keyword structures, or adapt to your specific photography niche.
---
*   **Getty Images Optimizer (Master ESP Tool)**
    *   **Near-Perfect Acceptance:** Map your tags against a built-in Master Dictionary of 9,867+ approved terms using a dedicated Vision Model followed by a Text Model pass.
    *   **Interactive Getty Resolver:** Available for both Single and Batch modes with visual context highlighting and term splitting.
    *   **Semantic AI Disambiguation:** The AI analyzes image context to solve homonyms (e.g., automatically distinguishing a "crane" bird from a "crane" construction machine).
    *   **Non-Destructive Workflow:** Original metadata remains untouched; optimized terms are safely stored in separate XMP metadata.
---
*   **Manual Workflow & Ergonomics (Hands-On Control)**
    *   **Intuitive Drag & Drop Keywords:** Seamlessly drag and drop keyword bubbles to reorder them (vital for Adobe Stock top 10 priority weighting) or drag selected keywords directly between different photos in the grid.
    *   **Advanced Batch Metadata Application:** Select multiple files to bulk-add, overwrite, or clear Title, Description, and Keywords simultaneously. 
    *   **Smart Append Sync:** Type a keyword into a selection of hundreds of photos—the app injects it in real-time without wiping or overwriting their unique existing tags.
    *   **Interactive Integrated Map:** A built-in map module allows you to visually verify extracted GPS coordinates running the reverse geocoding.
    *   **Lightning-Fast Copy & Paste:** Use dedicated shortcuts to copy entire metadata blocks (or specific fields) from one master image and paste them across an entire batch.
    *   **Metadata Templates:** Save and load custom metadata presets for recurring shoots or specific studio setups.
---
*   **Global Distribution & Smart FTP Suite**
    *   **Multi-Server Batch Uploads with Multi-Threading:** Configure individual thread limits per agency to prevent connection blocks (`421 Too many connections`).
    *   **1-Click Automated CSV Upload:** The app generates a temporary, agency-specific CSV with matching category IDs, uploads it alongside your media, and automatically purges it from your drive.
    *   **Universal Category Mapping:** Pre-configured and easily adjustable category mapping for Adobe Stock, Shutterstock, and other major microstock agencies.
    *   **FTP Status Badges:** Successful uploads write micro-badges directly into XMP metadata for persistent tracking.
    *   **Custom FTP Profiles:** Create specialized configurations (e.g., "Stock Photo", "Editorial").
---
*   **Advanced Interface & Portfolio Organization**
    *   **Blazing-Fast Image Grid:** Displays Titles, Descriptions, and Keywords directly below every card. Includes comprehensive Thumbnail Badges (GPS, XMP, ORIG, RAW, VIDEO, GETTY, FTP, CAT).
    *   **Visual Status Indicators:** Color-coded states (Gray/Yellow/Green/Red) warn you in real-time about validation errors.
    *   **Top Toolbar:** Quick access to AI Profiles, Absolute Priority AI Hints, and Speed/Thread control.
    *   **Filter Bar:** Smart Search (with Case sensitivity), Folder Filtering with live photo counts, and File Type Filters.
    *   **Absolute Priority AI Hints:** Force the AI to treat your manual hints (obscure locations, Latin species) as absolute facts, completely eliminating hallucinations.
    *   **Flat View:** Toggle a unified, continuous list view for all loaded subfolders simultaneously.
---
*   **Universal Metadata Compatibility:** 100% compliant with  standard EXIF, IPTC, and XMP schemas. Your data is written safely to sidecars or directly embedded, ensuring seamless round-trip interoperability with industry-standard software like Adobe Lightroom, Bridge, and Capture One
    *   **Keyword Order Restoration:** Easily revert to your original keyword sequencing with a single click. This safety net guarantees that your manually sorted priority tags (crucial for Adobe Stock's Top 10 algorithm) are instantly restored if you need to roll back changes after an AI pass or batch edit.
---
*   **Professional Metadata Management & Linguistics**
    *   **Detail Photo View:** Inline editing with real-time word and character counters.
    *   **Category Management:** Easily assign standard microstock categories to single images or entire batches to ensure full compliance with agency submission requirements.
    *   **Metadata Protection:** Strict preservation of existing keywords and Face Recognition (People tags).
    *   **Auto-GPS Country Lookup (Reverse Geocoding):** Auto-translates GPS coordinates into readable city/country names via OpenStreetMap or ArcGIS to give the AI geographical context.
    *   **Dual-Language Spellcheck:** Real-time underlining and suggestions. Validate against two dictionaries simultaneously (e.g., English + your native language) without switching settings.
---
*   **Powerful Batch Operations**
    *   **Smarter Batch Rename:** Rename thousands of files using dynamic variables like `{TITLE}`, `{CC}`, `{DATE}`, or `{FOLDER_NAME}`.
    *   **Type-Ahead Autocomplete:** Predictive text powered by a pre-warmed database of 300,000+ highly commercial stock terms.
    *   **Bulk Metadata Editing:** Smart Add/Remove/Replace with `Old -> New` syntax and `Ctrl+H` support.
    *   **File Operations:** Integrated Copy, Move, and Delete with complete sidecar file synchronization.
---
*   **Comprehensive Settings & Configuration**
    *   **Ollama VRAM Context Tuning:** Optimize memory allocation based on your GPU hardware.
    *   **Video Economy Mode:** Collage-based analysis to minimize API consumption and process video files efficiently.
    *   **Integrated Metadata Translator:** Easily translate existing tags between languages.
    *   **Field Constraints:** Customizable safety guardrails and visual per-session caps.

---

**Pricing Model:** Standard web tools lock you into recurring subscriptions. ArtushVision AI is sold as a **Commercial Lifetime License for a one-time payment of $39.99**. 

**Try Before You Buy:** I highly encourage everyone to test their hardware compatibility first. Download the fully functional **Free Lite Edition** (has small per-session caps, but no time expiration).

**Check it out here:** [https://vision.artushfoto.eu](https://vision.artushfoto.eu)

💬 *Let me know what you think! I am actively patching bugs and adding features based on contributor feedback.*

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[⭐ User Reviews & Testimonials](/docs/artushvision-reviews.html)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*