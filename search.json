---
layout: null
---
[
  {% assign all_items = site.pages | concat: site.posts %}
  {% for item in all_items %}
    {% if item.title and item.url != "/search.json" and item.url != "/" %}
    {
      "title": {{ item.title | jsonify }},
      "url": {{ item.url | relative_url | jsonify }},
      "content": {{ item.content | strip_html | strip_newlines | jsonify }}
    }{% unless forloop.last %},{% endunless %}
    {% endif %}
  {% endfor %}
]