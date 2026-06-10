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

The Getty Optimizer module in ArtushVision AI solves this by acting as a professional bridge between your creative work and the technical requirements of the ESP system. You can map words **manually (100% offline)** or let the **Cloud AI** do the heavy lifting for you.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/getty-resolver-add-term.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/getty-resolver-add-term.png" alt="ArtushVision AI - Interactive AI Resolver and Disambiguation" width="100%" class="screenshot-img">
</a>    

---

<h2 id="built-in-master-dictionary">1. Built-in Master Dictionary & Non-Destructive Workflow</h2>

ArtushVision AI includes a massive, local Master Dictionary specifically built for the Getty Images commercial ecosystem. You no longer need to manually search the ESP portal for permitted terms.

* **Automated Mapping:** Instantly translates standard tags into approved Getty alternatives (e.g., expanding "`Authentic`" into the required `"Real People", "candid", "Real Life", "Natural Pattern", "Auto Post", "Production Filter", "Digital Authentication"` format).
* **Technical Tag Injection:** Automatically adds required structural tags such as Horizontal/Vertical, Photography, No People that Getty requires for commercial searchability.
* **Non-Destructive Safety:** Your original metadata remains completely untouched and safe. All Getty-optimized terms, titles, and descriptions are stored in dedicated `.getty` JSON sidecar files.

---

## 2. Accessing the Optimizer

Select one or more photos in the main grid, right-click, and select **"Getty Optimizer..."** from the context menu.

The main window displays two lists:
* **Original Keywords:** Your source metadata (safe and untouched).
* **Optimized Getty Keywords:** The resulting keywords mapped against the Master Dictionary.

### Main Window Actions:
* **Interactive Resolver (AI Mapping)...**: Opens the advanced interactive table to manually or AI-resolve unknown words and ambiguities.
* **Re-Optimize All (Local)**: A 1-click local optimization. It automatically unchecks unknown words, appends technical tags (e.g., *Horizontal*, *Vertical*, *Photography*), and sorts the keywords. It runs locally without consuming API tokens.
* **Export ESP CSV**: Generates the final CSV file formatted specifically for the Getty Images ESP portal.
* **Delete Getty Data**: Deletes the generated `.getty` sidecar files if you want to start from scratch.

**Getty Images Optimizer Overview in ArtushVision AI**

<video src="video/getty-optimizer-overview.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Overview of Getty Optimizer">
  ArtushVision AI - Getty Optimizer Overview.
</video>
<p><a href="video/getty-optimizer-overview.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

<h2 id="interactive-ai-resolver-and-disambiguation">3. Interactive Mapping (Getty Resolver)</h2>

The Resolver is the heart of the Getty optimization process. Click **Interactive Resolver** to open a detailed, interactive table of all your tags across the selected batch of photos.

---
### Photo Context, Thumbnails & Dynamic Badges (Top Panel)
At the top of the window, you'll see thumbnails of your selected batch.
* **Dynamic Status Badges**: Each thumbnail features a live badge in the corner showing the exact number of valid Getty terms for that photo.
    * **Gray (Neutral)**: Unprocessed. The photo still contains unresolved "Unknown" words waiting for your input or AI analysis.
    * **Green**: Optimized. All unknown words are resolved, and the photo has between 5 and 50 valid terms.
    * **Red**: Limit Violation. The photo has fewer than 5 or more than 50 terms and needs adjustment.
* **Filter by Photo (Left-Click)**: Click any thumbnail to instantly filter the table below. It will show *only* the terms associated with that specific photo. Click again to clear the filter, or use the **"Clear Photo Filter"** button.
* **Multi-Select & Targeted Edits**: Use `Ctrl + Click` to select multiple thumbnails. When one or more thumbnails are selected, **any changes you make in the table below (checking terms, unchecking, or adding new terms) will apply strictly to those selected photos**, leaving the rest of the batch untouched.
* **Context Menu (Right-Click)**: Right-click a thumbnail to copy/paste your perfectly mapped Getty terms across multiple photos, or to open the original file.

---

### Interactive Table & Color-Coded Terms
The main table displays your original keywords on the left and the corresponding valid Getty terms (chips) on the right. Understanding the color coding is key to mastering the Resolver:

