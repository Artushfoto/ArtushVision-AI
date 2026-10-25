---
title: "GPS Geotagging: Assign Coordinates Manually or from GPX Track"
description: "Learn how to geotag photos in ArtushVision AI. Easily assign precise GPS coordinates manually or sync location data automatically from GPX track logs."
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

# Simple Geotagging Photos: Manual Coordinates and GPX Track Import

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

### 📍 Interactive GPS Assignment & Instant Geo-Verification

A comprehensive GPS assignment and editing workflow has been added directly to the Photo Detail window:

* **Where and How to Add GPS:**  
  When an image lacks camera GPS metadata, an **`📍 Add GPS`** button appears in the bottom toolbar of the Detail window (or **`✏ Edit GPS`** for manually assigned coordinates). Clicking it launches an interactive map dialog where you can locate the spot using instant search, by clicking anywhere on the map, dragging the marker pin, or manually entering precise latitude and longitude coordinates. You can toggle between **Google Maps (Hybrid, Satellite, Roadmap)** and **OpenStreetMap** layers, and click the **`👁️ Street View`** button to open a full 360° panorama in your browser for immediate visual confirmation of the location before saving.

* **Dialog Geometry Memory:**  
  The GPS Picker window automatically remembers its screen position and dimensions across sessions, launching at your preferred size and layout every time.

* **Why Add GPS (Geo Filter & SEO Relevance):**  
  Adding GPS coordinates provides much more than just standard EXIF/XMP metadata—it supplies concrete **Geographical Evidence** for the ArtushVision AI decision pipeline. The moment location is confirmed, a photo geo-context is built immediately, running all existing keywords through the **Geo Filter**:
  
  1. Names of countries, cities, states, regions, and prominent landmarks/POIs matching the coordinates are instantly verified as **geo-confirmed (green bubbles)**.
  
  2. Confirmed location terms receive maximum weight in SEO and KWQ scoring and are safeguarded against accidental removal or demotion during keyword sorting.
  
  3. This dramatically improves photo discoverability and relevance on stock agency search engines without requiring a camera with built-in GPS hardware.

---

