webp---
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

# Getty Images ESP Metadata Optimizer: Master the Controlled Vocabulary

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Eliminate submission errors and keyword rejections. ArtushVision AI ensures a Near-Perfect Acceptance Rate with the Getty Images ESP system through manual or automated keyword translation and context-aware AI disambiguation.**

Optimizing metadata for the **Getty Images / iStock ESP portal** is one of the most demanding tasks for **stock contributors**. Getty Images enforces a strict **Controlled Vocabulary (CV)** of over 9,800 approved commercial terms. Standard keywords used for other stock agencies are frequently rejected or mismatched by the ESP portal, leading to tedious manual corrections.

The **Getty Optimizer module** in ArtushVision AI solves this by acting as a professional bridge between your creative work and the technical requirements of the ESP system. You can map words **manually**, use **Local Semantics (100% offline)**, or let the **Cloud AI** do the heavy lifting for you.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/getty-resolver-add-term.webp" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/getty-resolver-add-term.webp" alt="ArtushVision AI - Interactive AI Resolver and Disambiguation for Getty ESP" width="100%" class="screenshot-img">
</a>    

---

## 1. Built-in Getty Master Dictionary & Non-Destructive Workflow

ArtushVision AI includes a massive, local **Master Dictionary** specifically built for the Getty Images commercial ecosystem. You no longer need to manually search the ESP portal for permitted terms.

* **Automated Keyword Mapping:** Instantly translates standard tags into approved Getty alternatives (e.g., expanding "`Authentic`" into the required `"Real People", "candid", "Real Life", "Natural Pattern", "Auto Post", "Production Filter", "Digital Authentication"` format).
* **Technical Tag Injection:** Automatically adds required structural tags such as *Horizontal/Vertical*, *Photography*, or *No People* that Getty requires for **commercial searchability**.
* **Non-Destructive Safety:** Your original metadata remains completely untouched and safe. All Getty-optimized terms, titles, and descriptions are stored in dedicated, custom `XMP-getty` fields directly within the files, allowing this data to be instantly recalled or reloaded at any time.

---

## 2. Accessing the Getty ESP Optimizer & Main Interface

Select one or more photos in the main grid, right-click, and select **"Getty Optimizer..."** from the context menu. 

The main dashboard displays your original keywords side-by-side with the optimized **Getty tags**. From this view, you can trigger key actions or launch the advanced **Interactive Resolver** interface.

<video src="video/getty-optimizer-overview.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Overview of Getty ESP Optimizer">
  ArtushVision AI - Getty ESP Optimizer Overview.
</video>
<p><a href="video/getty-optimizer-overview.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

### Main Control Panel Actions:
* **Interactive Resolver (AI Mapping)...**: Opens the visual dashboard for rapid validation and mapping.
* **Export ESP CSV...**: Generates a final, clean **CSV spreadsheet** specifically formatted for direct import into the **Getty Images ESP portal**.
* **Export for Getty...**: Creates copies of the selected files (JPEGs, RAWs, or videos) in your target directory and writes the optimized Title, Description, and approved Keywords directly into their standard metadata fields (EXIF/IPTC/XMP) using ExifTool.
  * **`Direct Upload:`** Simply upload these embedded files directly to the Getty portal, **no CSV import is required**. Once the upload is complete, you can safely delete these exported copies from your local drive to save disk space, as they can be fully re-generated from your originals at any time.
* **Delete Getty Data**: Clears all generated `getty terms` from the selected files' metadata space so you can start the optimization process from scratch.
* **Custom Content Control:** The Getty Images Export Optimizer also allows you to set a **specific title and description** tailored exclusively for the Getty ESP portal. These adjustments are applied strictly to your Getty metadata and have no impact on your standard title and description.

## 3. Interactive AI Resolver Dashboard for Keyword Mapping

When you open the **Interactive Resolver**, you are presented with an advanced dual-panel layout designed for rapid inline validation and micro-management of your **batch metadata**.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/interactive-resolver-dashboard.webp" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/interactive-resolver-dashboard.webp" alt="ArtushVision AI - The Interactive AI Resolver Dashboard for Getty Metadata" width="100%" class="screenshot-img">
</a>  

### Interactive Table & Color-Coded Terms

