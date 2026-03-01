# ArtushVision AI

**ArtushVision AI** is a professional, AI-powered desktop application designed for photographers, stock agencies, and archivists. It automates the process of keywording, captioning, and managing metadata for images and videos using advanced Computer Vision models (via OpenRouter/Gemini) and robust local tools.

ArtushVision AI serves as a bridge between modern AI analysis and industry-standard metadata formats (EXIF, IPTC, XMP), utilizing **ExifTool** for reliable file operations.

---

## 🚀 Key Features

### 🧠 AI-Powered Analysis
*   **Vision Models:** Integrates with top-tier Vision AI models (Gemini Pro Vision, GPT-4o, Claude 3.5 Sonnet, etc.) via OpenRouter.
*   **Auto-Keywording:** Generates relevant keywords based on visual content.
*   **Auto-Captioning:** Creates descriptive titles and detailed descriptions.
*   **Custom Profiles:** Users can define custom system prompts to tailor AI output (e.g., specific stock photography requirements).

### 📂 Metadata Management
*   **Industry Standards:** Full support for XMP, IPTC, and EXIF standards.
*   **Format Support:** Handles JPG, TIFF, PNG, and **RAW formats** (via XMP sidecars).
*   **Video Support:** Metadata management for video files using FFmpeg for thumbnails and ExifTool for data.
*   **Batch Operations:** Bulk editing, copying/pasting metadata, and finding/replacing text across thousands of files.
*   **Validation:** Real-time character counting and limit validation for stock agency requirements.

### 🖥️ Modern User Interface
*   **Grid View:** A responsive, virtualized grid capable of handling large folders efficiently.
*   **Detail View:** A focused editor for individual files with zoomable preview and map integration.
*   **Tagging System:** Interactive "bubble" widgets for keywords with drag-and-drop reordering and color coding (AI vs. Manual vs. Original).
*   **Themes:** Fully supported Dark and Light modes.

### 🛠️ Productivity Tools
*   **Spell Check:** Integrated multi-language spell checking (Hunspell/Enchant) with online suggestions.
*   **Synonyms:** Built-in synonym finder (Datamuse API) to expand keyword reach.
*   **Translation:** Automatic translation of keywords and descriptions.
*   **Geolocation:** Integrated map view (Google Maps/OpenStreetMap) to visualize GPS data.
*   **Backups:** Automatic CSV backups and "Original" file preservation before saving.

---

## 📂 Codebase Structure & Module Description

The project is modularized to ensure maintainability and separation of concerns. Below is a breakdown of the key files and their functions.

### 1. Core & Entry Point
*   **`run.py`**: The main entry point of the application. Initializes the Qt Application, applies styles, and launches the main window.
*   **`ai_keywording_config.py`**: Central configuration file. Handles paths, constants, and default settings.
*   **`ai_keywording_license.py`**: Manages licensing logic, trial limitations, and activation security.
*   **`ai_development_history.py`**: Maintains a changelog and development history log.
*   **`qt_version.py`** & **`update_version.py`**: Manages application versioning.

### 2. Main GUI & Logic
*   **`ai_keywording_gui_qt.py`**: The main application class (`ArtushVisionQtApp`). Orchestrates the high-level logic and connects major components.
*   **`qt_main_window_ui.py`**: Defines the layout and widget initialization for the main window.
*   **`qt_app_logic.py`**: Contains business logic separated from the GUI implementation.
*   **`qt_settings.py`**: The Settings dialog implementation, handling user preferences.
*   **`qt_profiles.py`**: Editor for AI System Prompts (Profiles).

