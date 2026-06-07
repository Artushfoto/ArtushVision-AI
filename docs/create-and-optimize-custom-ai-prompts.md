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

# How to Create and Optimize Custom AI Prompts for ArtushVision

[← Back to ArtushVision AI Home](/index.html)

Creating the perfect AI prompt for generating stock photography metadata can be challenging. Fortunately, you don't have to write it from scratch! You can use advanced chatbots like **ChatGPT, Claude, or Gemini** to act as your personal "Prompt Engineer."

By providing the chatbot with our default baseline template, a list of available variables, and your specific photography niche, the AI will generate a highly optimized prompt tailored specifically for your workflow.

---

## The "Meta-Prompt" Strategy (Copy & Paste)

Copy the entire block blockquote below, fill in your specific requirements at the bottom, and paste it into your favorite chatbot. 

> **Role:** Act as an expert AI Prompt Engineer specializing in microstock photography metadata and SEO optimization.
> 
> **Context:** I am using a desktop application called ArtushVision to automatically analyze my photos and generate titles, descriptions, and 50 keywords. The application uses a System Prompt to instruct the AI (like Gemini, Claude, or local Ollama models) on how to analyze the image and return a strict JSON object.
> 
> **Available Variables:**
> The application dynamically injects real data into the prompt using the following `{variables}`. You must strategically place them in the prompt you create for me:
> - `{user_hint}`: A custom hint I provide before analysis (e.g., specific animal species, location name).
> - `{filename}`, `{folder_context}`: File and folder names for context.
> - `{date_info}`: The capture date.
> - `{city}`, `{country}`, `{loc_hint}`: Geographic data extracted automatically from GPS.
> - `{camera_model}`, `{lens_hint}`, `{exposure_info}`, `{aspect_ratio}`, `{flash_used}`: Technical EXIF data (useful for generating photography-specific tags like "long exposure", "bokeh", "drone photography").
> - `{allowed_categories}`: A list of strict categories the AI must choose from.
> - `{local_vision_text}`: *(Only for two-step Local/Hybrid models)* A raw text description of the image generated in Phase 1.
> 
> **The Default Baseline Prompt:**
> ```text
> Analyze the image and generate stock photography metadata. Return ONLY a valid JSON object.
> 
> Context:
> Date: {date_info}
> Location: {loc_hint} ({city}, {country})
> User Hint: {user_hint}
> Technical: {camera_model}, {exposure_info}, {aspect_ratio}
> 
> Instructions:
> 1. "title": A short, descriptive title (STRICT LIMIT: MAXIMUM 200 CHARACTERS).
> 2. "description": Describe the visual content. You MUST include the location ({loc_hint}) and the date ({date_info}). STRICT LIMIT: MAXIMUM 200 CHARACTERS.
> 3. "keywords": Generate EXACTLY 50 unique keywords. To reach 50, you MUST categorize your thinking: include 10 literal objects, 10 colors/lighting terms, 10 background elements, 10 location/nature terms, and 10 abstract concepts/emotions. DO NOT STOP early.
> 
> JSON Structure:
> {"title": "...", "description": "...", "keywords": ["...", "..."]}
> ```
> 
> **My Request:**
> Please rewrite and optimize this prompt for my specific use case. 
> 
> **1. My Niche/Goal:** [INSERT YOUR NICHE HERE - e.g., "I shoot high-end culinary and food photography. I need keywords focused on taste, ingredients, dietary trends (vegan, keto), and lighting/mood."]
> **2. Target Engine:** [INSERT ENGINE TYPE - e.g., "Cloud AI" OR "Local/Hybrid AI"]
> *(Note to chatbot: If the target is Cloud AI, provide one unified prompt. If the target is Local/Hybrid AI, I need TWO prompts: Phase 1 (Vision) asking only for a highly detailed raw text description of the image, and Phase 2 (Text) asking to format `{local_vision_text}` and the other variables into the final JSON).*
> 
> Return the optimized prompt(s) ready to be copy-pasted into the software. Ensure the strict JSON formatting instructions remain intact!

---

## Understanding the Engines (Cloud vs. Local)

When generating your prompt, it's crucial to tell the chatbot which AI engine you are using, as their architecture differs:

### 1. Cloud AI (OpenRouter)
Cloud models (like Gemini 2.5, Claude 3.5 Sonnet) are massive and incredibly smart. They can "look" at the image and format it into a perfect JSON structure all in a single step. 
* **You need:** 1 unified prompt.

### 2. Local AI & Hybrid AI (Ollama)
Small local models (running on your GPU) often struggle to both accurately describe an image *and* format complex JSON simultaneously. ArtushVision solves this by splitting the task into two phases:
* **Phase 1 (Vision Prompt):** The model only acts as an "eye". It looks at the image and writes a massive, chaotic paragraph of raw text describing everything it sees. **Do not ask for JSON here.**
* **Phase 2 (Text Prompt):** A language model takes that raw text (injected via the `{local_vision_text}` variable) alongside your GPS/EXIF data, and formats it into the clean, 50-keyword JSON object.

---

## Implementing Your New Prompt

Once ChatGPT/Claude/Gemini generates your optimized prompt:

1. Open **ArtushVision AI**.
2. Click the **⚙ Profile Editor** (gear icon) in the top toolbar.
3. Click the **➕ New** button to create a blank profile.
4. Paste the generated prompt into the **System Prompt** text area (if using Local/Hybrid, paste the Phase 1 and Phase 2 prompts into their respective fields).
5. Ensure the **AI Model** field points to your desired model (e.g., `google/gemini-2.5-flash-lite` for Cloud, or `qwen2.5-vl:3b` for Local).
6. Click **Save** and give your new profile a descriptive name (e.g., `Food_Photography_Pro.json`).

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

[← Back to ArtushVision AI Home](/index.html)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*