The main table displays your original keywords on the left and the corresponding valid Getty terms (chips) on the right. 

   * **Original Word**: The keyword from your metadata. **Double-click** to edit it in place. If you type a **comma** (e.g., changing "cooked food" to "cooked, food"), the Resolver will intelligently split the word into two separate rows. Words marked in **red** are not recognized by the Getty dictionary and must be resolved or unchecked before submission.
   * **Orange Terms (Unmapped / Unrecognized / Ambiguous):** These represent unrecognized keywords. Because Getty's official vocabulary is proprietary, the built-in master dictionary cannot cover 100% of it. However, an unrecognized keyword might still be a valid Getty term. If it is, you can easily add it to your personal database by **right-clicking the word** and saving it to your **User Dictionary**. Once added, it will automatically be recognized and reported as a **valid Getty term** in all future optimizations and exports.
   * **Blue Terms (Standard)**: Valid Getty terms successfully mapped from the master dictionary.
   * **Green Terms (AI or Local Semantics Suggested)**: Brand new, highly relevant terms suggested by the Cloud AI or local offline Semantics model.
   * **Purple Chips (Mixed State)**: Indicates that the term is selected for *some* photos but not *all* photos in your current batch view.

**Interaction & Shortcuts**:
   * **Manual Selection**: Click any active colored bubble to check/uncheck it.
   * **Hover Context Visualizer**: Hover your mouse over any chip to instantly highlight the photo thumbnails it is currently assigned to (or can be assigned to).
   * **Drag & Drop (Assign & Remove)**: Grab a chip and drop it directly onto a photo thumbnail to instantly assign it. To **remove** it from that photo, hold **Alt** or **Shift** while dropping the chip.
   * **Undo/Redo**: Use `Ctrl+Z` and `Ctrl+Y` to safely step backward or forward through your edits.

---

### Control Panel Element Breakdown

The bottom control panel is organized into two horizontal rows for efficient access:

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/control-panel-element-breakdown.webp" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/control-panel-element-breakdown.webp" alt="ArtushVision AI - Resolver Control Panel Element Breakdown" width="100%" class="screenshot-img">
</a>  

#### Row 1: Cloud AI & UI Settings
* **`Resolve with AI beta` (Green Button)**: Triggers the Cloud AI semantic resolver to process selected images.
* **Profile Selector (`Getty_Default.json` Dropdown)**: Selects the active AI system prompt profile, or allows you to create your own depending on your needs. Use different profiles for varying photography styles or **microstock targets**.
* **Profile Settings (Cog Icon ⚙)**: Opens the Profile Editor where you can modify the model selection, system prompt templates, variables (such as `{loc_hint}` or `{date_info}`), and keyword blacklists.
* **`New AI terms:` (Spinbox)**: Controls the number of new approved Getty keywords the AI should suggest per photo. Setting this to `0` disables new suggestions, while `5` to `8` is recommended for high-quality, relevant tags. Higher values can lead to less precise or irrelevant suggestions.

* **`Row height:` (Spinbox)**: Adjusts the vertical line spacing of the main resolver table (between `30px` and `150px`) to customize data density.

#### Row 2: Offline Semantic Resolving & Local Actions
* **`Offline Suggest` (Blue Button)**: Starts the local semantic suggestion engine (**100% local offline, no API credits required**).
* **`Suggest Threshold:` (Spinbox)**: Sets the minimum semantic similarity score (from `0.10` to `1.00`) required for local matching. The default is `0.45`. Higher values (e.g. 0.70) produce fewer but more relevant suggestions. Lower values (e.g. 0.40) produce more suggestions but they might be less relevant.
* **`Model:` (Dropdown)**: Chooses which **local ONNX embedding model** to use for semantic similarity calculations.
Available models:
  * **MiniLM-L6-v2 (Super-Fast):** A lightning-fast, lightweight model with very low hardware requirements, making it ideal for modest or older machines.
  * **BGE-small-en-v1.5 (Accurate):** The recommended default choice, delivering solid, well-balanced accuracy and excellent processing speed.
  * **BGE-base-en-v1.5 (Maximum Accuracy):** Provides the absolute maximum accuracy in its class for pinpoint semantic mapping, at the cost of slightly higher memory and CPU utilization.
