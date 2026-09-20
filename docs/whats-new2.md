---
title: "What's New in ArtushVision AI | Release Notes & Features"
description: "Discover the latest updates in ArtushVision AI (v1.20). Explore Advanced SEO & Market Intelligence, Selling Score, Bestseller GAP analysis, Ground-Truth Verification, direct MP4 metadata injection, and bulk CSV export."
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

# What's New in ArtushVision AI v1.20

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[Frequently Asked Questions (FAQ)](/docs/faq.html)

Version 1.20 introduces a major expansion of ArtushVision AI: **Market Intelligence and advanced SEO tools for professional stock photographers and videographers.**

ArtushVision AI now combines visual relevance, market data, buyer-oriented search patterns, geographic verification, and taxonomy intelligence in a single metadata workflow.

---

## Microstock Market Intelligence

ArtushVision AI now goes beyond generating visually relevant keywords.

**Microstock Market Intelligence** adds market context to the keyword optimization workflow, helping contributors identify relevant opportunities based on available stock-market data.

It provides additional insight into:

* keyword demand and market supply,
* commercial search patterns,
* missing opportunities in existing metadata,
* relevant multi-word search phrases,
* and emerging or less saturated keyword candidates.

The feature is designed to **support metadata decisions**, not to predict or guarantee sales or search rankings.

---

### Bestseller GAP

**Bestseller GAP** identifies relevant keywords that are commonly associated with comparable successful stock content but are missing from the current metadata.

This makes it easier to discover potentially useful additions without replacing the contributor's own judgment.

You can:

* inspect individual missing keywords,
* review their relevance and market context,
* and add selected terms directly to your metadata.

---

### Commercial Phrases

Stock buyers often search for specific combinations of words rather than isolated terms.

The new **Commercial Phrases** engine identifies relevant multi-word search phrases and separates them from ordinary descriptive vocabulary.

Examples can include phrases such as:

* `isolated on white`
* `copy space`
* `aerial view`
* `wildlife in nature`

Only phrases compatible with the detected subject and context are considered.

---

### Market Discovery

**Market Discovery** provides an additional source of keyword candidates by comparing the current subject context with available market-search data.

It can surface:

* relevant lower-competition opportunities,
* related search concepts,
* emerging keyword candidates,
* and market terms that may not be obvious from visual analysis alone.

Market Discovery is intentionally presented as a **discovery tool** rather than a prediction of future trends.

---

### SEO Sort

Version 1.20 introduces **SEO Sort**, a dedicated workflow for organizing existing keywords.

With one click, ArtushVision AI can reorder the current keyword set according to its relevance and SEO importance, helping place the strongest terms earlier in the metadata.

This allows contributors to optimize keyword order without having to manually reorganize large keyword sets.

**Shortcut:** `Ctrl+Shift+S`

---

### Explainable Keyword Verdicts

Keyword recommendations are now presented using clear action-oriented categories:

* **🔥 MUST USE** — highly relevant terms with strong supporting evidence.
* **✅ RECOMMENDED** — useful relevant terms worth considering.
* **⚠️ OPTIONAL** — descriptive or contextual terms with lower priority.
* **❌ AVOID** — terms affected by conflicts, redundancy, or insufficient relevance.

The verdicts are designed to make the reasoning behind keyword suggestions easier to understand and review.

---

### Smart SEO Expand

**Smart SEO Expand** provides a focused set of additional keyword candidates based on the current metadata and detected subject.

Instead of generating a large list of loosely related words, the feature focuses on a smaller set of relevant candidates that can be reviewed and selectively added.

New discovery suggestions are visually separated from the existing keyword set for easier review.

---

## Improved Ground-Truth Verification

Version 1.20 also extends the way ArtushVision AI validates keyword candidates against available evidence.

### Geographic Verification

Geographic terms can be checked against available GPS and geographic information.

This helps distinguish between:

* locations supported by the photograph's metadata,
* locations supported by contextual evidence,
* and geographic terms that are not sufficiently supported.

The goal is to reduce incorrect geographic tagging while preserving relevant natural and administrative place names.

---

### Taxonomic Verification