* **Blue Terms (Standard)**: These are standard, valid Getty terms successfully mapped from the master dictionary.
* **Green Terms (AI Suggested)**: These are brand new, highly relevant terms suggested by the Cloud AI based on your photo's text context and your prompt.
* **Red Text/Rows (Unknown)**: Words marked in red are not recognized by the Getty dictionary. **You must uncheck these rows** (or map them to a valid term), otherwise Getty will reject them during submit.

**Working with Multiple Terms & Purple Chips:**
Often, an original word can have multiple meanings (e.g., "Crane" can be a bird or machinery), or you simply want to assign multiple valid terms to one or more selected photos.
* **Global vs. Per-Photo Selection**: You can check multiple terms at once. By default, checking a term applies it to *all* photos in the batch that share the original word. However, you can click a specific photo thumbnail (Top Panel) and check a term *only* for that single photo.
* **The Purple Term (Mixed State)**: If you select a term for *some* photos but not *all* photos in your current batch view, the chip turns **Purple**. This immediately tells you that you have customized the selection and successfully disambiguated meanings across different photos within the same batch.

**Context Visualizer & Drag and Drop:**
To speed up your workflow when dealing with multiple photos and terms, you can use these interactive features:
* **Hover to Highlight**: Hover your mouse over any term (chip) to instantly highlight the photo thumbnails it is currently assigned to. If you hover over an *unselected* term, it will light up all photos containing that original keyword, showing you exactly where the term *can* be assigned.
* **Drag & Drop**: Found a perfect term and want to assign it to just one specific photo? Simply grab the term (bubble) and drag & drop it directly onto the desired photo thumbnail in the top panel. It will be instantly and exclusively added to that photo without affecting the rest of the batch.

---

### Interactive Table & Color-Coded Terms new

The Getty Resolver is designed to work perfectly even without an internet connection. The main table displays your original keywords on the left and the corresponding valid Getty terms (chips) on the right. Understanding the interface and color coding is key to mastering the Resolver:

1. **Original Word**: The keyword from your metadata. **Double-click** an original word to edit it in place. If you type a comma (e.g., changing "cooked food" to "cooked, food"), the Resolver will intelligently split the word into two separate rows and remap them instantly. Words marked in **red** are not recognized by the Getty dictionary and **must be unchecked** (or mapped to a valid term), otherwise Getty will reject them during submit.

2. **Getty Term (Chips)**: The mapped terms from the Getty Master Dictionary.
    * **Color Coding**:
        * **Blue Terms (Standard)**: These are standard, valid Getty terms successfully mapped from the master dictionary.
        * **Green Terms (AI Suggested)**: These are brand new, highly relevant terms suggested by the Cloud AI based on your photo's text context and your prompt.
        * **Purple Chips (Mixed State)**: If you select a term for *some* photos but not *all* photos in your current batch view, the chip turns **Purple**. This immediately tells you that you have customized the selection and successfully disambiguated meanings across different photos.
    * **Interaction**:
        * **Manual Selection**: You can check multiple terms at once. By default, this applies the term to *all* photos in the batch that share the original word. To apply a term to a single photo, click its thumbnail in the top panel first.
        * **Double-Click to Delete**: If multiple chips are shown and a suggested term is irrelevant, you can **double-click** the chip to delete it from the options.
        * **Hover Context Visualizer**: Hover your mouse over any term (chip) to instantly highlight the photo thumbnails it is currently assigned to. If you hover over an *unselected* term, it will light up all photos containing that original keyword, showing you exactly where the term *can* be assigned.
        * **Drag & Drop (Assign & Remove)**: Found a perfect term and want to assign it to just one specific photo? Simply grab the chip and drag & drop it directly onto the desired photo thumbnail to instantly assign it. To **remove** a term from a specific photo, hold **Alt** (or **Shift**) while dropping the chip onto the thumbnail. Alternatively, hold **Alt** and click a highlighted thumbnail while hovering over a chip to remove it instantly.

3. **Status / Source**: This column tells you where the term came from (e.g., *Internal Dictionary*, *User Dictionary*, *Cloud Suggested*, or *Unknown*). AI suggestions will feature green text, multiple ambiguous choices will be orange, and unknown words will be red.

---
**Manual Editing in Getty Optimizer**

<video src="video/getty-optimizer-manual.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Manual Editing in Getty Optimizer">
  ArtushVision AI - Getty optimizer manual editing Overview.