* **`Add Term` (Button)**: Opens a manual search dialog to look up and append approved Getty terms directly to selected photos.
* **`User Dictionary` (Button)**: Accesses your personal persistent vocabulary database and the new **Personalization Blacklist**.
* **`Re-Optimize All (Local)`(Button)**: A 1-click local utility that runs without consuming API tokens. It automatically unchecks unknown terms, appends structural technical tags, and sorts the keywords alphabetically.

---

### Photo Context, Thumbnails & Dynamic Badges (Top Panel)

At the top of the window, you'll see thumbnails of your selected batch:
* **Dynamic Status Badges**: Each thumbnail features a live badge in the corner showing the exact number of valid Getty terms for that photo.
  * **Gray (Neutral)**: Unprocessed. The photo still contains unresolved "Unknown" words waiting for your input or AI analysis.
  * **Green**: Optimized. All unknown words are resolved, and the photo has between 5 and 50 valid terms.
  * **Red**: Limit Violation. The photo has fewer than 5 or more than 50 terms and needs adjustment.
* **Filter by Photo (Left-Click)**: Click any thumbnail to instantly filter the table below. It will show *only* the terms associated with that specific photo. Click again to clear the filter.
* **Multi-Select & Targeted Edits**: Use `Ctrl + Click` to select multiple thumbnails. When one or more thumbnails are selected, **any changes you make in the table below will apply strictly to those selected photos**, leaving the rest of the batch untouched.
* **Context Menu (Right-Click)**: Right-click a thumbnail to copy/paste your perfectly mapped Getty terms across multiple photos, or to open the original file.

* **Getty Resolver Hover Highlights**: Hovering your mouse over any Getty term chip in the table dynamically highlights related photo thumbnails in the sidebar:
  * **Blue Border**: The photo already has this specific Getty term checked (active).
  * **Orange Border**: The photo contains the original keyword, but this Getty term is currently unchecked (candidate photo).

<video src="video/getty-optimizer-manual.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Manual Editing in Getty ESP Optimizer">
  ArtushVision AI - Getty optimizer manual editing Overview.
</video>
<p><a href="video/getty-optimizer-manual.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## 4. AI-Powered Metadata Optimization Engines

### Cloud AI Resolving & Disambiguation

Cloud AI resolving uses advanced Vision & Language models (such as Gemini 2.5 Flash Lite or GPT-4o) via OpenRouter to read the visual context of your images and handle homonyms, words with multiple meanings.

**Example**: If your original keyword is **"crane"**, the Cloud AI reviews the photo's visual content, title, description, and GPS data to identify whether the photo features a construction site (mapping it to `crane (construction machine)`) or a wetland (mapping it to `crane (bird)`).

If **New AI terms** is set greater than `0`, the AI will also discover and suggest completely new concepts that are guaranteed to exist in Getty’s controlled vocabulary database.

<video src="video/getty-optimizer-ai.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Using AI to resolve Getty ESP Terms">
  ArtushVision AI - Getty resolver with AI beta.
</video>
<p><a href="video/getty-optimizer-ai.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

### Offline Resolving (Local Semantics)
The **Offline Suggest** feature uses local vector embedding models running on the ONNX Runtime directly on your CPU. **Based on our extensive real-world testing, this offline workflow performs exceptionally well**, delivering highly accurate keyword mapping and context evaluation without any cloud API dependency. It automatically transforms your keywording workflow in three automated steps:

1. **Context Understanding:** The Local Semantics analyzes existing keywords to target the core theme (e.g., *snow, mountains* automatically targets *winter sports*).
2. **Automatic Cleaning & Disambiguation:** Red-marked unrecognized rows are checked against the Getty database via vector encoding. If a close match fits the theme, it is corrected; otherwise, it is skipped. Ambiguous words are automatically locked into their correct definition based on nearby tags.
3. **Controlled Keyword Expansion:** The local model compares context vectors against the pre-compiled Getty Vector Database and appends new relevant terms up to your chosen **Suggest Threshold** limit.

    * **MiniLM-L6-v2**: Super-fast and lightweight model for modest hardware.
    * **BGE-small-en-v1.5**: Recommended default balancing speed and precision.
    * **BGE-base-en-v1.5**: Maximum accuracy with the largest embedding space.