ArtushVision AI now uses biological taxonomy as an additional source of evidence when working with animals, plants, fungi, and other taxonomic subjects.

The system can distinguish between:

* specific species,
* broader taxonomic groups,
* related organisms,
* and conflicting species suggestions.

This provides an additional safeguard against visually plausible but biologically incorrect keyword suggestions.

---

### Human Presence Verification

Human-related suggestions can be checked against visual evidence.

This helps prevent inappropriate human-related keywords from being introduced into scenes where people are not actually present, while allowing relevant contextual concepts when supported by the image.

---

## New Video Metadata Workflow

Version 1.20 extends ArtushVision AI beyond still photography with native metadata handling for video.

### Direct Metadata Write to MP4 / MOV

Metadata can now be written directly into supported MP4 and MOV files **without re-encoding the video stream**.

This means the video image and audio streams do not need to be rendered again simply to update metadata.

The workflow is designed for stock-video contributors working with applications and agencies that support standard embedded metadata workflows.

---

## Universal Drag & Drop

Importing content is now simpler.

You can drag folders or mixed batches directly from Windows Explorer into the ArtushVision AI workspace.

Supported workflows include:

* JPG and other supported image formats,
* RAW photographs,
* MP4 video,
* MOV video,
* and mixed batches.

---

## Multiple CSV Export

Version 1.20 expands agency export workflows with **multiple CSV templates in a single operation**.

Selected assets can be exported using different agency-specific templates without having to repeat the export process separately for every destination.

Configured export targets can also be remembered for recurring workflows.

---

## Improved Metadata Workflow

The new features are integrated into the existing ArtushVision AI workflow rather than requiring separate tools.

A typical workflow can now be:

**Analyze → Review → Verify → Optimize → SEO Sort → Export**

This allows visual analysis, keyword optimization, market research, verification, and agency export to remain part of one workflow.

---

## What Market Intelligence Does — and Does Not Do

Market Intelligence is intended to provide **additional evidence for metadata decisions**.

It does not guarantee:

* sales,
* downloads,
* search-engine position,
* agency acceptance,
* or future market demand.

Stock-market algorithms and buyer behavior can change independently of ArtushVision AI.

The purpose of Market Intelligence is to give contributors more useful information when deciding **which relevant keywords and phrases deserve attention**.

---

## Version 1.20 in Brief

**New**

* Market Intelligence
* Bestseller GAP
* Commercial Phrases
* Market Discovery
* SEO Sort
* Explainable Keyword Verdicts
* Smart SEO Expand
* Expanded geographic verification
* Expanded taxonomic verification
* Human-presence verification
* Direct MP4/MOV metadata writing
* Universal Drag & Drop
* Multiple CSV Export

Version 1.20 marks the transition from AI-assisted keyword generation toward a broader **metadata optimization and market-intelligence workflow for professional stock contributors**.


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

<!-- Odložené načtení Google Analytics pro maximální PageSpeed skóre -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    let analyticsLoaded = false;

    function loadAnalytics() {
      if (analyticsLoaded) return;
      analyticsLoaded = true;

      // 1. Dynamické vložení externího skriptu gtag.js s NOVÝM ID
      var gtagScript = document.createElement('script');
      gtagScript.async = true;
      gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-KCZWMGZFJ5';
      document.head.appendChild(gtagScript);

      // 2. Inicializace nastavení Google Analytics s NOVÝM ID
      window.dataLayer = window.dataLayer || [];
      window.gtag = function(){ dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', 'G-KCZWMGZFJ5');

      // 3. Odstranění posluchačů událostí po úspěšném načtení
      document.removeEventListener('scroll', loadAnalytics);
      document.removeEventListener('mousemove', loadAnalytics);
      document.removeEventListener('touchstart', loadAnalytics);
    }

    // Spuštění při první skutečné interakci uživatele
    document.addEventListener('scroll', loadAnalytics, { passive: true });
    document.addEventListener('mousemove', loadAnalytics, { passive: true });
    document.addEventListener('touchstart', loadAnalytics, { passive: true });

    // Pojistka: Pokud uživatel do 5 sekund nic neudělá, načíst Analytics automaticky
    setTimeout(loadAnalytics, 5000);
  });
</script>
