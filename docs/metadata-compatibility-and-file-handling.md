---
title: "Metadata Compatibility and File Handling | ArtushVision AI"
description: "Learn how ArtushVision AI ensures bi-directional metadata synchronization with Adobe Lightroom, Zoner Photo Studio, and digiKam."
---
<div style="display: none;">
<style>
header, .page-header, .site-header, footer, .site-footer, .footer { display: none !important; }
h1 { text-align: center; }
</style>
</div>

# Metadata Compatibility and File Handling

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

**ArtushVision AI utilizes the industry-standard ExifTool for reading and writing metadata. To ensure seamless bi-directional synchronization with the most popular photo editors and file managers, the application writes information in parallel across multiple metadata standards (XMP, IPTC, and EXIF).**

The application is fully compatible out-of-the-box with software such as **Adobe Lightroom, Zoner Photo Studio, digiKam, ACDSee**, and native **Windows Explorer**.

---

## Core Text Metadata Synchronization

When saving text information, the data is synchronously written into both the modern XMP and the legacy IPTC standards to ensure older systems and stock agencies read them perfectly.

* **Universal Title and Description:** Titles are written into `XMP-dc:Title`, `IPTC:ObjectName`, `XMP-photoshop:Headline`, and `XPTitle` (for Windows). Descriptions map directly to `XMP-dc:Description`, `IPTC:Caption-Abstract`, and `XPComment`.
* **Smart Keyword Management:** Tags are distributed to `XMP-dc:Subject`, `IPTC:Keywords`, and Lightroom's specific `XMP-lr:HierarchicalSubject`. The application automatically deduplicates words and strips empty tags during both reading and writing processes.

---

## Ratings, Flags, and Color Labels

Every photo management software historically uses slightly different tags for organization. ArtushVision AI bridges these gaps and ensures your sorting logic is never lost.

* **Universal Star Ratings (1–5):** The app reads ratings in multiple formats and writes them to all supported standards simultaneously. This includes Adobe Lightroom (`XMP-xmp:Rating`), Zoner Photo Studio (`XMP-znr:Rating`), ACDSee, and Windows Explorer (`MicrosoftPhoto:Rating`, which is automatically translated from the 1-99 scale to 1-5 stars).
* **Pick and Reject Flags:** Flags are highly dependent on specific software ecosystems. ArtushVision AI fully supports the two main ones: Adobe Lightroom (`XMP-xmpDM:Pick` and `XMP-xmpDM:Good`) and digiKam (`XMP-digiKam:PickLabel`).
* **Color Labels:** Colors (Red, Yellow, Green, Blue, Purple) are saved as standard text strings (`XMP-xmp:Label`) and simultaneously converted to numerical priority (`XMP-photoshop:Urgency`) for legacy software compatibility.

---

## File Handling and XMP Sidecars

* **Non-Destructive RAW and Video:** To guarantee maximum safety of your original data, the application *never* writes directly into RAW files (CR2, NEF, ARW, DNG) or Videos (MP4, MOV). All metadata is safely stored in adjacent `.xmp` sidecar files.
* **XMP Naming Conventions:** ArtushVision AI fully supports and reads both recognized naming standards: the basic standard (`filename.xmp`) and Adobe Lightroom's extended standard (`filename.CR2.xmp`). When creating a new XMP file, existing EXIF data is automatically copied from the original RAW/Video to prevent technical data loss.
* **Direct JPG, TIFF, and PNG Writing:** Standard image formats receive metadata directly into the file to prevent data fragmentation. If a legacy XMP sidecar already exists for a JPG, the app automatically merges it, renames it, and archives it to prevent future loading collisions.

---

## ArtushVision Specific Metadata

The application stores its internal tracking data in standard text fields so it remains readable and persistent even in other editors.

* **FTP Upload History:** The list of stock agencies where a photo was successfully uploaded is safely stored in the `IPTC:TransmissionReference` and `XMP-photoshop:TransmissionReference` fields.
* **Category Mapping:** Selected agency categories are saved into supplemental fields (`XMP-photoshop:SupplementalCategories` and `IPTC:SuppCategory`).
* **Internal Flags:** System flags (e.g., AI Generated, Editorial, Mature) are embedded into `IPTC:SpecialInstructions` and `XMP-photoshop:Instructions` using a safe bracket format.

---

## Visual Status Badges and File Management

Keep track of your technical data and backup states without ever opening a properties dialog. ArtushVision AI displays small informational micro-badges directly on your image thumbnails in both the grid and detail views.

* **File Type and Geolocation:** Instantly identify special media types with dedicated **RAW** and **VIDEO** badges, or see if a file contains embedded coordinates with the **GPS** badge.
* **Backup Trackers:** Know your data is safe at a glance. The application highlights files that have a dedicated **XMP** sidecar, an original backup file (**ORIG**), or are safely backed up in a spreadsheet (**CSV**).
* **Distribution and AI Tags:** Track your workflow visually. The **CAT** badge indicates successfully mapped categories, the **GETTY** badge highlights optimized terms, and tiny agency micro-badges (e.g., S, A, F) show your complete FTP upload history.

---

## Seamless Adobe Lightroom and other photo management software compatibility

← Back to ArtushVision AI Home

Keep your master catalog perfectly in sync. ArtushVision AI writes all tags and edits into industry-standard XMP sidecars, ensuring your non-destructive workflow remains intact.

* **[Non-Destructive XMP Workflow:](/docs/metadata-compatibility-and-file-handling#file-handling-and-xmp-sidecars)** All metadata edits are safely stored in external sidecar files, keeping your original RAW assets completely untouched.
* **Instant Catalog Synchronization:** To apply your AI-generated keywords and edits back to your Lightroom catalog, simply select the modified photos in the Lightroom grid.
* **One-Click Import:** Right-click the selected assets in Lightroom and choose **Metadata > Read Metadata from File**. Lightroom will instantly update its database with all your new tags, titles, and color labels.

*ArtushVision AI - Universal XMP Support: Fits Seamlessly Into Your Existing Ecosystem.*

---

### [Get Started Now]

* Download Free Lite Version
* Purchase Lifetime License - $39.99

---

[← Back to ArtushVision AI Home](https://vision.artushfoto.eu)

---

*ArtushVision AI - Professional precision and complete configuration control.*
