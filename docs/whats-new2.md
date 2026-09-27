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
  margin: 24px auto;
  max-width: 100%;
  text-decoration: none;
}
.screenshot-img {
  width: 100%;
  height: auto;
  display: block;
  border: 1px solid #333;
  border-radius: 8px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.18);
  transition: transform 0.2s ease, opacity 0.2s ease;
}
.screenshot-img:hover {
  opacity: 0.96;
  transform: translateY(-2px);
}

/* Badge a alert boxy */
.update-badge {
  display: inline-block;
  background-color: #2ea44f;
  color: #ffffff;
  font-size: 13px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 20px;
  margin-bottom: 12px;
}

.notice-box {
  background: #f6f8fa;
  border: 1px solid #d0d7de;
  border-left: 4px solid #0969da;
  border-radius: 6px;
  padding: 14px 18px;
  margin: 20px 0;
  font-size: 14px;
}

@media (prefers-color-scheme: dark) {
  .notice-box {
    background: #161b22;
    border-color: #30363d;
    border-left-color: #58a6ff;
    color: #c9d1d9;
  }
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

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu) | [Frequently Asked Questions (FAQ)](/docs/faq.html) | [Documentation Index](/index.html)

<div class="notice-box">
  <strong>🎉 Free Update for v1.x Users:</strong> Version 1.20 is a free update for all active lifetime license owners. Existing users can update directly via <strong>Help → Check for Updates</strong> inside the application.
</div>

Version 1.20 introduces a major milestone for ArtushVision AI: **Microstock Market Intelligence, Selling Score analytics, and lossless MP4/MOV video metadata injection for professional stock contributors.**

ArtushVision AI now unifies computer vision, stock-agency market demand, commercial buyer phrases, biological taxonomy, and geographic validation into a seamless, high-speed metadata workstation.

---

## Microstock Market Intelligence

ArtushVision AI now goes far beyond generating visually descriptive tags.

**Microstock Market Intelligence** injects real-world commercial context into your cataloging workflow, helping contributors identify missing high-demand keywords and buyer search patterns.

It provides actionable insight into:

* Keyword commercial demand vs. marketplace saturation,
* High-intent buyer search phrases,
* Revenue-critical keywords missing from your current metadata,
* Real-time metadata strength scoring before agency submission,
* Lower-competition emerging opportunities.

---

### Commercial Selling Score

Evaluate the commercial readiness and SEO weight of your metadata before submitting to agencies.

ArtushVision AI calculates a dynamic **Selling Score (0–100%)** based on:

* **Title & Description Structure:** Search-engine readability and strategic keyword placement.
* **Commercial Intent Coverage:** Ratio of action-oriented and conceptual buyer phrases versus generic descriptors.
* **Keyword Density & Order:** Optimal keyword count (avoiding over-tagging penalties) and placement of primary terms in the top 10–25 positions.
* **Redundancy & Conflict Suppression:** Deductions for spammy variants, irrelevant terms, or contradictory concepts.

The Selling Score gives you an instant, objective benchmark to ensure your asset can compete effectively in search rankings.

---

### Bestseller GAP Analysis

**Bestseller GAP** analyzes comparable top-performing stock media and detects high-converting keywords that are missing from your file.

Instead of guessing what buyers search for:

* Inspect high-relevance missing terms side by side with your current list,
* Review their commercial demand context,
* Add selected terms with a single click without overriding your creative judgment.

---

### Commercial Buyer Phrases

Stock buyers frequently search using multi-word phrases rather than single isolated keywords.

The **Commercial Phrases** engine automatically extracts and prioritizes commercial concepts such as:

* `isolated on white`
* `copy space for text`
* `aerial view`
* `candid lifestyle`
* `wildlife in natural habitat`

Every suggested phrase is strictly cross-checked against visual and contextual evidence to guarantee 100% agency compliance.

---

### Market Discovery

**Market Discovery** acts as an intelligent keyword scout, comparing your image subject against market search patterns.

It surfaces:

* **Niche Opportunities:** High-demand keywords with lower asset saturation,
* **Conceptual Search Terms:** Buyer-oriented conceptual metaphors (e.g., *resilience*, *teamwork*, *tranquility*) that direct visual inspection might miss,
* **Trending & Seasonal Queries:** Relevant emerging terms aligned with current commercial demand.

---

### SEO Sort

Stock agency algorithms (such as Adobe Stock and Shutterstock) weigh the first 10–25 keywords significantly higher than the rest.

With **SEO Sort**, ArtushVision AI reorders your entire keyword list with a single click:

* Core subject and primary commercial keywords are moved to the top positions,
* Secondary and contextual descriptors are organized cleanly after primary terms,
* Redundant or weak synonyms are deprioritized.

**Keyboard Shortcut:** `Ctrl+Shift+S`

---

### Explainable Keyword Verdicts

Say goodbye to black-box AI suggestions. Every suggested keyword now comes with clear, actionable classification:

* **🔥 MUST USE** — Essential subject and high-commercial-value terms with overwhelming evidence.
* **✅ RECOMMENDED** — Strong contextual and secondary terms that expand discoverability.
* **⚠️ OPTIONAL** — Broad, generic, or atmospheric keywords; useful if keyword quota allows.
* **❌ AVOID** — Contradictory, hallucinated, spammy, or geographically conflicting terms.

This transparent labeling allows you to review and approve dozens of tags in seconds.

---

### Smart SEO Expand

**Smart SEO Expand** provides a curated, non-destructive expansion of your existing keywords.

Rather than flooding your file with generic synonyms, it analyzes the specific gaps in your metadata and suggests a tight cluster of high-relevance additions. Discovery candidates are visually highlighted so you can approve them individually or in bulk.

