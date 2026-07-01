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

**Eliminate submission errors and keyword rejections. ArtushVision AI ensures Near-Perfect Acceptance Rate with the Getty Images ESP system through manual or automated keyword translation and context-aware AI disambiguation.**

Uploading to Getty Images (ESP) is often challenging due to their strict Controlled Vocabulary (CV). Standard keywords used for other stock agencies are frequently rejected or mismatched by the ESP portal, leading to tedious manual corrections.

The Getty Optimizer module in ArtushVision AI solves this by acting as a professional bridge between your creative work and the technical requirements of the ESP system. You can map words **manually (100% offline)** or let the **Cloud AI** do the "heavy lifting for you".

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
* **Export ESP CSV...**: Generates a final CSV file formatted specifically for uploading metadata to the Getty Images ESP portal.
* **Export for Getty...**: Creates copies of the actual selected files (JPEGs, RAWs, or videos) in a designated directory and writes the optimized Getty Title, Description, and Keywords directly into standard metadata fields (EXIF/IPTC/XMP) using ExifTool.
* **Delete Getty Data**: Deletes the generated `getty terms` from selected files if you want to start from scratch.

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

**Getty Images Optimizer Overview in ArtushVision AI**

<video src="video/getty-optimizer-overview.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Overview of Getty Optimizer">
  ArtushVision AI - Getty Optimizer Overview.
</video>
<p><a href="video/getty-optimizer-overview.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

### Interactive Table & Color-Coded Terms

The Getty Resolver is designed to work perfectly even without an internet connection. The main table displays your original keywords on the left and the corresponding valid Getty terms (chips) on the right. Understanding the interface and color coding is key to mastering the Resolver:

1. **Original Word**: The keyword from your metadata. **Double-click** an original word to edit it in place. If you type a comma (e.g., changing "cooked food" to "cooked, food"), the Resolver will intelligently split the word into two separate rows and remap them instantly. Words marked in **red** are not recognized by the Getty dictionary and **must be unchecked** (or mapped to a valid term), otherwise Getty will reject them during submit.

2. **Getty Term (Chips)**: The mapped terms from the Getty Master Dictionary.
    * **Color Coding**:
        * **Orange Terms** (Unmapped / Unrecognized): These are custom or unrecognized terms that could not be found in the Getty master dictionary or your user mappings. The orange chip indicates a raw keyword that you can manually map, edit, delete or save to your dictionary.
        * **Blue Terms (Standard)**: These are standard, valid Getty terms successfully mapped from the master dictionary.
        * **Green Terms (AI Suggested)**: These are brand new, highly relevant terms suggested by the Cloud AI based on your photo's text context and your prompt.
        * **Purple Chips (Mixed State)**: If you select a term for *some* photos but not *all* photos in your current batch view, the chip turns **Purple**. This immediately tells you that you have customized the selection and successfully disambiguated meanings across different photos.
    * **Interaction**:
        * **Manual Selection**: You can check multiple terms at once. By default, this applies the term to *all* photos in the batch that share the original word. To apply a term to a single photo, click its thumbnail in the top panel first.
        * **Hover Context Visualizer**: Hover your mouse over any term (chip) to instantly highlight the photo thumbnails it is currently assigned to. If you hover over an *unselected* term, it will light up all photos containing that original keyword, showing you exactly where the term *can* be assigned.
        * **Drag & Drop (Assign & Remove)**: Found a perfect term and want to assign it to just one specific photo? Simply grab the chip and drag & drop it directly onto the desired photo thumbnail to instantly assign it. To **remove** a term from a specific photo, hold **Alt** (or **Shift**) while dropping the chip onto the thumbnail. 

3. **Status / Source**: This column tells you where the term came from (e.g., *Internal Dictionary*, *User Dictionary*, *Cloud Suggested*, or *Unknown*). AI suggestions will feature green text, multiple ambiguous choices will be orange, and unknown words will be red.

