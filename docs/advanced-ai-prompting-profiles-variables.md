---
title: "Advanced AI Prompting and Profile Editor | ArtushVision AI Documentation"
description: "Complete technical reference for AI variables and professional prompting in ArtushVision AI. Master dynamic EXIF, GPS, and metadata injection."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
</style>
</div>

# Advanced AI Prompting: Ultimate Control Over Your Metadata

**Most AI keywording tools are black boxes—you upload an image and get generic results. ArtushVision AI flips this script by giving you absolute freedom to dictate exactly how the AI should think, format, structure, and prioritize your metadata.**

The built-in Profile Editor allows you to program the AI for any specific niche, whether you need standard microstock keywords, poetic social media captions, or strict journalistic editorial descriptions.

---

## 1. Mode-Specific Prompting
Because every AI engine behaves differently, ArtushVision AI allows you to save independent prompt profiles for each Processing Mode:

* **Cloud & Local AI:** Standard single-step prompts instructing the Vision model to analyze the image and return commercial JSON metadata.
* **Hybrid & Two-Step Local AI:** These advanced "Agentic" pipelines use two independent prompts:
    * **Phase 1 (Vision Prompt):** Instructs the local Vision model to describe the image in raw detail.
    * **Phase 2 (Text Prompt):** Instructs a text-only model to take that description and strictly format it for SEO using the `{local_vision_text}` variable.

---

## 2. Dynamic Variables Reference
Variables allow the application to inject real-world data from your files directly into the AI prompt. This ensures the AI has 100% accurate background context.

### Basic and Contextual Variables
| Variable | Description | Usage Example |
| :--- | :--- | :--- |
| `{local_vision_text}` | Raw text description of the image from the local Vision model. | Used in Phase 2 of Hybrid or Two-Step modes. |
| `{user_hint}` | Text entered in the Global Hint bar of the main window. | Specific subjects like Latin names or client IDs. |
| `{filename}` | Filename of the asset without its extension. | Useful if filenames contain project codes. |
| `{folder_context}` | Name of the parent folder. | Provides project-level context (e.g., "Wedding_2025"). |
| `{date_info}` | The exact capture date in DD.MM.YYYY format. | Injects temporal context for the AI. |
| `{allowed_categories}` | List of categories defined in your Category Matrix. | Ensures the AI picks from your commercial niche. |

### Geolocation Variables (Automatic)
These are generated via reverse geocoding from the photo's GPS coordinates.
| Variable | Description | Output Example |
| :--- | :--- | :--- |
| `{city}` | The detected city name. | "Prague" |
| `{country}` | The detected country name. | "Czech Republic" |
| `{loc_hint}` | Combined City and State/Province. | "Jihlava, Vysočina" |
| `{gps_raw}` | Raw numerical coordinates. | "50.08, 14.43" |
| `{maps_link}` | Direct URL to the location on Google Maps. | https://www.google.com/maps/... |

### Geolocation Variables (Existing IPTC)
Loaded from existing text metadata (manually entered or from software like Lightroom).
| Variable | Description | Field Source |
| :--- | :--- | :--- |
| `{existing_location}` | Specific location name. | IPTC: Location |
| `{existing_sublocation}` | Specific sub-location. | IPTC: Sub-location |
| `{existing_city}` | City name. | IPTC: City |
| `{existing_state}` | State or Province. | IPTC: Province/State |
| `{existing_country}` | Full country name. | IPTC: Country |
| `{existing_country_code}` | ISO Country Code. | IPTC: Country Code |

### Technical and EXIF Parameters
Technical data helps the AI infer professional photography tags.
| Variable | Description | Contextual Benefit |
| :--- | :--- | :--- |
| `{camera_model}` | Camera or Drone model (e.g., "DJI Mavic 3"). | Triggers tags like "aerial view" or "drone photography". |
| `{exposure_info}` | Shutter, aperture, and ISO (e.g., "1/2s, f/1.8"). | Infers tags like "long exposure" or "bokeh". |
| `{aspect_ratio}` | Detects orientation (Landscape, Portrait, etc.). | Infers tags like "panoramic" or "copy space". |
| `{flash_used}` | Injects Yes/No status. | Triggers "studio lighting" or "flash photography". |
| `{lens_hint}` | Technical lens info from EXIF. | Identifies wide-angle or telephoto perspective. |

### Metadata Preservation
Use these to command the AI to build upon your existing manual work.
| Variable | Description | Usage Example |
| :--- | :--- | :--- |
| `{existing_keywords}` | Keywords currently saved in the file or XMP. | "Add 20 synonyms to {existing_keywords}." |
| `{existing_title}` | Current title loaded from the photo. | "Refine this title: {existing_title}." |
| `{existing_description}` | Current description loaded from the photo. | "Expand this description: {existing_description}." |
| `{existing_rating}` | Photo rating (1-5 stars). | Prioritizes processing for high-rated shots. |

