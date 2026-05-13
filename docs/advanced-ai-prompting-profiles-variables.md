---
title: "Advanced AI Prompting and Profile Editor | ArtushVision AI Documentation"
description: "Master advanced AI prompting with dynamic variables. Learn how to inject EXIF, GPS, and custom hints into your AI workflow for professional metadata automation."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
</style>
</div>

# Advanced AI Prompting: Ultimate Control Over Your Metadata

**Most AI keywording tools act as black boxes—you upload an image and receive generic results. ArtushVision AI provides absolute freedom to dictate exactly how the AI should think, format, and prioritize your metadata.**

The built-in Profile Editor allows you to program the AI to deliver perfect results for any niche, from standard microstock keywords to strict journalistic editorial descriptions or poetic social media captions.

[IMAGE: A screenshot of the Profile Editor window, showing a custom JSON system prompt and the Available Variables helper panel.]

---

## Mode-Specific Prompting
Different AI engines require different instructions. ArtushVision AI allows you to save independent prompt profiles for each processing mode:

* **Cloud and Local AI:** Standard single-step prompts instructing a Vision model to analyze the image and return commercial JSON metadata.
* **Hybrid and Two-Step Local AI:** These advanced agentic pipelines use two independent prompts:
    * **Phase 1 (Vision Prompt):** Instructs the local Vision model to describe the image in raw, exhaustive detail (e.g., "Describe all subjects, lighting, and atmosphere...").
    * **Phase 2 (Text Prompt):** Instructs a text-only model to take that raw description and format it into professional SEO metadata using the `{local_vision_text}` variable.

---

## Dynamic Context Injection (Variables)
An AI model cannot guess your camera settings or a specific location just by looking at pixels. ArtushVision AI solves this by injecting rich, dynamic metadata directly into your prompt via variables.

### 1. Basic and Contextual Variables
These variables provide the fundamental framework for the AI's analysis.

| Variable | Description | Usage Example |
| :--- | :--- | :--- |
| `{user_hint}` | Manual hint entered in the main window | Injecting Latin species names or specific client IDs. |
| `{filename}` | Current filename without extension | Useful if your filenames already contain project codes. |
| `{folder_context}` | Name of the parent folder | Provides situational context (e.g., "Wedding 2025"). |
| `{date_info}` | Exact capture date (DD.MM.YYYY) | Allows the AI to mention seasons or specific eras. |
| `{local_vision_text}` | Raw description from Phase 1 | Used in Phase 2 of Hybrid/Two-Step modes. |

### 2. Geolocation and Mapping
Ensure 100% geographical accuracy and prevent AI hallucinations.

**Automatically generated from GPS coordinates:**
* `{city}` and `{country}`: Isolated location names.
* `{loc_hint}`: Combined City and State/Province.
* `{gps_raw}`: Raw coordinates (e.g., 50.08, 14.43).
* `{maps_link}`: A direct link to Google Maps for the AI's reference.

**Loaded from existing IPTC/XMP metadata (e.g., from Lightroom or DigiKam):**
* `{existing_city}`, `{existing_state}`, `{existing_country}`, `{existing_country_code}`, `{existing_location}`, `{existing_sublocation}`.

### 3. Technical and EXIF Parameters
Help the AI "understand" the technical art of your photography to generate superior keywords.

* **`{camera_model}`:** Identifies the device (e.g., "DJI Mavic 3" or "GoPro"). Instruct the AI to add tags like "drone photography" or "action camera" based on this value.
* **`{exposure_info}`:** Injects shutter speed, aperture, and ISO (e.g., "1/2s, f/1.8, ISO 3200"). The AI can infer tags like "long exposure," "motion blur," or "bokeh."
* **`{aspect_ratio}`:** Detects "Landscape," "Portrait," or "Panorama." Helps the AI generate layout tags like "copy space" or "vertical."
* **`{flash_used}`:** Injects Yes/No. Essential for generating light-related tags like "studio lighting" or "flash photography."
* **`{lens_hint}`:** Provides details about the focal length and specific lens used.

### 4. Existing Metadata Preservation
Avoid overwriting manual work and command the AI to build upon it.

* `{existing_keywords}`, `{existing_title}`, `{existing_description}`, `{existing_rating}`.
* **Example Prompt:** *"Here are my existing tags: {existing_keywords}. Keep all of them and suggest 20 more commercial synonyms."*

---

## Profile Management and Workflows
Build a library of specialized workflows to switch between different project types instantly.

* **JSON Profiles:** Save your prompts as individual profiles (e.g., "Editorial News," "Microstock Standard," "Instagram Caption Generator").
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