## Camera Clock Drift Calculator & Reference Photo Sync
Eliminate the headache of synchronizing out-of-sync camera clocks with GPX tracks:
* **Reference Photo Method (Artush GPX Tracker):**  
  Simply take a single photo of your smartphone screen displaying your GPS tracking app (such as the free companion [Artush GPX Tracker](https://gpxtracker.artushfoto.eu)). In the GPS dialog, open the **Time Offset Calculator**, type in the time visible on the photo's screen, and the engine automatically computes the exact second-accurate clock drift.
* **Sub-Second Accuracy:** Photos are matched to your GPX route with sub-second precision, accounting for local daylight saving time and camera drift.

---

## GPS Removal & Privacy Anonymization
For sensitive commercial shoots, private residential locations, or protected wildlife habitats, you can now strip GPS coordinates cleanly:
* **1-Click Location Removal:** Right-click any photo or multi-photo selection in the grid and choose **`Remove GPS Coordinates`** (also available in the Detail toolbar and Map picker).
* **Two-Step Camera Hardware Protection:** If an original photo contains native camera hardware EXIF GPS, the application requests an explicit confirmation to prevent accidental loss of original camera telemetry.
* **Full EXIF & XMP Purge:** Strips all GPS tags and cache references atomically, with complete Undo (`Ctrl+Z`) support.

---

### Automatic GPX Track Geotagging & Time Synchronization

You can now reconstruct the exact geographical positions of entire photo sessions directly from GPS track recordings logged by outdoor GPS devices, fitness trackers, smartwatches, or smartphone hiking apps:

* **Unified GPX Mode in GPS Picker:**  
  Inside the GPS Picker dialog, simply switch the mode toggle from **`📍 Manual GPS`** to **`📈 GPX Track`**. Clicking **`Select GPX file...`** loads standard GPX tracks (v1.0 & v1.1) with elevation and UTC timestamps, rendering the entire route polyline directly onto the interactive map.

* **High-Precision Time-Matching Algorithm:**  
  Photos are matched to the track by synchronizing image capture timestamps with recorded trackpoints using an ultra-fast binary search (`bisect`) engine with sub-second linear position and elevation interpolation.

* **Camera Clock Drift & Time Zone Correction:**  
  Cameras often have clocks set incorrectly or set to local daylight saving time without embedded UTC offsets. The GPX panel includes:
  * **Camera Time Zone Selector:** Full timezone offset range from `UTC-12:00` to `UTC+14:00` with automatic detection of your system timezone.
  * **Clock Drift Fine-Tuning:** Numerical drift entry in seconds (`+/-` seconds) to compensate for camera clocks that were slightly ahead or behind real GPS time.

* **Smart Gap Protection (No False Positions):**  
  To prevent assigning erroneous interpolated positions across pauses in tracking (e.g., flights, tunnels, indoor breaks, or vehicle drives), the engine enforces strict limits:
  * **Max Time Gap:** Adjustable threshold (e.g., 5 min) beyond which timestamps are rejected rather than blindly interpolated.
  * **Max Distance Jump:** Filters out GPS telemetry anomalies and sudden teleportation artifacts.
  * **Quality Categorization:** Matches are classified into **MATCHED** (reliable), **UNCERTAIN** (borderline), and **UNMATCHED**. An optional checkbox allows you to selectively include or exclude uncertain points.

* **Visual Map Inspection of Photo Locations:**  
  Before committing any metadata to your files, all matched photos appear as interactive marker pins along the GPX polyline on Leaflet/Google Maps. Clicking any pin zooms in and displays the filename, timestamp offset, and matching status in a real-time tooltip.

  <a href="images/time-sync-in-artushvision-ai.webp" target="_blank" class="screenshot-link">
  <img src="images/time-sync-in-artushvision-ai.webp" alt="ArtushVision Camera Clock Drift Calculator & Reference Photo Sync" width="100%" class="screenshot-img">
</a>
<div style="height: 15px;"></div>

---

### Batch GPS Assignment & Strict Protection Lock

Geotagging multiple photos in bulk is now fast, secure, and non-destructive:

* **Grid Context Menu & Batch Bar Integration:**  
  Select any number of photos in the main grid and right-click to choose **`📍 Assign GPS coordinates to selection...`** (or use the batch edit toolbar). The action is available for both single and multi-photo selections.

* **Strict GPS Protection Lock (Zero Data Overwrites):**  
  To protect valuable camera originals, bulk operations enforce a strict, two-tier protection lock:
  * **Camera EXIF GPS Protected:** Any photo with existing GPS coordinates (whether from camera EXIF, manual placement, or previous GPX runs) is **strictly locked and skipped**.
  * **Explicitly Cleared State Respected:** If coordinates were previously removed by the user, bulk operations respect this choice and will not re-tag the file.
  * The dialog banner clearly displays: **`Selected`**, **`Eligible (no GPS)`**, and **`Protected (already has GPS)`** counts.

* **Efficient Single-Call Reverse Geocoding:**  
  When applying GPS coordinates to dozens or hundreds of images simultaneously, the application performs a smart, single reverse geocoding lookup (or spatial ~1km clustering for GPX tracks). It automatically populates missing **Country** and **City** fields without redundant network calls, while strictly preserving any existing user metadata.

* **Full Undo / Redo (`Ctrl+Z` / `Ctrl+Y`):**  
  Both single and bulk GPS operations (manual coordinate assignment, GPX geotagging, or coordinate removal) are fully integrated into the global Undo history stack. If you accidentally apply coordinates to the wrong folder selection, pressing **`Ctrl+Z`** immediately restores all original metadata, caches, and SEO scores atomically.

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
