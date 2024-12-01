# Test

- [1. `Test > aProperty` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: enum (of string)](https://img.shields.io/badge/type-enum%20%28of%20string%29-4c72b0)](#aProperty)
- [2. `Test > aDictPropertyARequired` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#aDictPropertyARequired)
  - [2.1. `Test > aDictPropertyARequired > a` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#aDictPropertyARequired_a)
  - [2.2. `Test > aDictPropertyARequired > b` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#aDictPropertyARequired_b)

**Title:** Test

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                             | Pattern | Type             | Deprecated | Definition                     | Title/Description                           |
| ---------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------ | ------------------------------------------- |
| - [aProperty](#aProperty )                           | No      | enum (of string) | No         | In #/definitions/aProperty     | This is the description from the definition |
| - [aDictPropertyARequired](#aDictPropertyARequired ) | No      | object           | No         | In #/definitions/aDictProperty | -                                           |

## <a name="aProperty"></a>1. `Test > aProperty` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: enum (of string)](https://img.shields.io/badge/type-enum%20%28of%20string%29-4c72b0)

|                |                           |
| -------------- | ------------------------- |
| **Type**       | `enum (of string)`        |
| **Default**    | `"Default from property"` |
| **Defined in** | #/definitions/aProperty   |

**Description:** This is the description from the definition

Must be one of:
* "value1"
* "value2"

## <a name="aDictPropertyARequired"></a>2. `Test > aDictPropertyARequired` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `{"a": "a", "b": "b"}`                                                                                                            |
| **Defined in**            | #/definitions/aDictProperty                                                                                                       |

| Property                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [a](#aDictPropertyARequired_a ) | No      | string | No         | -          | -                 |
| + [b](#aDictPropertyARequired_b ) | No      | string | No         | -          | -                 |

### <a name="aDictPropertyARequired_a"></a>2.1. `Test > aDictPropertyARequired > a` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="aDictPropertyARequired_b"></a>2.2. `Test > aDictPropertyARequired > b` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
