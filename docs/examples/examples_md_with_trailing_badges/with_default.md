# User Preference

- [1. `User Preference > favorite_os` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: enum (of string)](https://img.shields.io/badge/type-enum%20%28of%20string%29-4c72b0)](#favorite_os)
- [2. `User Preference > favorite_colors` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of enum (of string)](https://img.shields.io/badge/type-array%20of%20enum%20%28of%20string%29-6672b1)](#favorite_colors)
  - [2.1. User Preference > favorite_colors > favorite_colors items](#favorite_colors_items)
- [3. `User Preference > desired_number_of_shoes` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer](https://img.shields.io/badge/type-integer-55a868)](#desired_number_of_shoes)

**Title:** User Preference

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                               | Pattern | Type                      | Deprecated | Definition | Title/Description |
| ------------------------------------------------------ | ------- | ------------------------- | ---------- | ---------- | ----------------- |
| - [favorite_os](#favorite_os )                         | No      | enum (of string)          | No         | -          | -                 |
| - [favorite_colors](#favorite_colors )                 | No      | array of enum (of string) | No         | -          | -                 |
| - [desired_number_of_shoes](#desired_number_of_shoes ) | No      | integer                   | No         | -          | -                 |

## <a name="favorite_os"></a>1. `User Preference > favorite_os` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: enum (of string)](https://img.shields.io/badge/type-enum%20%28of%20string%29-4c72b0)

|             |                    |
| ----------- | ------------------ |
| **Type**    | `enum (of string)` |
| **Default** | `"Linux"`          |

Must be one of:
* "Windows"
* "Mac"
* "Linux"

## <a name="favorite_colors"></a>2. `User Preference > favorite_colors` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of enum (of string)](https://img.shields.io/badge/type-array%20of%20enum%20%28of%20string%29-6672b1)

|             |                             |
| ----------- | --------------------------- |
| **Type**    | `array of enum (of string)` |
| **Default** | `["white", "blue"]`         |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [favorite_colors items](#favorite_colors_items) | -           |

### <a name="favorite_colors_items"></a>2.1. User Preference > favorite_colors > favorite_colors items

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "green"
* "blue"
* "orange"
* "red"
* "white"
* "black"

## <a name="desired_number_of_shoes"></a>3. `User Preference > desired_number_of_shoes` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer](https://img.shields.io/badge/type-integer-55a868)

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `2`       |

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 2 |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
