<div align="center">
  <h1>ArtushVision AI</h1>
  <p>
    <strong>The Ultimate AI-Powered Metadata & Keywording Tool for Photographers and Videographers</strong>
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Version-v2026.1.0-blue.svg" alt="Version">
  </p>

  <p>
    <em>Automate your stock photography workflow with state-of-the-art Vision AI.</em>
  </p>
</div>

<hr>

<h2>📖 About The Project</h2>
<p>
  <strong>ArtushVision AI</strong> is a sophisticated desktop application designed to revolutionize the workflow of stock photographers, archivists, and digital asset managers. Built with <strong>Python</strong> and <strong>PyQt6</strong>, it leverages state-of-the-art Large Language Models (LLMs) via OpenRouter to analyze images and videos, automatically generating accurate titles, descriptions, and keywords.
</p>
<p>
  It bridges the gap between raw media files and ready-to-sell stock assets by combining visual analysis with "hard facts" like GPS data, dates, and folder context.
</p>

<h2>🎯 Key Use Cases</h2>
<ul>
  <li><strong>Stock Photography/Videography:</strong> Automates the tedious process of tagging content for agencies (Shutterstock, Adobe Stock, Getty) while adhering to strict metadata limits.</li>
  <li><strong>Digital Archiving:</strong> Rapidly organizes large collections by identifying content, OCR text, and specific locations.</li>
  <li><strong>Location-Aware Tagging:</strong> Uses GPS coordinates to accurately identify landmarks, cities, and countries instead of generic guesses.</li>
</ul>

<h2>🚀 Features</h2>

<h3>🧠 Advanced AI Analysis</h3>
<ul>
  <li><strong>Multi-Model Support:</strong> Switch between top-tier Vision models (Google Gemini 2.0, Claude 3.5, GPT-4o) via OpenRouter.</li>
  <li><strong>Context-Aware Prompting:</strong> The AI analyzes not just the image, but also GPS coordinates, Google Maps links, folder names, dates, and lens information.</li>
  <li><strong>Video Intelligence:</strong> Extracts and analyzes video frames to generate metadata for video files, supporting technical data analysis (duration, fps).</li>
  <li><strong>Bilingual Output:</strong> Generates keywords in English and a local language (e.g., Czech) simultaneously.</li>
</ul>

<h3>🖥️ Modern & Efficient GUI</h3>
<ul>
  <li><strong>Responsive Grid:</strong> High-performance thumbnail grid capable of handling thousands of files.</li>
  <li><strong>Visual Status System:</strong> Color-coded cells indicate file status (Unedited, Modified, Saved, Validation Error).</li>
  <li><strong>Interactive Badges:</strong> Quick indicators for GPS, RAW, Video, or XMP sidecar presence.</li>
  <li><strong>Tag Bubbles:</strong> Drag-and-drop interface for managing keywords individually.</li>
</ul>

<h3>⚡ Workflow & Batch Operations</h3>
<ul>
  <li><strong>Bulk Editing:</strong> Add, remove, or replace metadata across hundreds of files instantly.</li>
  <li><strong>Smart Filtering:</strong> Filter by file type (RAW/JPG/Video), Rating, Flags, or Color Labels.</li>
  <li><strong>Undo/Redo:</strong> Full history support to safely revert changes.</li>
  <li><strong>Cost Tracking:</strong> Monitors API usage and calculates costs per session.</li>
</ul>

<h2>🌟 Major Advantages</h2>
<ol>
  <li><strong>Reduced Hallucinations:</strong> By feeding the AI specific data (GPS, Date, Folder Name), the output is factually accurate.</li>
  <li><strong>Speed:</strong> Multi-threaded processing allows for analyzing hundreds of images in minutes.</li>
  <li><strong>Compliance:</strong> Built-in validators ensure titles and keywords meet stock agency requirements.</li>
  <li><strong>Safety:</strong> Uses <strong>ExifTool</strong> for industry-standard metadata writing and creates XMP sidecar backups.</li>
</ol>

<h2>🛠️ Basic Workflow</h2>
<ol>
  <li><strong>Import:</strong> Import a folder of images or videos into the grid.</li>
  <li><strong>Filter:</strong> Select the images you want to analyze (e.g., "Show only RAW files").</li>
  <li><strong>Run AI:</strong> Click "Run AI Analysis". The app generates optimized proxies and sends them to the AI.</li>
  <li><strong>Review:</strong> Use the <strong>Detail View</strong> or Batch Replace to refine the results.</li>
  <li><strong>Save:</strong> Click "Save All" to write metadata using ExifTool.</li>
</ol>

<h2>💻 Technical Stack</h2>
<ul>
  <li><strong>Metadata Engine:</strong> Phil Harvey's ExifTool</li>
  <li><strong>Video Processing:</strong> FFmpeg / FFprobe</li>
  <li><strong>AI Integration:</strong> OpenRouter API</li>
</ul>

<hr>
<p align="center">
  <em>Developed by ArtushFoto.eu</em>
</p>