### 3. The Grid System (Gallery)
The grid view is split into several modules for performance and readability:
*   **`modern_grid.py`**: The main container widget for the image grid.
*   **`qt_grid_core.py`**: Core functionality for the grid (layout management, item storage).
*   **`qt_grid_populate.py`**: Handles the loading and populating of grid items (threading, batching).
*   **`qt_grid_events.py`**: Manages UI events (mouse clicks, keyboard shortcuts) within the grid.
*   **`qt_grid_handlers.py`**: Specific handlers for grid interactions.
*   **`qt_grid_spellcheck.py`**: Manages spell checking specifically for grid cells.
*   **`grid_tag_actions.py`**: Logic for adding, removing, and editing tags directly in the grid.
*   **`qt_thumbnails.py`**: Handles asynchronous generation and caching of image/video thumbnails.

### 4. The Detail View (Single Image Editor)
A complex editor split into mixins:
*   **`qt_detail.py`**: The main dialog window for editing a single image.
*   **`qt_detail_ai.py`**: Handles AI generation requests within the detail view.
*   **`qt_detail_map.py`**: Manages the embedded map widget (QWebEngineView) and GPS data.
*   **`qt_detail_nav.py`**: Logic for navigating between previous/next images.
*   **`qt_detail_tags.py`**: Manages the keyword bubbles within the detail view.
*   **`qt_detail_undo.py`**: Implements a local Undo/Redo stack for the detail editor.
*   **`qt_detail_loader.py`**: Handles loading high-res previews and metadata.
*   **`qt_detail_sync.py`**: Synchronizes changes back to the main grid when closing.

### 5. AI & Keywording Engine
*   **`ai_keywording_ai.py`**: The core AI logic. Communicates with APIs (OpenRouter), handles prompts, and parses JSON responses.
*   **`qt_ai_handler.py`**: A Qt-based wrapper for the AI engine to run requests in background threads without freezing the UI.

### 6. Metadata & File I/O
*   **`qt_io.py`**: Handles saving data to disk. Manages ExifTool processes, backups, and CSV export/import.
*   **`qt_metadata.py`**: Logic for reading metadata from files and mapping it to UI fields.
*   **`exiftool_utils.py`**: Wrapper functions for interacting with the `exiftool.exe` command-line interface.
*   **`qt_batch.py`**: Implements batch operations (Find/Replace, Append, etc.).

### 7. Utilities & Helpers
*   **`qt_utils.py`** & **`qt_core_utils.py`**: General utility functions (file paths, string manipulation, etc.).
*   **`qt_ui_utils.py`**: Helpers for UI specific tasks.
*   **`qt_text_utils.py`**: Text processing utilities.
*   **`qt_lang_utils.py`**: Language detection and localization helpers.
*   **`persistent_cache.py`**: Manages caching for translations and synonyms to reduce API calls.
*   **`qt_webengine_utils.py`**: Utilities for the embedded Chromium browser (Map).

### 8. UI Components & Widgets
*   **`qt_tag_widgets.py`**: Custom widget for rendering interactive keyword bubbles.
*   **`qt_smart_widgets.py`**: Enhanced text inputs with validation and features.
*   **`qt_synonym_dialog.py`**: Dialog for finding synonyms using external APIs.
*   **`qt_spellcheck.py`**: The spell-checking engine integration.
*   **`qt_highlighter.py`**: Syntax highlighting for text fields (e.g., coloring keywords by source).
*   **`qt_icons.py`**: Centralized icon management (SVG/Base64).
*   **`qt_styles.py`**: Manages application stylesheets (CSS) and themes.

---

## ⚙️ Technical Requirements

*   **Python 3.10+**
*   **PyQt6**: For the Graphical User Interface.
*   **ExifTool**: Must be installed/available in the system path for metadata operations.
*   **FFmpeg**: Required for video thumbnail generation.
*   **Nuitka**: Used for compiling the application into a standalone executable (`.exe`).

## 📦 External Dependencies
*   `requests`: For API calls.
*   `Pillow`: For image processing.
*   `PyQt6-WebEngine`: For map display.
*   `pyspellchecker` / `pyenchant`: For spell checking.
*   `langdetect`: For language identification.

---

*Generated from project source code analysis.*

<!--stackedit_data:
eyJoaXN0b3J5IjpbOTc5MjMwMTM1XX0=
-->