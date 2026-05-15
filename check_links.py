import os
import re
import urllib.parse

def slugify_header(header_text):
    """Převede text nadpisu na markdown kotvu (např. 'Můj Nadpis!' -> 'můj-nadpis')"""
    # Odstraní formátování jako tučné písmo nebo odkazy uvnitř nadpisu
    header_text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', header_text) 
    header_text = header_text.strip().lower()
    header_text = re.sub(r'[^\w\- ]', '', header_text)
    return header_text.replace(' ', '-')

def check_links(directory):
    md_files = []
    # Najde všechny .md soubory
    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))
    
    # Předzpracuje všechny nadpisy ve všech souborech
    file_anchors = {}
    for filepath in md_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Najde všechny markdown nadpisy (začínající 1-6 hashy)
            headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
            anchors = [slugify_header(h[1]) for h in headers]
            file_anchors[filepath] = anchors
            
    broken_links = []
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    # Zkontroluje samotné odkazy
    for filepath in md_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            links = link_pattern.findall(content)
            
            for text, url in links:
                if url.startswith('http') or url.startswith('mailto:'):
                    continue # Přeskočíme externí webové odkazy
                    
                parsed_url = urllib.parse.urlparse(url)
                target_path = parsed_url.path
                anchor = parsed_url.fragment
                
                # Sestavíme absolutní cestu z relativní
                if target_path:
                    abs_target = os.path.normpath(os.path.join(os.path.dirname(filepath), urllib.parse.unquote(target_path)))
                else:
                    abs_target = filepath # Odkaz je jen kotva ve stejném souboru
                    
                # Kontrola existence souboru
                if not os.path.exists(abs_target):
                    broken_links.append(f"NENALEZEN SOUBOR: '{url}' v souboru {filepath}")
                elif anchor:
                    # Kontrola existence kotvy v souboru
                    if abs_target in file_anchors:
                        if anchor not in file_anchors[abs_target]:
                            broken_links.append(f"NENALEZENA KOTVA: '#{anchor}' v souboru {filepath} (Soubor existuje, ale chybí v něm tento nadpis)")
    
    if broken_links:
        print(f"Byl nalezen následující počet chyb {len(broken_links)}:")
        for bl in broken_links:
            print(f"- {bl}")
    else:
        print("Všechny lokální odkazy a kotvy napříč dokumentací jsou perfektně funkční! 🎉")

if __name__ == "__main__":
    check_links('.') # Spustí se v aktuálním adresáři