---

## Advanced Ground-Truth Verification

Version 1.20 introduces multi-layered evidence checks to prevent metadata rejections and agency penalties.

### Geographic Verification & Reverse Geocoding

* Verifies location keywords against embedded EXIF GPS coordinates,
* Distinguishes verified shoot locations from loose contextual mentions,
* Automatically injects accurate administrative names (Country, State/Province, City, National Park),
* Prevents misleading geographic tags on generic studio or outdoor shots.

---

### Taxonomic & Biological Verification

For wildlife, bird, insect, botanical, and mushroom photography, precision is paramount. ArtushVision AI now leverages a comprehensive biological taxonomy database:

* **Scientific Binomial Names:** Automatically validates and provides scientific Latin names (e.g., *Panthera pardus*, *Passer domesticus*) alongside common names.
* **Taxonomic Hierarchy:** Safely introduces correct family, genus, and order terms while avoiding false species identification.
* **Species Confusion Safeguard:** Prevents common AI hallucinations between visually similar but biologically distinct species.

---

### Human Presence & Demographics Verification

* Checks human-related terms (e.g., *person*, *adult*, *portrait*, *looking at camera*) against computer-vision evidence.
* Suppresses inadvertent people-related keywords in landscapes, still lifes, and macro shots.
* When people are detected, verifies age group, shot framing, and activity accurately.

---

## Native Video Metadata Workflow

Version 1.20 brings full native metadata management to stock videographers.

### Lossless MP4 & MOV Direct Injection

Write titles, descriptions, copyright, and keywords directly into video files **without re-encoding**.

* **Instantaneous Processing:** Tagging an MP4 or MOV clip takes milliseconds, saving hours of re-rendering.
* **Zero Quality Loss:** Video and audio streams are preserved bit-for-bit with no compression artifacts.
* **Agency-Ready Standard:** Writes both QuickTime metadata atoms (`©nam`, `©des`, `©key`) and embedded XMP schemas natively recognized by **Adobe Stock, Pond5, Shutterstock, BlackBox, and Getty/iStock**.

---

## Streamlined Batch Operations

### Universal Drag & Drop

Effortlessly import entire projects into the workspace:

* Drag single files, folders, or mixed batches directly from Windows Explorer,
* Seamlessly handles mixed collections of **JPG, RAW, MP4, and MOV** files in a single queue,
* Automatically parses existing embedded metadata upon import.

---

### Multi-Agency CSV Export

Exporting to multiple agencies with different CSV formatting rules is now a one-step operation:

* Export selected assets across multiple agency templates (Shutterstock, Adobe Stock, Pond5, etc.) simultaneously,
* Saves custom column mappings and delimiter settings for recurring daily workflows,
* Fully supports agency-specific requirements (e.g., custom category columns, editorial flags).

---

## Key Shortcuts Reference

| Shortcut | Action |
| :--- | :--- |
| `Ctrl + Shift + S` | **SEO Sort** — Reorder keywords by commercial weight |
| `Ctrl + E` | **Smart SEO Expand** — Surface relevant gap terms |
| `Ctrl + Shift + V` | **Run Ground-Truth Verification** |
| `Ctrl + Enter` | **Save & Write Metadata** to selected file(s) |

---

## What Market Intelligence Does — and Does Not Do

Market Intelligence is engineered to give contributors **evidence-based data to make informed metadata decisions**.

It does **not** guarantee:

* Specific sales volumes or revenue numbers,
* Guaranteed first-page rankings on any stock agency,
* Automatic acceptance by agency inspection algorithms.

Stock agency search algorithms and buyer preferences evolve constantly. ArtushVision AI equips you with the best available data, keyword hierarchy, and verification tools to maximize your commercial discoverability.

---

## Version 1.20 Changelog Summary

* **New:** Microstock Market Intelligence suite.
* **New:** Real-time Commercial Selling Score (0–100%).
* **New:** Bestseller GAP analysis for missing high-performing terms.
* **New:** Commercial multi-word buyer phrase detection.
* **New:** Market Discovery tool for niche, low-competition tags.
* **New:** SEO Sort algorithm with `Ctrl+Shift+S` shortcut.
* **New:** Explainable Keyword Verdicts (🔥 MUST USE, ✅ RECOMMENDED, ⚠️ OPTIONAL, ❌ AVOID).
* **New:** Smart SEO Expand with dedicated suggestion tray.
* **New:** Native MP4 / MOV lossless metadata write (no re-encoding).
* **New:** Full scientific binomial (Latin) taxonomy validation.
* **New:** GPS-assisted geographic reverse validation.
* **New:** Human-presence evidence validation.
* **New:** Multi-template batch CSV export.
* **New:** Universal Drag & Drop supporting mixed RAW/JPG/MP4/MOV folders.

---

## How to Get Version 1.20

* **Existing Customers:** Open ArtushVision AI and navigate to **Help → Check for Updates** to download and install version 1.20 free of charge.
* **New Users:** Download the free Lite version or unlock the complete workstation with a lifetime license.

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

## Need Help?

<div id="flex-search-container">
  <input type="text" id="flex-search-input" placeholder="Search documentation, tutorials, shortcuts..." autocomplete="off">
  <ul id="flex-results-container"></ul>
</div>

* [Complete Documentation Index](/index.html#complete-documentation-index)
* [⭐ User Reviews & Testimonials](/docs/artushvision-reviews.html)
* [❓ Frequently Asked Questions (FAQ)](/docs/faq.html)
* [💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI — Stability, precision, and market intelligence for professional photography and video workflows.*

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
