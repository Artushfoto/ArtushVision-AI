---
title: "Global Stock Distribution and Smart FTP Uploader | ArtushVision AI"
description: "Streamline your microstock workflow with the Smart FTP Uploader. Features per-server multi-threading, automated CSV generation, and visual status tracking."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
</style>
</div>

# Global Distribution and Smart FTP Uploader

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Distribute your portfolio to dozens of stock agencies in just a few clicks. ArtushVision AI eliminates the manual work of microstock distribution with intelligent tracking, auto-reconnects, and dynamic CSV generation.**

Uploading photos and videos to multiple stock agencies can be a full-time job. Dropped connections, strict rate limits, and the difficulty of tracking what was uploaded where can ruin a professional workflow. The ArtushVision AI FTP Uploader handles the heavy lifting in the background, allowing you to focus on your creative work.

[IMAGE: A wide screenshot of the main FTP Upload window showing the list of agencies, progress bars with speed/ETA, and the Profiles dropdown.]

---

## Per-Server Multi-Threading and Auto-Retry
Not all stock agencies are built the same. While some servers can handle aggressive uploads, others, such as Zoonar or Freepik, may temporarily block users for opening too many connections at once.

* **Custom Thread Control:** Assign a specific number of concurrent upload threads (1 to 10) to each individual FTP server to stay within agency limits.
* **Smart Fallback:** If the application detects a "421 Too many connections" error, it automatically drops the thread count and seamlessly reconnects without failing the batch.
* **Auto-Resumes and Retries:** Set global retry limits for dropped connections or server timeouts to ensure your files always reach their destination.

[IMAGE: A close-up screenshot of the Manage FTP Servers dialog, highlighting the Concurrent Threads slider and the CSV Template dropdown.]

---

## Dynamic CSV Generation and Category Mapping
Skip the manual spreadsheet work. The FTP module is deeply integrated with a powerful [Category Matrix](settings-configuration-customization.md#the-category-matrix) that translates your internal organization into agency-specific requirements.

* **Automated CSV Upload:** Assign a specific CSV template to an FTP server. When you start an upload, the application automatically generates the required CSV file with correct agency category IDs and uploads it alongside your media.
* **Temporary File Cleanup:** Generated CSV files are automatically removed from your local drive once the upload is complete to maintain a clean workspace. (You can edit these templates in the [CSV Editor](settings-configuration-customization.md#advanced-csv-template-editor)).
* **Agency Profiles:** Group your servers into Profiles (e.g., Exclusive Video Agencies or Main Stock Photo) to select multiple targets with a single click.

[IMAGE: A screenshot of the Category Matrix Editor showing how Master categories map to Adobe Stock, Shutterstock, and Motion Elements IDs.]

---

## Advanced Tracking and Visual Status Badges
Never upload the same file twice by accident. ArtushVision AI remembers the complete upload history of every asset directly within the file metadata.

* **Micro-Badges in Grid:** Instantly see tiny agency badges (e.g., S for Shutterstock, A for Adobe, F for Freepik) directly on your photo thumbnails in the main grid.
* **Persistent XMP Stamping:** Status information is written into the file's XMP metadata, ensuring your upload history is preserved even if you move your files to another drive.
* **Safeguard Logic:** A built-in protection system automatically skips files that have already been successfully uploaded to the target agency in the past.

[IMAGE: A screenshot of the main photo grid, highlighting the small agency micro-badges on the thumbnails and the Advanced FTP Filter dropdown.]

---

## Three-State Workflow Filtering
Manage thousands of assets with surgical precision using the dedicated FTP filters in the top bar.

* **Uploaded State:** View only assets that have successfully reached a specific agency.
* **Not Uploaded State:** Isolate files that still need to be distributed.
* **Ignore State:** Mark specific files to be skipped for certain agencies without removing them from your project.

---

### Professional Workflow in 3 Steps:
1. **Filter and Select:** Use the grid filters to show only Not Uploaded files and select the batch you want to distribute.
2. **Choose Profile:** Open the FTP Uploader, pick a pre-saved Agency Profile, and hit Upload.
3. **Monitor and Stamp:** The application manages queues, threads, and auto-generated CSVs in the background, instantly stamping your thumbnails with success badges.

---

### [Get Started Now]
* [Download Free Lite Version](https://www.artushfoto.eu/Software/Download-ArtushVision-AI)
* [Purchase Lifetime License - $39.99](https://www.artushfoto.eu/Software/Purchase-ArtushVision-AI)

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

---
*ArtushVision AI - Stability and precision for professional photography and stock distribution.*
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEwNjk4MjM2OF19
-->