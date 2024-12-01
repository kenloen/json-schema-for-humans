# Schema Docs

- [1. `root > name` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#name)
- [2. `root > alignment` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#alignment)

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

| Property                   | Pattern | Type   | Deprecated | Definition                     | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ------------------------------ | ----------------- |
| - [name](#name )           | No      | string | No         | In #/definitions/filled_string | a filled string   |
| - [alignment](#alignment ) | No      | string | No         | Same as [name](#name )         | a filled string   |

## <a name="name"></a>1. `root > name` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `string`                    |
| **Defined in** | #/definitions/filled_string |

**Description:** a filled string

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="alignment"></a>2. `root > alignment` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|                        |               |
| ---------------------- | ------------- |
| **Type**               | `string`      |
| **Same definition as** | [name](#name) |

**Description:** a filled string

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