</video>
<p><a href="video/getty-optimizer-manual.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

### Filters & Tools
Use the top bar filters to quickly isolate problematic terms (*Unknown*, *Multiple terms*, *Cloud Suggested*, *Optimized Terms*).
* **Undo (`Ctrl+Z`) / Redo (`Ctrl+Y`)**: The Resolver features a full local undo stack. If you accidentally split a word or paste the wrong tags, simply click Undo.
* **☑ All / ☐ None**: Quickly select or deselect all visible rows (intelligently skips "Unknown" words).

---

## 4. Resolving with Cloud AI (Disambiguation)

A major hurdle in metadata is homonyms—words with multiple meanings. If you use the word "crane," how do you know which Getty tag to pick? The AI analyzes the pixels and the context of the image to determine if it is a bird or a construction machine, selecting the exact correct branch of the Getty vocabulary for you.

1. Check the rows you want the AI to process (usually *Multiple terms* or *Unknown*).
2. **Select AI Profile & Model**: Choose a pre-configured profile from the dropdown. 
   * *Tip: Click the **Gear icon (⚙)** to open the Profile Editor. Here you can select exactly which Vision model to use (e.g., Google Gemini 2.5 Flash Lite) and tweak the System Prompt to fine-tune how the AI selects and suggests words.*
3. Set the **"New AI terms:"** counter (0-50). 
   * *If you set it to `0`, the AI will only disambiguate existing words (mapping them to Getty terms), saving API tokens.*
   * *If you set it > 0, the AI will also suggest completely new, highly relevant terms from the Getty Master Dictionary.*
4. Click **"Resolve with AI beta"**.

**Using AI to Resolve Getty Terms**

<video src="video/getty-optimizer-ai.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Using AI to resolve Getty Terms">
  ArtushVision AI - Getty resolver with AI beta.
</video>
<p><a href="video/getty-optimizer-ai.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

**Applying Exported CSV to Getty ESP** (https://esp.gettyimages.com)

Go to `Templates` → `Apply from CSV` → `Submit`

<video src="video/getty-optimizer-apply-csv.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Apply CSV on Getty ESP">
  ArtushVision AI - Applying exported CSV to Getty ESP.
</video>
<p><a href="video/getty-optimizer-apply-csv.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

## 5. Personal User Getty Dictionary and Memory

Teach ArtushVision AI your specific niche. If you specialize in rare Latin species, local landmarks, or technical subjects missing from the Master Dictionary, you can map them once and save the rule directly to your Personal Dictionary.

* **Add Term**: Click this button to search the Getty Master Dictionary manually. You can check multiple terms at once and apply them to the currently selected thumbnails (or to all photos if none are selected).
* **User Dictionary**: A place to manage your custom mappings. 
     * *Quick Add:* **Right-click** any Original Word in the table and select "Save 'word' to User Dictionary". Next time you load this word, it will automatically map to your preferred Getty term.
     * *Manage:* Open the User Dictionary to manually add new mappings, delete old ones, or "Clear All" to rely solely on the built-in Master Dictionary.

**Adding Terms to User Getty Dictionary**

<video src="video/getty-user-dictionary.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Add New Term to User Getty Dictionary">
  ArtushVision AI - Add New Term to User Getty Dictionary.
</video>
<p><a href="video/getty-user-dictionary.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## 6. Final Export and Global Distribution

Once your metadata is verified and the blue GETTY badges are active, you are ready for a flawless submission.

* **Precision CSV Export:** Generate a flawlessly formatted spreadsheet ready for the Getty ESP portal.

---

## 7. Recommended Professional Workflow in 5 Steps

1. **Open the Optimizer:** Select your finished photos in the main grid and right-click to open the **Getty Optimizer**.
2. **Review & AI Fix:** Click **Interactive Resolver**. Set "New AI terms" to `10-30` and click **Resolve with AI beta** to let the AI fix any ambiguous words based on image context (or manually check the correct bubbles).
3. **Local Cleanup:** Click **Re-Optimize All (Local)**. This will automatically uncheck any remaining "Unknown" words, add required technical tags (Horizontal/Vertical, Photography), and sort the list.
4. **Verify Badges & Save:** Make sure the badges on the thumbnails have turned **Green** (indicating 5-50 valid terms). Click **OK** to save the `.getty` sidecar files to your disk.
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
