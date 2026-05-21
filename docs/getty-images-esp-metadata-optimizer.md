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

# Getty Images Export Optimizer: Master the ESP Controlled Vocabulary

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Eliminate submission errors and keyword rejections. ArtushVision AI ensures Near-Perfect Acceptance Rate with the Getty Images ESP system through automated keyword translation and context-aware AI disambiguation.**

Uploading to Getty Images (ESP) is often challenging due to their strict Controlled Vocabulary (CV). Standard keywords used for other stock agencies are frequently rejected or mismatched by the ESP portal, leading to tedious manual corrections.

The Getty Optimizer module in ArtushVision AI solves this by acting as a professional bridge between your creative work and the technical requirements of the ESP system.

[IMAGE: A wide, clean screenshot of the Getty Optimizer main window showing the photo grid, the Optimize All button, and the blue GETTY status badges.]

---

## Built-in Master Dictionary

ArtushVision AI includes a massive, local Master Dictionary specifically built for the Getty Images commercial ecosystem. You no longer need to manually search the ESP portal for permitted terms.

* **Automated Mapping:** Instantly translates standard tags into approved Getty alternatives (e.g., expanding "malagasy" into the required "Malagasy People" and "Malagasy Culture" format)..
* **Technical Tag Injection:** Automatically adds required structural tags such as Number of People, Camera Settings, or Age Brackets that Getty requires for commercial searchability.
* **Redundancy Cleanup:** Intelligently merges duplicate meanings and removes prohibited terms before they reach the submission stage.

---

## Interactive AI Resolver and Disambiguation

A major hurdle in metadata is homonyms—words with multiple meanings. ArtushVision AI uses Vision AI to look at the actual content of your image to resolve these ambiguities.

* **Context-Aware Disambiguation (beta):** If you use the word "crane," the AI analyzes the pixels to determine if it is a bird or a construction machine, selecting the exact correct branch of the Getty vocabulary.
* **Visual Context Highlighting:** When selecting a term in the Resolver, the application highlights all thumbnails in your grid that contain that specific concept, allowing for instant batch verification.
* **Dynamic Word Splitting:** Double-click any complex phrase to split it into individual terms. The application re-evaluates the new terms against the Master Dictionary in real-time.

**Interactive AI Resolver and Disambiguation**
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/getty-resolver-add-term.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/getty-resolver-add-term.png" alt="ArtushVision AI - Interactive AI Resolver and Disambiguation" width="100%" class="screenshot-img">
</a>    

---

## Personal User Getty Dictionary and Memory

Teach ArtushVision AI your specific niche. If you specialize in rare Latin species, local landmarks, or technical subjects missing from the Master Dictionary, you can map them once and save the rule directly to your Personal Dictionary.

* **Persistent Learning:** Save custom mappings to your User Dictionary. The application will automatically apply these translations to all future exports.
* **Database Control:** You have full access to edit or remove your custom mappings, ensuring your personal metadata database remains accurate as your portfolio grows.

---

## Non-Destructive Workflow and Sidecars

Your original metadata remains safe. ArtushVision AI follows a professional safety-first logic to ensure your primary files are never corrupted.

* **Independent Sidecars:** All Getty-optimized terms, titles, and descriptions are stored in dedicated .getty JSON sidecar files.
* **XMP Integrity:** Your original keywords, Lightroom ratings, and People tags (Face Recognition) are preserved in your original files (see [Smart Protection](/docs/manual-editing-detailed-photo-view.html#advanced-protection-logic)).
* **Universal Compatibility:** Work seamlessly alongside Adobe Bridge, Lightroom, or Zoner Photo Studio.

[IMAGE: A smaller screenshot showing the User Dictionary manager window or the right-click context menu.]

---

## Final Export and Global Distribution

Once your metadata is verified and the blue GETTY badges are active, you are ready for a flawless submission.

* **Precision CSV Export:** Generate a flawlessly formatted spreadsheet ready for the Getty ESP portal.
* **Zero-Touch Integration:** Combine this with the [Smart FTP Suite](/docs/global-stock-distribution-ftp.html) to handle both file transfer and metadata synthesis in one unified workflow.

[IMAGE: A screenshot showing the Export ESP CSV button and the success dialog.]

---

### Professional Workflow in 3 Steps:

1. **Optimize All:** Select your folder and click Optimize All. The app translates the majority of terms using the [Master Dictionary](#built-in-master-dictionary).
2. **Resolve Unknowns:** Use the Interactive Resolver to map any remaining red (unknown) words or let the AI pick the best branch for ambiguous terms.
3. **Export:** Export the final verified data directly into the Getty ESP template. No rejections, no manual mapping on the portal.

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