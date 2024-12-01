# JSON Schema for Humans configuration file

- [1. `JSON Schema for Humans configuration file > minify` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#minify)
- [2. `JSON Schema for Humans configuration file > description_is_markdown` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#description_is_markdown)
- [3. `JSON Schema for Humans configuration file > expand_buttons` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#expand_buttons)
- [4. `JSON Schema for Humans configuration file > show_breadcrumbs` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#show_breadcrumbs)
- [5. `JSON Schema for Humans configuration file > collapse_long_descriptions` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#collapse_long_descriptions)
- [6. `JSON Schema for Humans configuration file > collapse_long_examples` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#collapse_long_examples)
- [7. `JSON Schema for Humans configuration file > link_to_reused_ref` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#link_to_reused_ref)
- [8. `JSON Schema for Humans configuration file > recursive_detection_depth` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer](https://img.shields.io/badge/type-integer-55a868)](#recursive_detection_depth)
- [9. ~~ `JSON Schema for Humans configuration file > deprecated_from_description` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#deprecated_from_description)
- [10. `JSON Schema for Humans configuration file > default_from_description` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#default_from_description)
- [11. `JSON Schema for Humans configuration file > copy_css` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#copy_css)
- [12. `JSON Schema for Humans configuration file > copy_js` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#copy_js)
- [13. ~~ `JSON Schema for Humans configuration file > templates_directory` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#templates_directory)
- [14. `JSON Schema for Humans configuration file > template_name` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: enum (of string)](https://img.shields.io/badge/type-enum%20%28of%20string%29-4c72b0)](#template_name)
- [15. `JSON Schema for Humans configuration file > custom_template_path` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#custom_template_path)
- [16. `JSON Schema for Humans configuration file > show_toc` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#show_toc)
- [17. `JSON Schema for Humans configuration file > examples_as_yaml` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#examples_as_yaml)
- [18. `JSON Schema for Humans configuration file > old_anchor_links` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#old_anchor_links)
- [19. `JSON Schema for Humans configuration file > markdown_options` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#markdown_options)
- [20. `JSON Schema for Humans configuration file > template_md_options` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#template_md_options)
  - [20.1. `JSON Schema for Humans configuration file > template_md_options > badge_as_image` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#template_md_options_badge_as_image)
  - [20.2. `JSON Schema for Humans configuration file > template_md_options > allow_html` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#template_md_options_allow_html)
  - [20.3. `JSON Schema for Humans configuration file > template_md_options > show_heading_numbers` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#template_md_options_show_heading_numbers)
  - [20.4. `JSON Schema for Humans configuration file > template_md_options > heading_leading_badges` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of enum (of string)](https://img.shields.io/badge/type-array%20of%20enum%20%28of%20string%29-6672b1)](#template_md_options_heading_leading_badges)
    - [20.4.1. JSON Schema for Humans configuration file > template_md_options > heading_leading_badges > heading_leading_badges items](#template_md_options_heading_leading_badges_items)
  - [20.5. `JSON Schema for Humans configuration file > template_md_options > heading_trailing_badges` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of enum (of string)](https://img.shields.io/badge/type-array%20of%20enum%20%28of%20string%29-6672b1)](#template_md_options_heading_trailing_badges)
    - [20.5.1. JSON Schema for Humans configuration file > template_md_options > heading_trailing_badges > heading_trailing_badges items](#template_md_options_heading_trailing_badges_items)
  - [20.6. `JSON Schema for Humans configuration file > template_md_options > show_array_restrictions` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#template_md_options_show_array_restrictions)
  - [20.7. `JSON Schema for Humans configuration file > template_md_options > properties_table_columns` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of enum (of string)](https://img.shields.io/badge/type-array%20of%20enum%20%28of%20string%29-6672b1)](#template_md_options_properties_table_columns)
    - [20.7.1. JSON Schema for Humans configuration file > template_md_options > properties_table_columns > properties_table_columns items](#template_md_options_properties_table_columns_items)
- [21. `JSON Schema for Humans configuration file > with_footer` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#with_footer)
- [22. `JSON Schema for Humans configuration file > footer_show_time` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#footer_show_time)

**Title:** JSON Schema for Humans configuration file

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** Choose how to generate JSON Schema for Humans documentation file.

Configuration parameters can be provided in several ways:

- On the CLI using `--config parameter_name=value` (example: `--config template_name=flat`)
- On the CLI using a config file `--config-file config.json`
- From code, by providing a GenerationConfiguration object to the called generation method.

| Property                                                       | Pattern | Type             | Deprecated                                                 | Definition | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------- | ------- | ---------------- | ---------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [minify](#minify )                                           | No      | boolean          | No                                                         | -          | Minify the output HTML document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [description_is_markdown](#description_is_markdown )         | No      | boolean          | No                                                         | -          | Whether to consider the description as markdown and render it accordingly.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - [expand_buttons](#expand_buttons )                           | No      | boolean          | No                                                         | -          | Add an \`Expand all\` and a \`Collapse all\` button at the top of the generated documentation.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [show_breadcrumbs](#show_breadcrumbs )                       | No      | boolean          | No                                                         | -          | For each property, show the relative place of that property in the schema.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - [collapse_long_descriptions](#collapse_long_descriptions )   | No      | boolean          | No                                                         | -          | If a description is considered big, show only the beginning and add a \`Read more\` button.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [collapse_long_examples](#collapse_long_examples )           | No      | boolean          | No                                                         | -          | If an example is considered big, collapse it, it can be displayed with a \`Show\` option.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [link_to_reused_ref](#link_to_reused_ref )                   | No      | boolean          | No                                                         | -          | If several \`$ref\` points to the same definition, only render the documentation for this definition the first time. All other occurrences are replaced by an anchor link to the first occurrence. The first occurrence is the one that is the least nested from the top of the schema and appears first in that nesting level.<br /><br />*Note*: If this option is off and the schema contains recursive definitions, the generation will crash!                                                                     |
| - [recursive_detection_depth](#recursive_detection_depth )     | No      | integer          | No                                                         | -          | *Advanced option*<br />If \`link_to_reused_ref\` is false and a \`$ref\` in the schema refers to a parent of itself, we would get a \`RecursionError\` trying to render the documentation. To avoid this, each reference is checked for circular references.<br /><br />This option determines the number of times to recursively follow definitions looking for a circular reference.<br /><br />In other words, if a schema has a deeply nested element that refers to itself, this option may need to be increased. |
| - [deprecated_from_description](#deprecated_from_description ) | No      | boolean          | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | Mark a property as deprecated (with a big red badge) if the description contains the string \`[Deprecated\`.                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [default_from_description](#default_from_description )       | No      | boolean          | No                                                         | -          | Extract the default value of a property from the description like this: \`\`[Default \`the_default_value\`]\`\`.<br /><br />The default value from the "default" attribute will be used in priority.                                                                                                                                                                                                                                                                                                                   |
| - [copy_css](#copy_css )                                       | No      | boolean          | No                                                         | -          | Copy \`schema_doc.css\` to the same directory as \`RESULT_FILE\` after generation.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [copy_js](#copy_js )                                         | No      | boolean          | No                                                         | -          | Copy \`schema_doc.min.js\` to the same directory as \`RESULT_FILE\` after generation.<br /><br />This file contains the logic for the anchor links.                                                                                                                                                                                                                                                                                                                                                                    |
| - [templates_directory](#templates_directory )                 | No      | string           | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | [Deprecated]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [template_name](#template_name )                             | No      | enum (of string) | No                                                         | -          | The name of the built-in template to use to render the documentation.<br /><br />\`js\` is the default and uses javascript for anchor links, collapsible sections and tabs.<br /><br />\`js_offline\` is identical to \`js\` except that all CSS, fonts and JavaScript are bundled for offline use.<br /><br />\`flat\` uses no javascript, but has no interactivity.<br /><br />\`md\` is the markdown template.<br /><br />\`md_nested\` is the markdown template with collapsible nested sections.                  |
| - [custom_template_path](#custom_template_path )               | No      | string           | No                                                         | -          | Path to a custom Jinja2 template file.<br /><br />There can be multiple files to split the template, but this path should be the entry point.<br /><br />If no output file is specified, the extension of the template file will be used to determine the output documentation extension. i.e. if the template is in ./custom_template/content.html, the resulting documentation will have the html extension.                                                                                                         |
| - [show_toc](#show_toc )                                       | No      | boolean          | No                                                         | -          | Whether to render table of contents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [examples_as_yaml](#examples_as_yaml )                       | No      | boolean          | No                                                         | -          | Whether to display examples as YAML instead of JSON                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [old_anchor_links](#old_anchor_links )                       | No      | boolean          | No                                                         | -          | Generate HTML ids for anchor links without special characters (keep only letters, digits, \`_\`, and \`-\`).<br /><br />This is the old behaviour and is only needed for browsers that do not support HTML 5.                                                                                                                                                                                                                                                                                                          |
| - [markdown_options](#markdown_options )                       | No      | object           | No                                                         | -          | [Markdown 2 options](https://github.com/trentm/python-markdown2/wiki/Extras) for the descriptions. \`description_is_markdown\` must be true for this to have any effect.<br /><br />**WARNING**<br />Adding an extra, even if the value is false, will activate it. For example \`{"break-on-newline": false}\` will activate the \`break-on-newline\` extra.                                                                                                                                                          |
| - [template_md_options](#template_md_options )                 | No      | object           | No                                                         | -          | specific options to md template                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [with_footer](#with_footer )                                 | No      | boolean          | No                                                         | -          | Whether to show the footer linking to the library repo and with the generation datetime                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [footer_show_time](#footer_show_time )                       | No      | boolean          | No                                                         | -          | Whether the footer should display the generation time                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## <a name="minify"></a>1. `JSON Schema for Humans configuration file > minify` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** Minify the output HTML document.

## <a name="description_is_markdown"></a>2. `JSON Schema for Humans configuration file > description_is_markdown` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** Whether to consider the description as markdown and render it accordingly.

## <a name="expand_buttons"></a>3. `JSON Schema for Humans configuration file > expand_buttons` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `false`   |

**Description:** Add an `Expand all` and a `Collapse all` button at the top of the generated documentation.

## <a name="show_breadcrumbs"></a>4. `JSON Schema for Humans configuration file > show_breadcrumbs` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** For each property, show the relative place of that property in the schema.

## <a name="collapse_long_descriptions"></a>5. `JSON Schema for Humans configuration file > collapse_long_descriptions` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** If a description is considered big, show only the beginning and add a `Read more` button.

## <a name="collapse_long_examples"></a>6. `JSON Schema for Humans configuration file > collapse_long_examples` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** If an example is considered big, collapse it, it can be displayed with a `Show` option.

## <a name="link_to_reused_ref"></a>7. `JSON Schema for Humans configuration file > link_to_reused_ref` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** If several `$ref` points to the same definition, only render the documentation for this definition the first time. All other occurrences are replaced by an anchor link to the first occurrence. The first occurrence is the one that is the least nested from the top of the schema and appears first in that nesting level.

*Note*: If this option is off and the schema contains recursive definitions, the generation will crash!

## <a name="recursive_detection_depth"></a>8. `JSON Schema for Humans configuration file > recursive_detection_depth` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer](https://img.shields.io/badge/type-integer-55a868)

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `25`      |

**Description:** *Advanced option*
If `link_to_reused_ref` is false and a `$ref` in the schema refers to a parent of itself, we would get a `RecursionError` trying to render the documentation. To avoid this, each reference is checked for circular references.

This option determines the number of times to recursively follow definitions looking for a circular reference.

In other words, if a schema has a deeply nested element that refers to itself, this option may need to be increased.

## <a name="deprecated_from_description"></a>9. ~~ `JSON Schema for Humans configuration file > deprecated_from_description` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|                |                                                            |
| -------------- | ---------------------------------------------------------- |
| **Type**       | `boolean`                                                  |
| **Deprecated** | ![Deprecated](https://img.shields.io/badge/Deprecated-red) |
| **Default**    | `false`                                                    |

**Description:** Mark a property as deprecated (with a big red badge) if the description contains the string `[Deprecated`.

## <a name="default_from_description"></a>10. `JSON Schema for Humans configuration file > default_from_description` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `false`   |

**Description:** Extract the default value of a property from the description like this: ``[Default `the_default_value`]``.

The default value from the "default" attribute will be used in priority.

## <a name="copy_css"></a>11. `JSON Schema for Humans configuration file > copy_css` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** Copy `schema_doc.css` to the same directory as `RESULT_FILE` after generation.

## <a name="copy_js"></a>12. `JSON Schema for Humans configuration file > copy_js` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** Copy `schema_doc.min.js` to the same directory as `RESULT_FILE` after generation.

This file contains the logic for the anchor links.

## <a name="templates_directory"></a>13. ~~ `JSON Schema for Humans configuration file > templates_directory` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|                |                                                            |
| -------------- | ---------------------------------------------------------- |
| **Type**       | `string`                                                   |
| **Deprecated** | ![Deprecated](https://img.shields.io/badge/Deprecated-red) |

**Description:** [Deprecated]

## <a name="template_name"></a>14. `JSON Schema for Humans configuration file > template_name` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: enum (of string)](https://img.shields.io/badge/type-enum%20%28of%20string%29-4c72b0)

|             |                    |
| ----------- | ------------------ |
| **Type**    | `enum (of string)` |
| **Default** | `"js"`             |

**Description:** The name of the built-in template to use to render the documentation.

`js` is the default and uses javascript for anchor links, collapsible sections and tabs.

`js_offline` is identical to `js` except that all CSS, fonts and JavaScript are bundled for offline use.

`flat` uses no javascript, but has no interactivity.

`md` is the markdown template.

`md_nested` is the markdown template with collapsible nested sections.

Must be one of:
* "flat"
* "js"
* "js_offline"
* "md"
* "md_nested"

## <a name="custom_template_path"></a>15. `JSON Schema for Humans configuration file > custom_template_path` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|             |          |
| ----------- | -------- |
| **Type**    | `string` |
| **Default** | `null`   |

**Description:** Path to a custom Jinja2 template file.

There can be multiple files to split the template, but this path should be the entry point.

If no output file is specified, the extension of the template file will be used to determine the output documentation extension. i.e. if the template is in ./custom_template/content.html, the resulting documentation will have the html extension.

## <a name="show_toc"></a>16. `JSON Schema for Humans configuration file > show_toc` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** Whether to render table of contents.

## <a name="examples_as_yaml"></a>17. `JSON Schema for Humans configuration file > examples_as_yaml` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `false`   |

**Description:** Whether to display examples as YAML instead of JSON

## <a name="old_anchor_links"></a>18. `JSON Schema for Humans configuration file > old_anchor_links` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `false`   |

**Description:** Generate HTML ids for anchor links without special characters (keep only letters, digits, `_`, and `-`).

This is the old behaviour and is only needed for browsers that do not support HTML 5.

## <a name="markdown_options"></a>19. `JSON Schema for Humans configuration file > markdown_options` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `{"fenced-code-blocks": {"cssclass": "highlight jumbotron"}, "tables": null, "break-on-newline": true}`                           |

**Description:** [Markdown 2 options](https://github.com/trentm/python-markdown2/wiki/Extras) for the descriptions. `description_is_markdown` must be true for this to have any effect.

**WARNING**
Adding an extra, even if the value is false, will activate it. For example `{"break-on-newline": false}` will activate the `break-on-newline` extra.

**Example:** 

```json
{
    "fenced-code-blocks": {
        "cssclass": "highlight jumbotron"
    },
    "tables": null,
    "break-on-newline": true,
    "cuddled-lists": true
}
```

## <a name="template_md_options"></a>20. `JSON Schema for Humans configuration file > template_md_options` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** specific options to md template

| Property                                                                     | Pattern | Type                      | Deprecated | Definition | Title/Description                                                                                                                                                                            |
| ---------------------------------------------------------------------------- | ------- | ------------------------- | ---------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [badge_as_image](#template_md_options_badge_as_image )                     | No      | boolean                   | No         | -          | if true generate badges(eg: optional, required) using embedded image (https://img.shields.io).<br /><br /> if false, use text instead                                                        |
| - [allow_html](#template_md_options_allow_html )                             | No      | boolean                   | No         | -          | for \`md_nested\` the heading is with an HTML \`<details>\` which do not allow markdown but it is possible to use HTML instead. Fx. the badges can be renderned a HTML \`<img ..>\` instead. |
| - [show_heading_numbers](#template_md_options_show_heading_numbers )         | No      | boolean                   | No         | -          | if true generate heading numbers to correspond to table of contents.<br /><br /> if false, do not generate heading numbers                                                                   |
| - [heading_leading_badges](#template_md_options_heading_leading_badges )     | No      | array of enum (of string) | No         | -          | Badges or bracket names to be included before heading                                                                                                                                        |
| - [heading_trailing_badges](#template_md_options_heading_trailing_badges )   | No      | array of enum (of string) | No         | -          | Badges or bracket names to be included after heading                                                                                                                                         |
| - [show_array_restrictions](#template_md_options_show_array_restrictions )   | No      | boolean                   | No         | -          | if true generate array restrictions section.<br /><br /> if false, do not generate                                                                                                           |
| - [properties_table_columns](#template_md_options_properties_table_columns ) | No      | array of enum (of string) | No         | -          | array of column names to display in the properties table.<br /><br /> if empty, the default is ['Property','Pattern','Type','Deprecated','Definition','Title/Description']                   |

### <a name="template_md_options_badge_as_image"></a>20.1. `JSON Schema for Humans configuration file > template_md_options > badge_as_image` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `false`   |

**Description:** if true generate badges(eg: optional, required) using embedded image (https://img.shields.io).

 if false, use text instead

### <a name="template_md_options_allow_html"></a>20.2. `JSON Schema for Humans configuration file > template_md_options > allow_html` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `false`   |

**Description:** for `md_nested` the heading is with an HTML `<details>` which do not allow markdown but it is possible to use HTML instead. Fx. the badges can be renderned a HTML `<img ..>` instead.

### <a name="template_md_options_show_heading_numbers"></a>20.3. `JSON Schema for Humans configuration file > template_md_options > show_heading_numbers` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** if true generate heading numbers to correspond to table of contents.

 if false, do not generate heading numbers

### <a name="template_md_options_heading_leading_badges"></a>20.4. `JSON Schema for Humans configuration file > template_md_options > heading_leading_badges` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of enum (of string)](https://img.shields.io/badge/type-array%20of%20enum%20%28of%20string%29-6672b1)

|             |                             |
| ----------- | --------------------------- |
| **Type**    | `array of enum (of string)` |
| **Default** | `["Required", "Property"]`  |

**Description:** Badges or bracket names to be included before heading

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                   | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [heading_leading_badges items](#template_md_options_heading_leading_badges_items) | -           |

#### <a name="template_md_options_heading_leading_badges_items"></a>20.4.1. JSON Schema for Humans configuration file > template_md_options > heading_leading_badges > heading_leading_badges items

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "Required"
* "Property"
* "Type"

### <a name="template_md_options_heading_trailing_badges"></a>20.5. `JSON Schema for Humans configuration file > template_md_options > heading_trailing_badges` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of enum (of string)](https://img.shields.io/badge/type-array%20of%20enum%20%28of%20string%29-6672b1)

|             |                             |
| ----------- | --------------------------- |
| **Type**    | `array of enum (of string)` |
| **Default** | `[]`                        |

**Description:** Badges or bracket names to be included after heading

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                     | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [heading_trailing_badges items](#template_md_options_heading_trailing_badges_items) | -           |

#### <a name="template_md_options_heading_trailing_badges_items"></a>20.5.1. JSON Schema for Humans configuration file > template_md_options > heading_trailing_badges > heading_trailing_badges items

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "Required"
* "Type"

### <a name="template_md_options_show_array_restrictions"></a>20.6. `JSON Schema for Humans configuration file > template_md_options > show_array_restrictions` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** if true generate array restrictions section.

 if false, do not generate

### <a name="template_md_options_properties_table_columns"></a>20.7. `JSON Schema for Humans configuration file > template_md_options > properties_table_columns` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of enum (of string)](https://img.shields.io/badge/type-array%20of%20enum%20%28of%20string%29-6672b1)

|          |                             |
| -------- | --------------------------- |
| **Type** | `array of enum (of string)` |

**Description:** array of column names to display in the properties table.

 if empty, the default is ['Property','Pattern','Type','Deprecated','Definition','Title/Description']

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                       | Description |
| ------------------------------------------------------------------------------------- | ----------- |
| [properties_table_columns items](#template_md_options_properties_table_columns_items) | -           |

#### <a name="template_md_options_properties_table_columns_items"></a>20.7.1. JSON Schema for Humans configuration file > template_md_options > properties_table_columns > properties_table_columns items

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "Property"
* "Pattern"
* "Type"
* "Deprecated"
* "Definition"
* "Title/Description"

## <a name="with_footer"></a>21. `JSON Schema for Humans configuration file > with_footer` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** Whether to show the footer linking to the library repo and with the generation datetime

## <a name="footer_show_time"></a>22. `JSON Schema for Humans configuration file > footer_show_time` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `true`    |

**Description:** Whether the footer should display the generation time

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
