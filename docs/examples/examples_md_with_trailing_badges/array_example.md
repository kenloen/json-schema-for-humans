# Schema Docs

- [1. `root > fruits` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of string](https://img.shields.io/badge/type-array%20of%20string-6672b1)](#fruits)
  - [1.1. root > fruits > fruits items](#fruits_items)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** A schema with an array

| Property             | Pattern | Type            | Deprecated | Definition | Title/Description |
| -------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| - [fruits](#fruits ) | No      | array of string | No         | -          | -                 |

## <a name="fruits"></a>1. `root > fruits` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of string](https://img.shields.io/badge/type-array%20of%20string-6672b1)

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

**Example:** 

```json
[
    "apple",
    "banana"
]
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [fruits items](#fruits_items)   | -           |

### <a name="fruits_items"></a>1.1. root > fruits > fruits items

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Example:** 

```json
"apple"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