---
**Manual Editing in Getty Optimizer, Drag & Drop (Assign & Remove)**

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

### 5. Smart Offline Suggestions & Keyword Optimization
The **Offline Suggest** feature in Getty Resolver uses a fast, local AI semantic model (such as MiniLM or the highly accurate BGE) combined with a built-in database of official Getty Images terms. It works entirely offline on your computer, protecting your data privacy while transforming your keywording workflow in three automated steps:

* **1. Understanding the Story of Your Photos:** The AI analyzes the existing, approved keywords on your selected images to instantly understand their core theme (e.g., if it sees *snow, mountains, skis*, it automatically targets the context of *winter sports*).
* **2. Automatic Keyword Cleaning & Correction:** The system reviews your current tags and takes action based on their accuracy:
  * **Unrecognized Words & Typos:** Red-marked rows are automatically checked against the Getty database. If a close match is found that fits the theme of the photo with high accuracy ($\ge 0.70$), it’s automatically corrected and kept. Typos and completely irrelevant words are discarded.
  * **Ambiguous Meanings (Disambiguation):** If a word has multiple meanings (like *"bank"* meaning a riverbank vs. a financial institution), the AI analyzes the photo's context and automatically locks in the correct Getty definition.
* **3. Controlled Keyword Expansion:** Based on the overall theme, the AI suggests new, highly relevant Getty-approved terms that you haven't used yet (e.g., adding *Winter Sport, Alpine,* or *Slope* to your skiing photo). 

You have full control over the results: the **New AI terms** setting in the UI acts as a hard ceiling for the maximum number of new suggestions (sorted from most relevant to least), while the **Suggest Threshold** lets you fine-tune the strictness of the AI filter to ensure only pinpoint-accurate keywords make it into your final metadata table.

### 6. User Getty Dictionary & Personalization Blacklist
The **User Getty Dictionary** dialog has been upgraded to a comprehensive, multi-tabbed manager within `LearnedMappingManagerDialog` to streamline custom metadata workflows. **Tab 1 (User Dictionary)** retains full management over your custom synonyms, shortcodes, and learned mappings, ensuring specific jargon is automatically recognized. **Tab 2 (Blocked Terms)** introduces the brand-new *Getty Personalization Blacklist* functionality. This feature allows you to instantly block unwanted or repetitive Getty terms via a right-click context menu directly on any `GettyChipButton` across all 19 supported languages. Once a term is blacklisted, it is automatically written to `getty_blacklist.json`, instantly stripped from active image states in memory, and completely filtered out of future dictionary loads and optimization processes. Within the manager tab, users can easily search through blocked items, unblock specific terms ("Allow Selected"), or wipe the blacklist clean ("Allow All") to dynamically adapt the AI's vocabulary to their active production needs.

---

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

Once your metadata is verified and the blue/green/purple GETTY badges are active, you have two options for exporting your work:

### Option A: Precision CSV Export (For ESP Web Portal)
Generate a flawlessly formatted spreadsheet ready for the Getty Images ESP portal.
* **How it works:** Click **Export CSV...** and choose your preferred CSV template. It will export a `.csv` file mapping filenames to their optimized Getty tags, titles, and descriptions.
* **Uploading:** Go to the Getty ESP portal, upload your media files, and then apply the metadata in one go using the `Templates` → `Apply from CSV` option.

