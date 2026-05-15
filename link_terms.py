import re
import os
import glob

terms = {
    "Ollama": "ollama-installation-guide.md",
    "OpenRouter": "cloud-ai-openrouter-api-setup.md",
    "Cloud AI": "ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path",
    "Local AI": "ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path",
    "Hybrid AI": "ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path",
    "2-Pass Local AI": "ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path",
    "Getty Images Optimizer": "getty-images-esp-metadata-optimizer.md",
    "Getty Optimizer": "getty-images-esp-metadata-optimizer.md",
    "ESP": "getty-images-esp-metadata-optimizer.md",
    "Master Dictionary": "getty-images-esp-metadata-optimizer.md#built-in-master-dictionary",
    "Smart FTP": "global-stock-distribution-ftp.md",
    "CSV Metadata": "global-stock-distribution-ftp.md#dynamic-csv-generation-and-category-mapping",
    "Category Matrix": "settings-configuration-customization.md#the-category-matrix",
    "Category Mapping": "settings-configuration-customization.md#the-category-matrix",
    "Smart Protection": "manual-editing-detailed-photo-view.md#advanced-protection-logic",
    "Detail Photo View": "manual-editing-detailed-photo-view.md",
    "Manual Editing": "manual-editing-detailed-photo-view.md",
    "AI Profiles": "advanced-ai-prompting-profiles-variables.md",
    "Batch Operations": "batch-operations-metadata-library-management.md",
    "Visual Culling": "smart-manual-keywording-batch-editing.md#visual-culling-ratings-flags-and-color-labels",
    "Smart Grid": "smart-grid-filters-search-metadata-management.md",
    "Local Model Manager": "local-ai-model-manager-ollama.md",
    "Face Tags": "manual-editing-detailed-photo-view.md",
    "Semantic AI Disambiguation": "getty-images-esp-metadata-optimizer.md#interactive-ai-resolver-and-disambiguation",
    "Dynamic Variables": "advanced-ai-prompting-profiles-variables.md#basic-and-contextual-variables",
    "Multilingual Spell Check": "manual-editing-detailed-photo-view.md#linguistic-intelligence-and-translation-tools",
    "Interactive Map": "manual-editing-detailed-photo-view.md#geospatial-tools-and-interactive-mapping",
    "Spellcheck": "smart-manual-keywording-batch-editing.md#multi-language-spellcheck-and-auto-corrections",
    "Reverse Geocoding": "settings-configuration-customization.md#maps-and-reverse-geocoding"
}

# Normalize terms to lower case for easy lookup in case-insensitive match
terms_lower = {k.lower(): v for k, v in terms.items()}

# Sort keys by length descending to match longest first
sorted_keys = sorted(terms_lower.keys(), key=len, reverse=True)

# Build a single regex pattern for all terms
terms_pattern_str = "|".join(re.escape(k) for k in sorted_keys)
unified_pattern = re.compile(r'\b(' + terms_pattern_str + r')\b', re.IGNORECASE)

def process_file(filepath, is_root):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Block pattern to avoid modifying frontmatter, code, links, html, or headers
    # Adding ^[ \t]*[-*] .*$ to not mess up list items with links entirely? No, we CAN replace in list items.
    block_pattern = re.compile(r'(^---.*?^---|```.*?```|`[^`]*`|\[[^\]]*\]\([^\)]*\)|<[^>]*>|^#+\s.*$)', re.MULTILINE | re.DOTALL)
    
    segments = block_pattern.split(text)
    
    for i in range(len(segments)):
        if i % 2 == 0: # Normal text
            def repl(match):
                original_text = match.group(1)
                term_lower = original_text.lower()
                link = terms_lower[term_lower]
                target_link = f"docs/{link}" if is_root else link
                return f"[{original_text}]({target_link})"
                
            segments[i] = unified_pattern.sub(repl, segments[i])

    new_text = "".join(segments)
    
    if new_text != text:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Updated {filepath}")

print("Processing index.md...")
process_file("index.md", is_root=True)

print("Processing docs/*.md...")
for file in glob.glob("docs/*.md"):
    process_file(file, is_root=False)

print("Done.")
