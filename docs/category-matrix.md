---
title: "Smart Category Mapping | ArtushVision AI"
description: "Master Categories in ArtushVision AI. Experience real-time tag bubbles, drag-and-drop mechanics, and lightning-fast sorting and culling."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
</style>
</div>

# Category Mapping Matrix

The **Category Mapping Matrix** is a powerful feature designed to eliminate the tedious task of manually assigning different categories for each individual stock photo agency. Since every agency (Adobe Stock, Shutterstock, Alamy, etc.) uses its own unique category names or ID numbers, ArtushVision AI uses a "Master Category" system to unify them.

You only need to assign a category once, and the application will automatically translate it into the correct format for every agency during the CSV export or FTP upload.

## Category Matrix Editor
You can access the editor by going to **Settings -> Configuration Management -> Category Mapping Matrix...**.
In this editor, you can define exactly how your Master categories map to specific agencies. 

*   **Master Category:** Usually based on the Dreamstime category system (which is very detailed). This is the category you (or the AI) will assign to the photo.
*   **Agency Columns:** You can map the Master category to corresponding categories for Adobe Stock, Shutterstock, Pond5, Alamy, and Motion Elements.
*   **Customization:** You can add new rows, delete them, or add entirely new columns if you start contributing to a new agency.
*   **Smart Split:** For **Motion Elements**, the matrix even distinguishes between `ME Photo` and `ME Video` categories, and the app automatically picks the right one based on the file type you are processing.

## How to Assign Categories

You can assign categories to your files in two ways:

### 1. Automatic AI Categorization
When you run the Cloud AI or Local AI analysis, the AI can be instructed to automatically select the best-fitting Master categories based on the image content. The AI selects from the allowed list in your matrix, and the app instantly stores them in the metadata.

### 2. Manual Assignment (Grid & Detail Window)
If you prefer to assign categories manually or want to adjust the AI's choices, you can easily do so:
*   **In the Grid (Batch Edit):** Select one or multiple photos, click the **Categories** button in the Batch Edit bar, and check up to 3 Master categories. They will be applied to all selected photos instantly.
*   **In the Detail Window:** The assigned categories are clearly displayed in their own section next to the Description. You can review them, see them neatly formatted in a list, and easily delete any incorrect ones using the "×" button.

## Visual Indicators: The `CAT` Badge
To give you a quick overview of your progress, ArtushVision provides visual feedback:
*   **CAT Badge:** As soon as a photo has at least one category assigned, a highly visible turquoise **`CAT` badge** appears on the image thumbnail in both the Grid and the Detail Window.
*   **Smart Tooltip:** If you hover your mouse over the `CAT` badge, a tooltip will pop up displaying the exact list of assigned Master categories for that specific file.

## Seamless CSV Export & FTP Integration
The true magic of the Category Matrix happens when you export your metadata. 

In the **CSV Template Editor**, you can add columns for `Mapped Category 1`, `Mapped Category 2`, etc. 

*   **Smart Auto-Mapping:** If you name your CSV template or FTP Server profile with the name of the agency (for example, `"Adobe Stock"` or `"Dreamstime"`), ArtushVision AI automatically understands where the file is going. It looks into your Category Matrix and fills the CSV column with the exact category required by that specific agency.
*   **Adobe Stock ID Conversion:** For Adobe Stock, you don't even need to know their category numbers. The app automatically converts text categories (like "Landscape" or "People") into Adobe's required numerical IDs (1-21) during the export.

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