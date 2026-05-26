---
title: "Advanced AI Prompting and Profile Editor | ArtushVision AI Documentation"
description: "Complete technical reference for AI variables and professional prompting in ArtushVision AI. Master dynamic EXIF, GPS, and metadata injection."
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

# Advanced AI Prompting: Ultimate Control Over Your Metadata

[← Back to ArtushVision AI Home](/index.html)

**Most AI keywording tools are black boxes, if you upload an image, and you get whatever generic keywords the developer decided you should get. ArtushVision AI flips this script entirely. Our built-in Profile Editor gives you absolute freedom to dictate exactly how the AI should "think", format, structure, and prioritize your metadata.**

Whether you need standard microstock keywords, poetic Instagram captions, or strict journalistic editorial descriptions, you can program the AI to deliver it perfectly.

---

## 1. Mode-Specific Prompting
Because every AI engine behaves differently, ArtushVision AI allows you to save completely independent prompt profiles for each Processing Mode:

* **[Cloud & Local AI](/docs/ai-metadata-generation-cloud-local-ollama.html):** Standard single-step prompts instructing the Vision model to analyze the image and return commercial JSON metadata.
* **[Hybrid & Two-Step Local AI](/docs/ai-metadata-generation-cloud-local-ollama.html):** These advanced "Agentic" pipelines use two independent prompts:
    * **Phase 1 (Vision Prompt):** Instructs the local Vision model to describe the image in raw, exhaustive detail without worrying about formatting (e.g., "Describe all subjects, lighting, colors, and atmosphere in this image...").
    * **Phase 2 (Text Prompt):** Instructs the Text-only model to take the raw description and strictly format it for SEO and microstock (using the `{local_vision_text}` variable).

---

## 2. Dynamic Context Injection (Variables)
An AI model can't guess what camera you used or where a mountain is located just by looking at a pixel grid. ArtushVision AI solves this by injecting rich, dynamic metadata directly into your prompt before it reaches the AI.

### Basic and Contextual Variables

| Variable | Description |
| :--- | :--- |
| `{local_vision_text}` | Raw text description of the image from local Ollama (Hybrid/Enhanced Local mode only). |
| `{user_hint}` | A massive time-saver. Type "Latin name: Alcedo atthis" into the top bar, and the AI will treat this as an undeniable fact, injecting it directly into your keywords. |
| `{filename}` | Filename (without extension). Great for parsing client names or project IDs. |
| `{folder_context}` | Folder name. Provides situational context. |
| `{date_info}` | The exact date the photo was taken (DD.MM.YYYY). |
| `{allowed_categories}` | Injects the list of allowed commercial categories from your Category Matrix so the AI selects the exact categories required by stock agencies. |

### [Geolocation & Maps](/docs/manual-editing-detailed-photo-view.html#geospatial-tools-and-interactive-mapping)
Never get rejected for hallucinated locations again. 

**1. Automatically generated by ArtushVision from the photo's GPS coordinates:**

| Variable | Description | Output Example |
| :--- | :--- | :--- |
| `{city}` & `{country}` | City and Country separately. | "Generate title: [Subject] in {city}, {country}." |
| `{loc_hint}` | Location from reverse geocoding. | City, State |
| `{gps_raw}` | Raw numerical coordinates. | 50.08, 14.43 |
| `{maps_link}` | Link to Google Maps. | http://googleusercontent.com/maps... |

**2. Loaded from text IPTC/XMP metadata (e.g., entered manually or by Lightroom/digiKam):**

| Variable | Description | Field Source |
| :--- | :--- | :--- |
| `{existing_location}` | Location | IPTC: Location |
| `{existing_sublocation}`| Sub-location | IPTC: Sub-location |
| `{existing_city}` | City | IPTC: City |
| `{existing_state}` | State/Province | IPTC: Province/State |
| `{existing_country}` | Country | IPTC: Country |
| `{existing_country_code}`| ISO Country Code | IPTC: Country Code |

### Technical & EXIF Parameters
Help the AI understand how the photo was taken to generate highly technical keywords.

| Variable | Description | Contextual Benefit |
| :--- | :--- | :--- |
| `{camera_model}` | Camera or Drone model from EXIF. | Let the AI know it was shot on a "DJI Mavic 3" (adds drone photography, aerial view) or a "GoPro" (adds action camera, point of view). |
| `{exposure_info}` | Time, aperture, and ISO. | Injects data like "1/2s, f/1.8, ISO 3200". The AI will deduce and add tags like long exposure, motion blur, low light, or bokeh. |
| `{aspect_ratio}` | Orientation and aspect ratio. | Injects "Landscape", "Portrait", or "Panorama", ensuring the AI adds layout tags like copy space or panoramic. |
| `{flash_used}` | Flash usage (Yes/No). | Triggering commercial tags like studio lighting or flash photography. |
| `{lens_hint}` | Lens information. | Details about the focal length and lens used. |

### Existing Metadata Preservation
Don't let the AI overwrite your manual work.

| Variable | Description | Usage Example |
| :--- | :--- | :--- |
| `{existing_keywords}` | Existing keywords loaded from the photo. | "Here are my existing tags: {existing_keywords}. Keep all of them, and suggest 20 more." |
| `{existing_title}` | Existing title loaded from the photo. | Use as a base for AI refinement. |
| `{existing_description}`| Existing description loaded from the photo. | Use as a base for AI expansion. |
| `{existing_rating}` | Photo rating (1-5 stars). | Can be used to trigger specific prompt behaviors. |

