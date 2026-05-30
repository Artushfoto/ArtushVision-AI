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

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/getty-resolver-add-term.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/getty-resolver-add-term.png" alt="ArtushVision AI - Interactive AI Resolver and Disambiguation" width="100%" class="screenshot-img">
</a>    

---

## 1. Built-in Master Dictionary & Non-Destructive Workflow

ArtushVision AI includes a massive, local Master Dictionary specifically built for the Getty Images commercial ecosystem. You no longer need to manually search the ESP portal for permitted terms.

* **Automated Mapping:** Instantly translates standard tags into approved Getty alternatives (e.g., expanding "malagasy" into the required "Malagasy People" and "Malagasy Culture" format).
* **Technical Tag Injection:** Automatically adds required structural tags such as Horizontal/Vertical, Photography, No People that Getty requires for commercial searchability.
* **Non-Destructive Safety:** Your original metadata remains completely untouched and safe. All Getty-optimized terms, titles, and descriptions are stored in dedicated `.getty` JSON sidecar files.
* **Universal Compatibility:** Work seamlessly alongside Adobe Bridge, Lightroom, or Zoner Photo Studio.

---

## 2. Accessing the Optimizer

Select one or more photos in the main grid, right-click, and select **"Getty Optimizer..."** from the context menu.

The main window displays two lists:
*   **Original Keywords:** Your source metadata (safe and untouched).
*   **Optimized Getty Keywords:** The resulting keywords mapped against the Master Dictionary.

### Main Window Actions:
*   **Interactive Resolver (AI Mapping)...**: Opens the advanced interactive table to manually or AI-resolve unknown words and ambiguities.
*   **Re-Optimize All (Local)**: A 1-click local optimization. It automatically unchecks unknown words, appends technical tags (e.g., *Horizontal*, *Vertical*, *Photography*), and sorts the keywords. It runs locally without consuming API tokens.
*   **Export ESP CSV**: Generates the final CSV file formatted specifically for the Getty Images ESP portal.
*   **Delete Getty Data**: Deletes the generated `.getty` sidecar files if you want to start from scratch.

---

## 3. Interactive Mapping (Getty Resolver)

The Resolver is the heart of the Getty optimization process. Click **Interactive Resolver** to open a detailed, interactive table of all your tags across the selected batch of photos.

### Photo Context & Thumbnails (Top Panel)
At the top of the window, you'll see thumbnails of your selected batch.
*   **Filter by Photo (Left-Click)**: Click any thumbnail to instantly filter the table below. It will show *only* the terms associated with that specific photo. Click again to clear the filter, or use the **"Clear Photo Filter"** button.
*   **Multi-Select**: Use `Ctrl + Click` to select multiple thumbnails.
*   **Context Menu (Right-Click)**: Right-click a thumbnail to copy/paste your perfectly mapped Getty terms across multiple photos, or to open the original file.

<video src="video/getty-optimizer-overview.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Using Keyword Sets in ArtushVision AI" aria-label="Overview of Getty Optimizer in ArtushVision AI">
  ArtushVision AI - Demonstration of seamless metadata drag and drop editing.
</video>
<p><a href="video/getty-optimizer-overview.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>


### The Resolution Table
1.  **Original Word**: The keyword from your metadata. **Double-click** an original word to edit it in place. If you type a comma (e.g., changing "cooked food" to "cooked, food"), the Resolver will intelligently split the word into two separate rows and remap them instantly.
2.  **Getty Term (Chips)**: The mapped terms from the Getty Master Dictionary. If multiple chips are shown, check the one that fits best. You can **double-click** a chip to delete it if it's irrelevant.
3.  **Status / Source**: Tells you where the term came from (e.g., *Internal Dictionary*, *User Dictionary*, *Cloud Suggested*, or *Unknown*).

### Filters & Tools
Use the top bar filters to quickly isolate problematic terms (*Unknown*, *Multiple terms*, *Cloud Suggested*, *Optimized Terms*).
*   **Undo (`Ctrl+Z`) / Redo (`Ctrl+Y`)**: The Resolver features a full local undo stack. If you accidentally split a word or paste the wrong tags, simply click Undo.
*   **☑ All / ☐ None**: Quickly select or deselect all visible rows (intelligently skips "Unknown" words).

---

## 4. Resolving with AI Beta

A major hurdle in metadata is homonyms—words with multiple meanings. If you use the word "crane," the AI analyzes the pixels to determine if it is a bird or a construction machine, selecting the exact correct branch of the Getty vocabulary.

1. Check the rows you want the AI to process (usually *Multiple terms* or *Unknown*).
2. Set the **"New AI terms:"** counter (0-50). 
   * *If you set it to `0`, the AI will only disambiguate existing words, saving API tokens.*
   * *If you set it > 0, the AI will also suggest completely new, highly relevant terms from the Getty Master Dictionary.*
3. Click **"Resolve with AI beta"**.

<video src="video/getty-optimizer-ai.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Using Keyword Sets in ArtushVision AI" aria-label="AI Getty Optimizer in ArtushVision AI">
  ArtushVision AI - Demonstration of seamless metadata drag and drop editing.
</video>
<p><a href="video/getty-optimizer-ai.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## 5. Personal User Getty Dictionary and Memory

Teach ArtushVision AI your specific niche. If you specialize in rare Latin species, local landmarks, or technical subjects missing from the Master Dictionary, you can map them once and save the rule directly to your Personal Dictionary.

*   **Add Term**: Click this button to search the Getty Master Dictionary manually. You can check multiple terms at once and apply them to the currently selected thumbnails (or to all photos if none are selected).
*   **User Dictionary**: A place to manage your custom mappings. 
    *   *Quick Add:* **Right-click** any Original Word in the table and select "Save 'word' to User Dictionary". Next time you load this word, it will automatically map to your preferred Getty term.
    *   *Manage:* Open the User Dictionary to manually add new mappings, delete old ones, or "Clear All" to rely solely on the built-in Master Dictionary.

[IMAGE: A smaller screenshot showing the User Dictionary manager window or the right-click context menu.]

---

## 6. Final Export and Global Distribution

Once your metadata is verified and the blue GETTY badges are active, you are ready for a flawless submission.

*   **Precision CSV Export:** Generate a flawlessly formatted spreadsheet ready for the Getty ESP portal.
*   **Zero-Touch Integration:** Combine this with the Smart FTP Suite to handle both file transfer and metadata synthesis in one unified workflow.

[IMAGE: A screenshot showing the Export ESP CSV button and the success dialog.]

---

## 7. Recommended Professional Workflow in 5 Steps

1. **Open the Optimizer:** Select your finished photos in the main grid and right-click to open the **Getty Optimizer**.
2. **Review & AI Fix:** Click **Interactive Resolver**. Set "New AI terms" to `0` and click **Resolve with AI beta** to let the AI fix any ambiguous words based on image context.
3. **Local Cleanup:** Click **Re-Optimize All (Local)**. This will automatically uncheck any remaining "Unknown" words, add required technical tags (Horizontal/Vertical, Photography), and sort the list.
4. **Verify & Save:** Review the result in the table. Click **OK** to save the `.getty` sidecar files to your disk.
5. **Export:** Back in the main Optimizer window, click **Export ESP CSV** to generate your final spreadsheet ready for upload. No rejections, no manual mapping on the portal.

---

### [Get Started Now]
* Download Free Lite Version
* Purchase Lifetime License - $39.99

---

← Back to ArtushVision AI Home

❓ Frequently Asked Questions (FAQ)

💬 Support, Bugs & Community Forum

---

*ArtushVision AI - Stability and precision for professional photography workflows.*
