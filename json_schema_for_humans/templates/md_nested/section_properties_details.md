{% for sub_property in schema.iterate_properties %}
  {%- if sub_property.is_additional_properties and not sub_property.is_additional_properties_schema -%}
    {% continue %}
  {% endif %}

  {% set html_id = sub_property.html_id %}

  {% set description = sub_property | get_description %}
<details>
<summary>
    {% filter md_heading(depth + 1, html_id, True) -%}
      {%- filter replace('\n', '') -%}
    {%- if 'Required' in config.template_md_options.heading_leading_badges and not skip_required and sub_property.property_name -%}
        {{ md_badge("Required", "blue", show_text=True) if sub_property.is_required_property else md_badge("Optional", "yellow", show_text=True) }}
    {%- endif -%}
    {%- if 'Type' in config.template_md_options.heading_leading_badges -%}
        {{ md_badge("type", None, sub_property.type_name, show_text=True)}}
    {%- endif -%}
    {%- if sub_property is deprecated  -%}
    {%- if config.template_md_options.allow_html -%}
    <s>
    {%- else -%}
    ~~
    {%- endif -%}
    {%- endif -%}
    {%- if 'Property' in config.template_md_options.heading_leading_badges -%}
        {%- if sub_property.is_pattern_property %}Pattern{% endif %} Property
    {%- endif -%}
    {%- if config.template_md_options.allow_html -%}
        <code>
    {%- endif -%}    
    {% with schema=sub_property %} {% include "breadcrumbs.md" %} {% endwith %}
    {%- if config.template_md_options.allow_html -%}
        </code>
    {%- endif -%}
    {%- if sub_property is deprecated  -%}
    {%- if config.template_md_options.allow_html -%}
    </s>
    {%- else -%}
    ~~
    {%- endif -%}
    {%- endif -%}
    {%- if 'Required' in config.template_md_options.heading_trailing_badges and not skip_required and sub_property.property_name -%}
        {{ md_badge("Required", "blue", show_text=True) if sub_property.is_required_property else md_badge("Optional", "yellow", show_text=True) }}
    {%- endif -%}
    {%- if 'Type' in config.template_md_options.heading_trailing_badges -%}
        {{ md_badge("type", None, sub_property.type_name, show_text=True)}}
    {%- endif -%}
    {%- endfilter %}
  {%- endfilter %}
  
  {% if sub_property.is_pattern_property %}
> All properties whose name matches the regular expression
```{{ sub_property.property_name }}``` ([Test](https://regex101.com/?regex={{ sub_property.property_name | urlencode }}))
must respect the following conditions
  {% endif %}

</summary>
<blockquote>

  {% with schema=sub_property, skip_headers=False, depth=depth+1 %}
    {% include "content.md" %}
  {% endwith %}

</blockquote>
</details>

{% endfor %}