---

## 3. Professional Prompt Example
This professional-grade prompt template is optimized for high-end microstock automation. It demonstrates how to enforce strict JSON formatting, ASCII-only characters, and precise character limits.

### The Template
```text
USER HINT: {user_hint}
FILENAME: {filename}
FOLDER CONTEXT: {folder_context}
ALLOWED CATEGORIES: {allowed_categories}

TASK: Act as a professional stock photography metadata expert. Generate metadata in a valid JSON format. Use ENGLISH ONLY and ASCII characters (no diacritics, no apostrophes).

1. IDENTIFICATION & PRIORITIES:
- USER HINT: Absolute priority for identifying the subject.
- DESCRIPTION: Factual sentence focusing on composition and concept (e.g., 'isolated on white', 'minimalist setup').
- CATEGORIES: Select exactly 3 categories from the ALLOWED CATEGORIES list that best match the image. Use the EXACT string from the list.

2. MICROSTOCK SALES DESCRIPTION (STRICT LIMIT):
- CONTENT: Describe lighting, textures, colors, and commercial context (wellness, healthy lifestyle). Do NOT use subjective words like 'beautiful'.
- STRICT LENGTH CONSTRAINT: The 'description' MUST be between 150 and 200 characters long (including spaces and punctuation). NEVER exceed 200 characters. If the text is longer, you MUST trim it to fit this range.

3. FORMATTING CONSTRAINTS:
- NO FILLER WORDS: Strictly avoid 'is a', 'it is', 'the', 'a'.
- ASCII ONLY: No diacritics, no apostrophes (').

4. KEYWORDS (STRICTLY 50 UNIQUE TERMS):
- EXACT COUNT: You MUST generate EXACTLY 50 unique keywords.
- FORBIDDEN WORDS: outdoor, outdoors, looking, day, daytime, sunny, summer, spring, season, unknown, none, gps, coordinate, 4k, hd, resolution, date, time, camera, lens, samsung, iphone, img_, dsc_, GoPro 13, log, video, MP4, City, Country.

5. OUTPUT FORMAT (JSON):
Return a valid JSON object:
{
  "title": "[Subject and features]",
  "description": "[Detailed commercial factual description for microstock]",
  "keywords": ["word1", "word2", ..., "word50"],
  "categories": ["Category 1", "Category 2", "Category 3"]
}

CONSTRAINTS:
- HARD CHARACTER LIMIT: The 'description' value MUST be minimum 150 and maximum 200 characters long. Any output over 200 characters is a critical failure.
- STRICT KEYWORD LIMIT: Array MUST contain exactly 50 strings.
- GEOGRAPHY-FREE: Omit all location data (city, country) for studio shots.
- STRICT ASCII FORMAT: Use ONLY the basic 26-letter English alphabet. Strip all diacritics (e.g., replace é with e, š with s). No single quotes or apostrophes.
- VALID JSON ONLY: Return pure valid JSON. NO markdown formatting. NO newlines, tabs, or control characters inside the string values.

---

## Profile Management and Workflows
Build a library of specialized workflows to switch between different project types instantly.

* **JSON Profiles:** Save your prompts as individual profiles (e.g., "Editorial ," "Microstock Standard," "Instagram Caption Generator").
* **One-Click Switching:** Change your active profile in the main grid depending on the batch of photos currently being processed.
* **Category Matrix Integration:** Use the `{allowed_categories}` variable to force the AI to select exactly the categories required by your target stock agencies.

[IMAGE: A graphic showing a raw prompt template with variables on the left and the final processed text received by the AI on the right.]

---

### Professional Workflow in 3 Steps:
1.  **Select a Profile:** Choose the appropriate prompt template for your current batch.
2.  **Add User Hints:** Enter any specific facts (like Latin names or specific events) into the Global Hint bar.
3.  **Execute AI:** The application merges your technical EXIF, GPS data, and manual hints into the prompt, resulting in metadata with surgical precision.

---

### [Get Started Now]
* [Download Free Lite Version](https://www.artushfoto.eu/Software/Download-ArtushVision-AI)
* [Purchase Lifetime License - $39.99](https://www.artushfoto.eu/Software/Purchase-ArtushVision-AI)

---
*ArtushVision AI - Absolute control over AI behavior for professional media creators.*
<!--stackedit_data:
eyJoaXN0b3J5IjpbODUyNjE0NDMyLDE5NzUyNjQzNTZdfQ==
-->