---
title: "Smart Manual Keywording and Culling | ArtushVision AI"
description: "Master manual metadata curation and visual culling in ArtushVision AI. Experience real-time tag bubbles, drag-and-drop mechanics, and lightning-fast sorting and culling."
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

# Smart Manual Keywording and Culling: Ultimate Control at Lightning Speed

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**While our AI engines do the heavy lifting, professional stock contributors know that manual curation is the key to a perfect portfolio. Whether you are adding a highly specific local location, fixing a typo, sorting out the best shots, or copying tags across a series of photos, ArtushVision AI provides a desktop-class editing experience that web browsers simply cannot match.**

Forget clumsy text boxes and constant reloading. Experience real-time tagging, spellchecking, seamless drag-and-drop mechanics, and lightning-fast culling.

[IMAGE: A close-up of the main grid showing the Visual Bubbles mode for keywords, with one tag being dragged and dropped onto an adjacent photo, and a 5-star rating highlighted under the thumbnail.]

---

## Visual Tag Bubbles and Seamless Drag-and-Drop

Transform your raw comma-separated text into interactive, colorful Tag Bubbles.

* **Reorder on the Fly:** Simply click and drag a bubble to change the order of your keywords.
* **Cross-Photo Drag and Drop:** Need a specific keyword on another photo? Grab the bubble and drop it onto any other image in the grid.
* **Multi-Select Dragging:** Hold Ctrl to select multiple bubbles at once, then drag the entire batch to instantly apply them to another photo.

* **Add a keyword to multiple photos** Select multiple photos (using `Ctrl` + `Click`) and type a keyword to apply it to all selected images in bulk.

* **Auto-Deduplication:** The application automatically prevents duplicate tags. If a photo already has the tag, it will smoothly ignore the dropped duplicate.

<video src="video/ seamless-drag-and-drop.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Seamless Drag and Drop Demonstration" aria-label="Video showing seamless drag and drop metadata editing in ArtushVision AI">
  ArtushVision AI - Demonstration of seamless metadata drag and drop editing.
</video>
<p><a href="video/ seamless-drag-and-drop.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## Smart Batch Editing and Copy-Paste

When you need to edit 500 photos at once, traditional copy-pasting is too dangerous—you risk overwriting unique tags.

* **Smart Append Sync:** Select 50 photos in the grid. Type a new keyword into one of them. ArtushVision AI intelligently appends that new word to all 50 photos in real-time without destroying their existing, unique tags.
* **Universal Copy/Paste:** Use standard Ctrl+C and Ctrl+V. If you paste a string of 20 keywords into a selection of photos, the application distributes them cleanly, removes duplicates, and immediately formats them into bubbles.
* **Visual Undo/Redo:** Made a mistake while mass-editing or rating? Press Ctrl+Z. The application remembers the exact state (including the specific tag colors, ratings, and flags) of your entire batch before the edit and restores it instantly.

**Select the photo widget**, press **CTRL+C**, and select the photos where you want to paste **(CTRL+V)** the copied metadata.**

<video src="video/copy-paste-metadata.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Copy and paste metadata in ArtushVision AI" aria-label="Video showing copy and paste metadata in ArtushVision AI">
  ArtushVision AI - Demonstration of seamless metadata drag and drop editing.
</video>
<p><a href="video/copy-paste-metadata.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

---

## Bulk Delete Keywords in ArtushVision

ArtushVision offers several ways to bulk delete keywords depending on what exactly you need to achieve.

## Delete Specific Keywords from Multiple Photos
*Use this method if you want to remove only certain words while keeping the rest of the tags intact.*

**Method A: Using Grid Bubbles (Fastest)**
1. Select multiple photos in the grid (you can click one and press `Ctrl + A` to select all).
2. Locate the specific keyword bubble you want to remove in any of the selected photos.
3. Click the **'×'** (delete) icon on that bubble. 
> **Result:** The keyword will be instantly and intelligently removed from *all* selected photos that contain it.

