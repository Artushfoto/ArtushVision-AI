# How to Download Local AI Models via Ollama

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

To unlock the full potential of ArtushVision AI's **Enhanced Local AI** or **Hybrid AI** modes, you need to download the appropriate models to your computer. This guide will walk you through choosing, downloading, and organizing your local models directly through the internal Model Manager.

> 💡 **Tip for Lite Version Users:** Running local models is a fantastic way to bypass cloud API constraints. To see how local models fit into your license tier, check out our [Free Trial Limits and Testing Guide](/docs/free-trial-limits-and-testing.html).

---

## 1. Find a Model on the Ollama Website
First, you need to select the specific model that matches your hardware and workflow needs.

* Open your web browser and navigate to the official [Ollama Library](https://ollama.com/search).
* Browse or search for models. Pay close attention to the model capabilities:
  * **Vision Models:** Required to analyze, describe, and tag images (e.g., `gemma4:e2b`, `qwen3-vl:4b`). These are critical for processing visual data and utilizing features like the [Absolute Priority AI Hint](/docs/advanced-ai-prompting-profiles-variables.md#basic-and-contextual-variables).
  * **Text Models:** Used for advanced metadata formatting, translations, and structuring tag taxonomies (e.g., `qwen2.5:7b`, `deepseek-r1:7b`).
* Once you find the desired model, copy its exact name including the parameter size tag (for example, copy `qwen3-vl:4b`, not just `qwen3-vl`).

![Screenshot: Finding and copying the exact model name on the Ollama website](images/ollama-website-copy.png)

---

## 2. Open the Internal Model Manager
* In ArtushVision AI, open the **Profile Editor**.
* Locate the **AI Model** input field and click the **Search Icon** next to it. This will open the internal AI Model Selection window.

![Screenshot: Clicking the search icon in the Profile Editor to open the Model Manager](images/open-model-manager.png)

---

## 3. Download the Model
* Look for the **Download New Model** section, located at the bottom of the Model Selection window.
* Paste the exact model name you copied from the Ollama website into the text field.
* Click the **Download** button.

![Screenshot: Pasting the model name and clicking the Download button](images/download-model-button.png)

---

## 4. Monitor the Download Progress
* The application will connect to your local Ollama instance and initiate the download process.
* You will see a live download progress indicator displaying the transferred data in MB or GB alongside the download speed.
* Wait until the download is fully complete. Once finished, a success message will appear, and the model will automatically populate in your list of available models.

![Screenshot: Live download progress indicator showing MB/GB transferred](images/download-progress.png)

---

## 5. Auto-Detection, Manual Override & Custom Notes

Once a model is successfully downloaded, the Model Manager automatically categorizes and organizes it for you:

### Auto-Detection & Manual Override
The manager automatically scans your downloaded models and categorizes them as **Vision** (models that can "see" images) or **Text** (language-only models), color-coding them in the grid for easy identification. If the system fails to recognize the model type automatically, you can easily right-click the model and configure its type **manually**.

### Adding Custom Notes
To keep your local AI environment organized, you can assign personal performance notes to any model:
* Locate your newly downloaded model in the manager's table.
* Double-click the cell in the **Note** column for that specific model.
* Type your custom description to document its real-world performance (e.g., *"Great for animal species and fine details"* or *"Fast text formatter, struggles with complex JSON"*).
* Press **Enter** or click away to save it. This helps you remember which specific subjects or tasks each model handles well and which it doesn't.

![Screenshot: Adding a custom note and viewing color-coded model types in the table](images/model-manager-grid.png)

---

## Next Steps & Related Documentation
* **Advanced Prompting:** Now that your models are ready, learn how to maximize their accuracy using [Advanced AI Prompting & Profiles](/docs/advanced-ai-prompting-profiles-variables.md).
* **Getty Integration:** Learn how to combine local AI text models with our [Automated Getty Mapping](/docs/advanced-ai-prompting-profiles-variables.md) to instantly match official agency taxonomies.

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