$terms = @{
    "ollama" = "ollama-installation-guide.md"
    "openrouter" = "cloud-ai-openrouter-api-setup.md"
    "cloud ai" = "ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path"
    "local ai" = "ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path"
    "hybrid ai" = "ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path"
    "2-pass local ai" = "ai-metadata-generation-cloud-local-ollama.md#4-tier-ai-engine-choose-your-processing-path"
    "getty images optimizer" = "getty-images-esp-metadata-optimizer.md"
    "getty optimizer" = "getty-images-esp-metadata-optimizer.md"
    "esp" = "getty-images-esp-metadata-optimizer.md"
    "master dictionary" = "getty-images-esp-metadata-optimizer.md#built-in-master-dictionary"
    "smart ftp" = "global-stock-distribution-ftp.md"
    "csv metadata" = "global-stock-distribution-ftp.md#dynamic-csv-generation-and-category-mapping"
    "category matrix" = "settings-configuration-customization.md#the-category-matrix"
    "category mapping" = "settings-configuration-customization.md#the-category-matrix"
    "smart protection" = "manual-editing-detailed-photo-view.md#advanced-protection-logic"
    "detail photo view" = "manual-editing-detailed-photo-view.md"
    "manual editing" = "manual-editing-detailed-photo-view.md"
    "ai profiles" = "advanced-ai-prompting-profiles-variables.md"
    "batch operations" = "batch-operations-metadata-library-management.md"
    "visual culling" = "smart-manual-keywording-batch-editing.md#visual-culling-ratings-flags-and-color-labels"
    "smart grid" = "smart-grid-filters-search-metadata-management.md"
    "local model manager" = "local-ai-model-manager-ollama.md"
    "face tags" = "manual-editing-detailed-photo-view.md"
    "semantic ai disambiguation" = "getty-images-esp-metadata-optimizer.md#interactive-ai-resolver-and-disambiguation"
    "dynamic variables" = "advanced-ai-prompting-profiles-variables.md#basic-and-contextual-variables"
    "multilingual spell check" = "manual-editing-detailed-photo-view.md#linguistic-intelligence-and-translation-tools"
    "interactive map" = "manual-editing-detailed-photo-view.md#geospatial-tools-and-interactive-mapping"
    "spellcheck" = "smart-manual-keywording-batch-editing.md#multi-language-spellcheck-and-auto-corrections"
    "reverse geocoding" = "settings-configuration-customization.md#maps-and-reverse-geocoding"
}

$keys = $terms.Keys | Sort-Object Length -Descending
$escapedKeys = $keys | ForEach-Object { [regex]::Escape($_) }
$termRegex = "\b(" + ($escapedKeys -join "|") + ")\b"
$unifiedPattern = New-Object System.Text.RegularExpressions.Regex($termRegex, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)

$regexStr = '(?m)(\A---[\s\S]*?^---|```[\s\S]*?```|`[^`]*`|<a\b[^>]*>[\s\S]*?<\/a>|\[[^\]]*\]\([^\)]*\)|<[^>]*>|^#+\s.*$)'
$blockPattern = New-Object System.Text.RegularExpressions.Regex($regexStr)

function Process-File {
    param([string]$FilePath, [bool]$IsRoot)
    $text = [IO.File]::ReadAllText($FilePath, [Text.Encoding]::UTF8)
    
    $segments = $blockPattern.Split($text)
    
    for ($i = 0; $i -lt $segments.Count; $i++) {
        if ($i % 2 -eq 0) {
            $segments[$i] = $unifiedPattern.Replace($segments[$i], [System.Text.RegularExpressions.MatchEvaluator] {
                param([System.Text.RegularExpressions.Match]$match)
                $orig = $match.Groups[1].Value
                $lower = $orig.ToLower()
                $link = $terms[$lower]
                $target = if ($IsRoot) { "docs/$link" } else { $link }
                return "[$orig]($target)"
            })
        }
    }
    
    $newText = $segments -join ""
    if ($newText -cne $text) {
        [IO.File]::WriteAllText($FilePath, $newText, [System.Text.UTF8Encoding]::new($false))
        Write-Host "Updated $FilePath"
    }
}

Process-File -FilePath "index.md" -IsRoot $true

Get-ChildItem -Path "docs" -Filter "*.md" | ForEach-Object {
    Process-File -FilePath $_.FullName -IsRoot $false
}
