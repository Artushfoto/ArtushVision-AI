---
title: "Global Microstock Distribution and Smart FTP Uploader"
description: "Streamline your microstock workflow with the Smart FTP Uploader. Features per-server multi-threading, automated CSV generation, and visual status tracking."
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

# Global Microstock Distribution and Smart FTP Uploader

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**Distribute your portfolio to dozens of stock agencies in just a few clicks. ArtushVision AI eliminates manual work with intelligent tracking, auto-reconnects, and dynamic CSV generation.**

Uploading photos and videos to multiple stock agencies can be a full-time job. Dropped connections, strict rate limits, and the difficulty of tracking what was uploaded where can ruin a professional workflow. The ArtushVision AI FTP Uploader handles the heavy lifting in the background, allowing you to focus on your creative work.


## Per-Server Multi-Threading and Auto-Retry

Not all stock agencies are built the same. While some servers can handle aggressive uploads, others, such as Zoonar or Freepik, may temporarily block users for opening too many connections at once.

* **Custom Thread Control:** Assign a specific number of concurrent upload threads (1 to 10) to each individual FTP server to stay within agency limits.
* **Smart Fallback:** If the application detects a "421 Too many connections" error, it automatically drops the thread count and seamlessly reconnects without failing the batch.
* **Auto-Resumes and Retries:** Set global retry limits for dropped connections or server timeouts to ensure your files always reach their destination.

**Global Distribution & Smart FTP Suite**

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-multiple-upload.webp" target="_blank" class="screenshot-link">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-multiple-upload.webp" alt="ArtushVision AI - Multi-threaded FTP Uploader for Microstock Distribution" width="100%" class="screenshot-img">
</a>   
<div style="height: 15px;"></div>

### Automated FTP Distribution and Smart Grid Status Tracking

<video src="video/ftp-upload.mp4" width="100%" autoplay loop muted playsinline title="ArtushVision AI - Smart FTP Upload and Status Tracking">
  ArtushVision AI - Multi-threaded FTP uploading, custom agency server groups configuration, and automated status tracking badges in the main photo grid.
</video>
<p><a href="video/ftp-upload.mp4" target="_blank" style="font-size: 0.9em;">Watch full-size FTP upload and status tracking workflow video</a></p>

---

## Dynamic CSV Generation and Category Mapping

Skip the manual spreadsheet work. The FTP module is deeply integrated with a powerful [Category Matrix](/docs/category-matrix.html) that translates your internal organization into agency-specific requirements.