**Applying Exported CSV to Getty ESP** (https://esp.gettyimages.com)

Go to `Templates` → `Apply from CSV` → `Submit`

<video src="video/getty-optimizer-apply-csv.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Apply CSV on Getty ESP">
  ArtushVision AI - Applying exported CSV to Getty ESP.
</video>
<p><a href="video/getty-optimizer-apply-csv.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

### Option B: Export JPG for Getty (Direct Metadata Embedding)
Export copies of your actual image/video files with Getty-optimized metadata written directly into the files themselves.
* **How it works:** Click **Export for Getty...** and select a destination folder. ArtushVision AI creates a folder named `YYYYMMDD-getty` (e.g., `20260624-getty`) and copies the files. It then writes the Getty titles, descriptions, and keywords directly into standard metadata fields (e.g., `XMP-dc`, `IPTC`, `XPKeywords`) and custom `XMP-getty` fields.
* **RAW & Video Support:** For JPEGs, the metadata is written directly inside the file headers. For RAW formats and videos, it will automatically write to `.xmp` sidecar files (if the raw writing option is enabled in settings) to preserve the original file integrity.
* **Benefit:** The exported JPEGs are completely self-contained. You can send them directly to clients, distribute them through other channels, or archive them with their final Getty-approved metadata fully embedded.

---

## 7. Recommended Professional Workflow

### Step-by-Step Workflow
#### 1. Load Your Files
* Open the **Getty Images Export Optimizer** in the application.
* Load a single image or a batch of photos that you wish to optimize.
#### 2. Open the Interactive Resolver
* Click on **Interactive Resolver** to review the mapping table.
* The table highlights recognized terms in **Blue**, multiple alternatives in **Orange**, and unknown/unmapped words in **Red**.
#### 3. Navigate and Filter Interactively
* **Highlight Photos by Term:** Hover your mouse cursor over any Getty term chip in the table to instantly highlight the thumbnails of photos where this term is (or can be) assigned.
* **Filter Terms by Photo:** Click on any photo thumbnail to filter the table and show only the terms associated with that specific image (click again to clear the filter).
* **Drag & Drop Term Assignment:** You can drag any term chip and drop it directly onto another photo thumbnail to instantly assign it.
  * *Tip:* Hold the **Alt** or **Shift** key while dragging a term onto a thumbnail (or clicking it) to remove/deselect the term from that photo instead.
#### 4. Clean Up and Edit Keywords
* **Deselect Unfit Terms:** Simply click on any active (colored) bubble to uncheck it and remove it from your final keyword list.

* **Handling Unknown Terms:** If you encounter unfamiliar terms, you can either deselect them or leave them checked to resolve later directly in Getty, QHero, or DeepMeta. If any of these keywords match an official Getty term, you can add it to your custom Getty dictionary. During future keyword optimizations, this word will automatically be recognized as a known term.

* **Split Multi-Word Keywords:** Double-click on any original word in the left column to edit it directly or split it into individual keywords using a comma (`,`).

#### 5. Leverage Cloud AI for Disambiguation (Auto-Resolve)
* When an original keyword maps to multiple alternative Getty terms (e.g., the word *'crane'* could mean a bird, a construction machine, or a camera rig), **Cloud AI** comes to the rescue.
* Click **Run AI Resolve**:
  * The AI engine studies the visual context of your photo (using its title, description, and metadata).
  * It automatically determines the correct meaning of the keyword and selects the most accurate Getty term.
  * It can also suggest additional context-aware keywords to fill in any gaps.
#### 6. Build Your Custom Dictionary (Memory)
* If the Resolver doesn't recognize a custom term (e.g., a specific landmark, person, or brand), you can map it manually.
* Right-click the original word in the table and select **Save to User Dictionary**. The application will permanently remember this mapping and apply it automatically to all future exports.
#### 7. Export CSV or Fully-Tagged JPEGs
Choose the export method that suits your workflow:
* **For CSV upload:** Click **Export CSV...** to generate an ESP-compliant spreadsheet template.
* **For self-contained files:** Click **Export for Getty...** to export copies of your files with the Getty-optimized metadata embedded directly inside the JPEGs or as XMP sidecars.
#### 8. Upload to Getty ESP
* Upload your media files to the Getty Images ESP portal.
* Apply the exported CSV file to your batch upload according to the integration guide:
  👉 [[Applying Exported CSV to Getty ESP Guide](getty-images-esp-metadata-optimizer.html#option-a-precision-csv-export-for-esp-web-portal)]

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[⭐ User Reviews & Testimonials](/docs/artushvision-reviews.html)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*