<video src="video/getty-optimizer-semantics.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Offline Resolving Getty ESP Terms with Local Semantics">
  ArtushVision AI - Offline Resolving Getty Terms with Local Semantics.
</video>
<p><a href="video/getty-optimizer-semantics.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## 5. Custom ESP Dictionaries, Memory & Keyword Blacklists

Teach ArtushVision AI your specific niche. Any manual keyword associations you make are remembered here for future exports.

* **Add Term**: Click to search the Getty Master Dictionary manually, select multiple terms, and apply them across your selection.
* **User Getty Dictionary**: 
  * *Quick Add:* **Right-click** any Original Word in the table and select *"Save 'word' to User Dictionary"*. Next time this word is loaded, it maps to your preferred Getty term automatically.
  * *Management:* Open the manager to manually add, delete, or wipe custom rules.
* **Personalization Blacklist (Tab 2 - Blocked Terms)**: Instantly block unwanted or repetitive Getty terms via a right-click context menu directly on any `GettyChipButton`. Blacklisted terms are written to `getty_blacklist.json`, stripped from active image memory, and completely filtered out of future processes.

<video src="video/getty-user-dictionary.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Add New Term to User Getty ESP Dictionary">
  ArtushVision AI - Add New Term to User Getty Dictionary.
</video>
<p><a href="video/getty-user-dictionary.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## 6. Final Export to Getty ESP and Global Distribution

Once your metadata is verified and your thumbnail status badges are green, choose your preferred export method:

### Option A: Precision CSV Export (For ESP Web Portal)
Generate a flawlessly formatted spreadsheet ready for the **Getty Images ESP web interface**.
1. Click **Export CSV...** and choose your preferred CSV template.
2. Go to the Getty ESP portal, upload your media files, and go to `Templates` → `Apply from CSV` → `Submit` to apply the metadata in one go.

<video src="video/getty-optimizer-apply-csv.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Apply CSV on Getty ESP">
  ArtushVision AI - Applying exported CSV to Getty ESP.
</video>
<p><a href="video/getty-optimizer-apply-csv.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

### Option B: Export JPG for Getty (Direct Metadata Embedding)
Export copies of your actual image files with Getty-optimized metadata embedded directly into the files themselves.
* **How it works:** Click **Export for Getty...** and select a destination folder. ArtushVision AI creates a folder named `YYYYMMDD-getty` (e.g., `20260624-getty`) and copies the files. It writes the Getty data into standard metadata fields (`XMP-dc`, `IPTC`, `XPKeywords`) and custom `XMP-getty` fields.
* **RAW & Video Support:** For JPEGs, data is written directly inside the file headers. For RAW formats and videos, it automatically writes to `.xmp` sidecar files to preserve original file integrity. 

---

## 7. Recommended Professional Stock Photography Workflow
Load Files ➔ Open Interactive Resolver ➔ Run Cloud AI or Offline Suggest ➔ Interactively Filter & Clean Tags ➔ Export CSV or Getty tagged JPG ➔ Upload files to ESP ➔ If You use CSV upload, apply CSV on Getty ESP.

1. **Load Your Files:** Open the Getty Optimizer module with your targeted image batch.
2. **Review Mapping Table:** Check your keyword status tags:
   * **Single Blue** = Successfully matched and OK.
   * **Multiple Blue / Orange** = Ambiguous terms requiring resolution (can be resolved manually, using AI semantic models, or a combination of both).
   * **Red** = Unknown or unrecognized keywords that need to be cleared or mapped.
3. **Navigate Interactively:** Use thumbnail filters, hover visualizers, and drag-and-drop to rapidly refine assignments. Hold **Alt/Shift** to subtract terms.
4. **Clean, Split and Check:** Double-click original words to edit typos or split phrases using a comma (`,`). Uncheck unfit terms. Check result.
5. **Save to Memory:** If you have new or unique terms not covered by the built-in master dictionary, save recurring custom keywords to your User Dictionary or blacklist unwanted ones, so they are automatically recognized or filtered next time.
6. **Export & Upload:** Generate your final **ESP-compliant CSV** or self-contained JPEGs, and complete your submission on the ESP portal!

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