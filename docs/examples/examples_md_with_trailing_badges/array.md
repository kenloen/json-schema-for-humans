# Schema Docs

- [1. `root > fruits` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of string](https://img.shields.io/badge/type-array%20of%20string-6672b1)](#fruits)
  - [1.1. root > fruits > fruits items](#fruits_items)
- [2. `root > vegetables` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array](https://img.shields.io/badge/type-array-8172b3)](#vegetables)
  - [2.1. root > vegetables > veggie](#vegetables_items)
    - [2.1.1. `root > vegetables > vegetables items > veggieName` ![type: string](https://img.shields.io/badge/type-string-4c72b0)](#vegetables_items_veggieName)
    - [2.1.2. `root > vegetables > vegetables items > veggieLike` ![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#vegetables_items_veggieLike)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** A schema with an array

| Property                     | Pattern | Type            | Deprecated | Definition | Title/Description |
| ---------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| - [fruits](#fruits )         | No      | array of string | No         | -          | -                 |
| - [vegetables](#vegetables ) | No      | array           | No         | -          | -                 |

## <a name="fruits"></a>1. `root > fruits` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of string](https://img.shields.io/badge/type-array%20of%20string-6672b1)

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

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

## <a name="vegetables"></a>2. `root > vegetables` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array](https://img.shields.io/badge/type-array-8172b3)

|          |         |
| -------- | ------- |
| **Type** | `array` |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [veggie](#vegetables_items)     | -           |

### <a name="vegetables_items"></a>2.1. root > vegetables > veggie

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/veggie                                                                                                              |

| Property                                      | Pattern | Type    | Deprecated | Definition | Title/Description          |
| --------------------------------------------- | ------- | ------- | ---------- | ---------- | -------------------------- |
| + [veggieName](#vegetables_items_veggieName ) | No      | string  | No         | -          | The name of the vegetable. |
| + [veggieLike](#vegetables_items_veggieLike ) | No      | boolean | No         | -          | Do I like this vegetable?  |

#### <a name="vegetables_items_veggieName"></a>2.1.1. `root > vegetables > vegetables items > veggieName` ![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The name of the vegetable.

#### <a name="vegetables_items_veggieLike"></a>2.1.2. `root > vegetables > vegetables items > veggieLike` ![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

**Description:** Do I like this vegetable?

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
