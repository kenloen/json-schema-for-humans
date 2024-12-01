# Schema Docs

- [1. ~~ `root > deprecated1` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#deprecated1)
- [2. ~~ `root > deprecated2` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#deprecated2)
- [3. ~~ `root > deprecated3` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#deprecated3)
- [4. ~~ `root > deprecated4` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#deprecated4)
- [5. `root > not_deprecated` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#not_deprecated)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** Test schema with deprecated in description

| Property                             | Pattern | Type   | Deprecated                                                 | Definition | Title/Description                                     |
| ------------------------------------ | ------- | ------ | ---------------------------------------------------------- | ---------- | ----------------------------------------------------- |
| - [deprecated1](#deprecated1 )       | No      | object | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | [Deprecated]                                          |
| - [deprecated2](#deprecated2 )       | No      | object | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | [Deprecated - Use \`not_deprecated\` instead]         |
| - [deprecated3](#deprecated3 )       | No      | object | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | This is [Deprecated]                                  |
| - [deprecated4](#deprecated4 )       | No      | object | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | This is [Deprecated - Use \`not_deprecated\` instead] |
| - [not_deprecated](#not_deprecated ) | No      | string | No                                                         | -          | -                                                     |

## <a name="deprecated1"></a>1. ~~ `root > deprecated1` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Deprecated**            | ![Deprecated](https://img.shields.io/badge/Deprecated-red)                                                                        |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** [Deprecated]

## <a name="deprecated2"></a>2. ~~ `root > deprecated2` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Deprecated**            | ![Deprecated](https://img.shields.io/badge/Deprecated-red)                                                                        |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** [Deprecated - Use `not_deprecated` instead]

## <a name="deprecated3"></a>3. ~~ `root > deprecated3` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Deprecated**            | ![Deprecated](https://img.shields.io/badge/Deprecated-red)                                                                        |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** This is [Deprecated]

## <a name="deprecated4"></a>4. ~~ `root > deprecated4` ~~![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Deprecated**            | ![Deprecated](https://img.shields.io/badge/Deprecated-red)                                                                        |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** This is [Deprecated - Use `not_deprecated` instead]

## <a name="not_deprecated"></a>5. `root > not_deprecated` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