* **Automated CSV Upload:** Assign a specific CSV template to an FTP server. When you start an upload, the application automatically generates the required CSV file with correct agency category IDs and uploads it alongside your media.
* **Temporary File Cleanup:** Generated CSV files are automatically removed from your local drive once the upload is complete to maintain a clean workspace. (You can edit these templates in the [CSV Editor](/docs/settings-configuration-customization.html#advanced-csv-template-editor)).
* **Agency Profiles:** Group your servers into Profiles (e.g., Exclusive Video Agencies or Main Stock Photo) to select multiple targets with a single click.

---

<h2 id="agency-profiles-and-server-groups">Agency FTP Profiles and Upload Server Groups</h2>
Speed up your distribution workflow by grouping multiple stock agencies together for simultaneous batch uploads.

Click to `File` → `Settings` → `Manage FTP Servers` or Select files and Click On Bottom Bar → `Upload via FTP` → `Manage FTP Servers`


<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-server-index.webp" target="_blank" class="screenshot-link" style="max-width: 800px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-server-index.webp" alt="ArtushVision AI - Manage Microstock FTP Agencies and Servers" style="width: 800px;" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

Click to `Add FTP` or `Double click` to FTP Agency → `Add or Update FTP Settings`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-editor.webp" target="_blank" class="screenshot-link" style="max-width: 600px; margin: 20px 0;">
  <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-editor.webp" alt="ArtushVision AI - FTP Upload Settings and Server Editor" style="width: 400px;" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

* **Custom Server Groups:** Create user-defined profiles (e.g., "Video Agencies" or "Editorial Only") to save your current selection of target FTP servers.
* **One-Click Distribution:** Select your pre-saved profile from the dropdown menu to instantly target all servers belonging to that specific group.
* **Independent Configuration:** Profile settings are safely stored independently of the main application, ensuring stability and allowing for easy backups.

Select `FTP Agencies` and `Save Profile Group`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-group-profiles.webp" target="_blank" class="screenshot-link" style="margin: 0; max-width: 800px; flex: 1 1 auto;">
    <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-group-profiles.webp" alt="ArtushVision AI - Microstock FTP Custom Server Groups Configuration" style="width: 100%; max-width: 800px;" class="screenshot-img">
  </a>
<div style="height: 15px;"></div>

---

## Advanced Tracking and Visual Status Badges

Never upload the same file twice by accident. ArtushVision AI remembers the complete upload history of every asset directly within the file metadata.

* **Micro-Badges in Grid:** Instantly see tiny agency badges (e.g., S for Shutterstock, A for Adobe, F for Freepik) directly on your photo thumbnails in the main grid. These badges appear automatically after a successful FTP upload, but you can also add them manually. You can simply type the name of any agency to track it, even if you don't have an FTP connection configured for it.
* **Persistent Metadata XMP Stamping:** Whether generated automatically or entered manually, the upload history is permanently written into the file's XMP/IPTC metadata. This ensures your tracking upload history is preserved forever, even if you move your files to another drive or open them in another software.
* **Safeguard Logic:** A built-in protection system automatically skips files that have already been successfully uploaded to the target agency in the past.

**FTP history badge in Main Grid**

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-badge.webp" target="_blank" class="screenshot-link" style="margin: 0; max-width: 400px; flex: 1 1 auto;">
    <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-badge.webp" alt="ArtushVision AI - FTP Upload History Badges in Photo Grid" style="width: 100%; max-width: 400px;" class="screenshot-img">
  </a>
<div style="height: 15px;"></div>

**FTP upload history editor**

Right-Mouse-click to any image in main grid → `Edit FTP History (Selection)`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-badge-editor.webp" target="_blank" class="screenshot-link" style="margin: 0; max-width: 100%; flex: 1 1 auto;">
    <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-badge-editor.webp" alt="ArtushVision AI - Edit Microstock FTP Upload History" style="width: 100%; max-width: 100%;" class="screenshot-img">
  </a>
<div style="height: 15px;"></div>

**Add FTP history badge**

Setup upload history → `Select or add servers, where is file already uploaded`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-add-badge.webp" target="_blank" class="screenshot-link" style="margin: 0; max-width: 400px; flex: 1 1 auto;">
    <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-add-badge.webp" alt="ArtushVision AI - Manually Add FTP Status Badge to File Metadata" style="width: 100%; max-width: 400px;" class="screenshot-img">
  </a>
<div style="height: 15px;"></div>

---

## Three-State Workflow Filtering

Manage thousands of assets with surgical precision using the dedicated FTP filters in the top bar.

* **Uploaded State:** View only assets that have successfully reached a specific agency.
* **Not Uploaded State:** Isolate files that still need to be distributed.
* **Ignore State:** Mark specific files to be skipped for certain agencies without removing them from your project.

**Advanced FTP filter**

Go to `Filter Toolbar` → `Advanced FTP Filter`

<a href="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-filter.webp" target="_blank" class="screenshot-link" style="margin: 0; max-width: 500px; flex: 1 1 auto;">
    <img src="https://raw.githubusercontent.com/Artushfoto/ArtushVision-AI/main/docs/images/ftp-filter.webp" alt="ArtushVision AI - Advanced FTP Upload Filter for Microstock Assets" style="width: 100%; max-width: 500px;" class="screenshot-img">
  </a>
<div style="height: 15px;"></div>

---

### Professional Workflow in 3 Steps:

1. **Filter and Select:** Use the grid filters to show only Not Uploaded files and select the batch you want to distribute.
2. **Choose Profile:** Open the FTP Uploader, pick a pre-saved Agency Profile, and hit Upload.
3. **Monitor and Stamp:** The application manages queues, threads, and auto-generated CSVs in the background, instantly stamping your thumbnails with success badges.

---

### [Get Started Now]
* [Download Free Lite Version](/docs/download-purchase.html)
* [Purchase Lifetime License - $39.99](/docs/download-purchase.html#buy-lifetime-license)

---

## Need Help?

Search the documentation pages directly or jump back to the main [Complete Documentation Index](/index.html#complete-documentation-index).

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

[⭐ User Reviews & Testimonials](/docs/artushvision-reviews.html)

[❓ Frequently Asked Questions (FAQ)](/docs/faq.html)

[💬 Support, Bugs & Community Forum](https://github.com/Artushfoto/ArtushVision-AI/discussions)

---

*ArtushVision AI - Stability and precision for professional photography workflows.*

<!-- Odložené načtení Google Analytics pro maximální PageSpeed skóre -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    let analyticsLoaded = false;

    function loadAnalytics() {
      if (analyticsLoaded) return;
      analyticsLoaded = true;

      // 1. Dynamické vložení externího skriptu gtag.js s NOVÝM ID
      var gtagScript = document.createElement('script');
      gtagScript.async = true;
      gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-KCZWMGZFJ5';
      document.head.appendChild(gtagScript);

      // 2. Inicializace nastavení Google Analytics s NOVÝM ID
      window.dataLayer = window.dataLayer || [];
      window.gtag = function(){ dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', 'G-KCZWMGZFJ5');

      // 3. Odstranění posluchačů událostí po úspěšném načtení
      document.removeEventListener('scroll', loadAnalytics);
      document.removeEventListener('mousemove', loadAnalytics);
      document.removeEventListener('touchstart', loadAnalytics);
    }

    // Spuštění při první skutečné interakci uživatele
    document.addEventListener('scroll', loadAnalytics, { passive: true });
    document.addEventListener('mousemove', loadAnalytics, { passive: true });
    document.addEventListener('touchstart', loadAnalytics, { passive: true });

    // Pojistka: Pokud uživatel do 5 sekund nic neudělá, načíst Analytics automaticky
    setTimeout(loadAnalytics, 5000);
  });
</script>