**Method B: Using the Batch Edit Panel**
1. Select the affected photos.
2. Open the **Batch Edit** panel (click the checklist icon in the top filter bar if it's not visible).
3. In the *"Batch edit:"* dropdown menu, select **Keywords**.
4. Type the exact keyword you want to delete into the text field.
5. Click the **"- Remove"** button.

## Clear All Keywords (Start Fresh)
*Use this method if you want to completely erase the Keywords field for the selected photos and run the AI again.*

**Method A: Using the Context Menu**
1. Select the photos in the grid.
2. **Right-click** anywhere on your selection.
3. Choose **"Clear keywords (selection)"** from the context menu.

**Method B: Using the Batch Edit Panel**
1. Select the photos and open the **Batch Edit** panel.
2. Select **Keywords** from the dropdown menu.
3. Click the **"⌫ Clear Field"** button.

---

### Pro Tip: Made a Mistake? Restore Original Data!
If you accidentally deleted the wrong keywords and **haven't clicked the "Save" button yet**, you can easily revert your photos to their original state:

* Select the affected photos, **right-click** them, and choose **"Restore original from disk (selection)"**.
* *Alternatively*, click the **"⟲ Restore from Backup"** button located in the bottom toolbar.

---

### Keyword Sets (Presets)

ArtushVision AI offers a powerful **Keyword Sets (Presets)** feature that significantly speeds up routine photo tagging. Instead of repeatedly typing the same expressions, you can save frequently used combinations of tags (e.g., for specific locations, studio shoots, or animal species) as named sets. Using the built-in **Sets Editor**, you can easily create, manage, and modify these presets as needed.

<video src="video/keyword-sets.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Using Keyword Sets in ArtushVision AI" aria-label="How to use Keyword Set in ArtushVision AI">
  ArtushVision AI - Demonstration of seamless metadata drag and drop editing.
</video>
<p><a href="video/keyword-sets.mp4" target="_blank" style="font-size: 0.9em;">Open video in full size</a></p>

The feature is fully integrated into your workflow and is available across the entire application:
* **In the main grid:** You can apply sets in bulk to any number of selected photos – just use the context menu (right-click) or the *Sets* button on the bottom batch edit bar.
* **In the detail window:** During focused editing of a specific photo, you have instant access to presets via a special icon directly in the header of the Keywords section.

<div style="display: flex; gap: 20px; align-items: flex-start; flex-wrap: wrap; margin-top: 15px;">
  <a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/keyword-set.png" target="_blank" class="screenshot-link" style="margin: 0; max-width: 150px; flex: 0 0 auto;">
    <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/keyword-set.png" alt="ArtushVision AI - Predefined Keyword Sets" style="width: 150px;" class="screenshot-img">
  </a>
  <a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/keyword-set-editor.png" target="_blank" class="screenshot-link" style="margin: 0; max-width: 600px; flex: 1 1 auto;">
    <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/keyword-set-editor.png" alt="ArtushVision AI - Keyword Sets Editor" style="width: 100%; max-width: 600px;" class="screenshot-img">
  </a>
</div>
<div style="height: 15px;"></div>

*Smart insertion: Applying a set works non-destructively. The application compares your existing tags on the photo with the preset and adds only the missing words (automatic deduplication). Furthermore, the new words are immediately colored green (indicating manual addition) and undergo instant spell checking.*

---

## Visual Culling: Ratings, Flags and Color Labels

Organizing a massive photoshoot requires speed. ArtushVision AI features a complete visual rating system built right into the grid, allowing you to cull your photos without taking your hands off the keyboard.

* **Keyboard Shortcuts:** Instantly rate photos using keys 1-5, apply Pick/Reject flags using P and X (or U to unflag), and assign color labels with keys 6-9.
* **Batch Culling:** Select 100 photos and press 5 to rate them all as 5-star instantly.
* **[100% Lightroom , digiKam and Zoner Compatible:](/docs/metadata-compatibility-and-file-handling.html#seamless-adobe-lightroom-and-other-photo-management-software-compatibility)** Your ratings, flags, and color labels are natively written into <a href="/docs/metadata-compatibility-and-file-handling.html">EXIF/XMP sidecars</a>. If you rate a photo in ArtushVision AI, the 5 stars will flawlessly appear in Adobe Lightroom, digiKam, ACDSee, and Zoner Photo Studio.

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/visual-culling.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/visual-culling.png" alt="ArtushVision AI - Visual Culling" width="100%" class="screenshot-img">
</a>

---

### Field Limits & Validation

To ensure your metadata and files meet the strict requirements of various stock photography agencies, ArtushVision AI includes a comprehensive **Limits** monitoring system. By configuring these limits in the Settings menu, you can maintain full control over the length and volume of your metadata. You can define specific thresholds for:

*   **Title Length:** Set the minimum and maximum allowed character count for the title.
*   **Description Length:** Set the minimum and maximum allowed character count for the description.
*   **Keywords Count:** Define the required minimum and maximum number of keywords (e.g., min 5, max 50).
*   **Resolution Limit (Megapixels):** Specify a minimum megapixel count to quickly identify images that are too small and might be rejected by agencies.


When the **Enable Validation** feature is active, the application continuously checks your data in real-time. Any field or image falling outside your defined limits will be instantly highlighted with an error color (default red) in both the grid and the detail view. This provides immediate visual feedback, preventing you from uploading incomplete or non-compliant files. You can also fully customize the error highlight color separately for both Light and Dark themes to suit your preferences.

Go to `Top Menu` → `File` → `Settings` → `Field Limits`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/field-limits-settings.png" target="_blank" class="screenshot-link" style="max-width: 300px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/field-limits-settings.png" alt="ArtushVision AI - Versatile AI - Field limit settings" style="width: 300px;" class="screenshot-img">
</a>

---

## Lightning-Fast Autocomplete (Type Ahead)

Stop typing the same words over and over. As you type, the Smart Autocomplete instantly suggests the best matches from an ultra-fast, pre-warmed database of over 300,000 highly commercial words.

* **Smart Formatting:** Press Enter to accept a suggestion, and the application will automatically add a comma, a space, and turn it into a bubble.
* **Case Preservation:** If you start typing with a capital letter, the autocomplete will respect your formatting (e.g., typing "Lon" will suggest "London", not "london").

[IMAGE: A screenshot of a user typing in the Keywords field, showing the autocomplete dropdown menu suggesting words, and a typo underlined in red.]

---

## Multi-Language Spellcheck and Auto-Corrections

Never get a batch rejected for a typo again. ArtushVision AI features a robust, offline-first spellchecking engine.

* **Dual-Language Support:** Do you shoot local events but tag in English? Set a Primary (e.g., English) and a Secondary language (e.g., Czech or German). The application will validate against both dictionaries simultaneously, so local names are no longer flagged as errors.
* **Quick Fixes:** Right-click any red-underlined word to open the context menu. The <a href="/docs/ai-metadata-generation-cloud-local-ollama.html#4-tier-ai-engine-choose-your-processing-path">Cloud AI</a> will instantly suggest the best spelling corrections, complete with your native language translation in brackets.
* **User Dictionary:** Teach the application your specific client names or locations. Add a custom word to your **Personal Dictionary** with one click, and the app will instantly clear the error across your entire portfolio.

Go to `Top Menu` → `File` → `Settings` → `Language and AI`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/language-and-ai.png" target="_blank" class="screenshot-link" style="max-width: 400px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/language-and-ai.png" alt="ArtushVision AI - Versatile AI - Field limit settings" style="width: 400px;" class="screenshot-img">
</a>

---

## Interactive Synonym Explorer

Struggling to find the right word? Double-click any tag (or right-click and select Synonyms) to open the Interactive Synonym Dialog.

* **Cloud-Powered Vocabulary:** Powered by the Datamuse API, the application pulls dozens of highly relevant synonyms, related concepts, and associations.
* **Meaning and Definitions:** Hover over any suggested synonym to instantly see its dictionary definition and native translation.
* **"Did you mean?":** If you open the dialog on a misspelled word, it prominently displays a section with the correct spelling alternatives.

**Interactive Synonym Dialog**

Right Nouse Click → `Keyword`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/synonyms.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/synonyms.png" alt="ArtushVision AI - Interactive Synonym Dialog" width="100%" class="screenshot-img">
</a>

---

### Master Your Workflow in 3 Steps:

1. **Cull and Sort:** Rapidly go through your grid using keyboard shortcuts (1-5, P, X) to rate and flag the best photos for microstock submission.
2. **Type and Tab:** Use the intelligent autocomplete to rapidly build your base tags, tabbing smoothly between the <a href="/docs/manual-editing-detailed-photo-view.html#title-and-description-editor">Title, Description, and Keywords fields</a>.
3. **Drag and Drop:** Visually distribute specialized tags between photos by dragging the bubbles, and select the rest of the overarching themes everywhere instantly (see the <a href="/docs/global-stock-distribution-ftp.html">Smart FTP Uploader</a>).

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