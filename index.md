<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<script src="/pagefind/pagefind-ui.js"></script>

<div style="max-width: 500px; margin: 20px auto; padding: 0 10px;">
  <div id="search"></div>
</div>

<script>
  window.addEventListener('DOMContentLoaded', (event) => {
    if (typeof PagefindUI !== 'undefined') {
      new PagefindUI({ 
        element: "#search", 
        showSubResults: true,
        translations: {
          placeholder: "Search documentation...",
          clear_search: "Clear",
          searching: "Searching..."
        }
      });
    }
  });
</script>