---

## 3. Professional Prompt Example
This professional-grade prompt template is optimized for high-end microstock automation. It demonstrates how to enforce strict JSON formatting, ASCII-only characters, and precise character limits.

### The Template

    USER HINT: {user_hint}
    FILENAME: {filename}
    FOLDER CONTEXT: {folder_context}
    ALLOWED CATEGORIES: {allowed_categories}
    
    TASK: Act as a professional stock photography metadata expert. Generate metadata in a valid JSON format. Use ENGLISH ONLY and ASCII characters (no diacritics, no apostrophes).
    
    1. IDENTIFICATION & PRIORITIES:
    - **USER HINT**: Absolute priority for identifying the subject.
    - **DESCRIPTION**: Factual sentence focusing on composition and concept (e.g., 'isolated on white', 'minimalist setup').
    - **CATEGORIES**: Select exactly 3 categories from the ALLOWED CATEGORIES list that best match the image. Use the EXACT string from the list.
    
    2. MICROSTOCK SALES DESCRIPTION (STRICT LIMIT):
    - **CONTENT**: Describe lighting, textures, colors, and commercial context (wellness, healthy lifestyle). Do NOT use subjective words like 'beautiful'.
    - **STRICT LENGTH CONSTRAINT**: The 'description' MUST be between 150 and 200 characters long (including spaces and punctuation). NEVER exceed 200 characters. If the text is longer, you MUST trim it to fit this range.
    
    3. FORMATTING CONSTRAINTS:
    - **NO FILLER WORDS**: Strictly avoid 'is a', 'it is', 'the', 'a'.
    - **ASCII ONLY**: No diacritics, no apostrophes (').
    
    4. KEYWORDS (STRICTLY 50 UNIQUE TERMS):
    - **EXACT COUNT**: You MUST generate EXACTLY 50 unique keywords.
    - **FORBIDDEN WORDS**: outdoor, outdoors, looking, day, daytime, sunny, summer, spring, season, unknown, none, gps, coordinate, 4k, hd, resolution, date, time, camera, lens, samsung, iphone, img_, dsc_,GoPro 13,log, video, MP4, City, Country.
    
    5. OUTPUT FORMAT (JSON):
    Return a valid JSON object:
    {
      "title": "[Subject and features]",
      "description": "[Detailed commercial factual description for microstock]",
      "keywords": ["word1", "word2", ..., "word50"],
      "categories": ["Category 1", "Category 2", "Category 3"]
    }
    
    CONSTRAINTS:
    - **HARD CHARACTER LIMIT**: The 'description' value MUST be minimum 150 and maximum 200 characters long. Any output over 200 characters is a critical failure.
    - **STRICT KEYWORD LIMIT**: Array MUST contain exactly 50 strings.
    - **GEOGRAPHY-FREE**: Omit all location data (city, country) for studio shots.
    - **STRICT ASCII FORMAT**: Use ONLY the basic 26-letter English alphabet. You MUST strip all diacritics and replace local or special characters from ANY language (e.g., ě,š,č,ř,ž,ý,á,í,é, ä,ö,ü,ß, ñ) with their plain English equivalents (e,s,c,r,z,y,a,i,e, a,o,u,ss, n). No single quotes or apostrophes.
    - **VALID JSON ONLY**: Return pure valid JSON. NO markdown formatting (do not use ```json). NO newlines, tabs, or control characters inside the string values.

---

## 4. Profile Management and Workflows
Build a library of specialized workflows to switch between different project types instantly.

* **JSON Profiles:** Save your prompts as individual .json profiles (e.g., "Wildlife Editorial", "Standard Microstock", "Instagram Reel Generator").
* **One-Click Switching:** Change your active profile in the main grid depending on the batch of photos currently being processed.
* **Category Matrix Integration:** Use the `{allowed_categories}` variable to force the AI to select exactly the categories required by your target stock agencies via the Category Matrix.

[IMAGE: A graphic showing a raw prompt template with variables on the left and the final processed text received by the AI on the right.]

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/prompt-editor-gear.png" target="_blank" class="screenshot-link" style="max-width: 500px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/prompt-editor-gear.png" alt="ArtushVision AI - AI prompt Editor Button" style="width: 500px;" class="screenshot-img">
</a>
<div style="height: 15px;"></div>


**Prompt Editor for Hybrid AI** (Two steps, Local Vision AI and Cloud AI text)
<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/local-vision-cloud-text-promt-editor.png" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/local-vision-cloud-text-promt-editor.png" alt="ArtushVision AI - Batch Edit Toolbar" width="100%" class="screenshot-img">
</a>

---

### Professional Workflow in 3 Steps:
1. **Select a Profile:** Choose the appropriate prompt template for your current batch.
2. **Add User Hints:** Enter any specific facts (like Latin names or specific events) into the Global Hint bar.
3. **Execute AI:** The application merges your technical EXIF, GPS data, and manual hints into the prompt, resulting in metadata with surgical precision.

---

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

[← Back to ArtushVision AI Home](/index.html)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*