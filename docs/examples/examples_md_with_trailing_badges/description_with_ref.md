# Schema Docs

- [1. `root > outer` ![Required](https://img.shields.io/badge/Required-blue)![type: object](https://img.shields.io/badge/type-object-c44e52)](#outer)
  - [1.1. `root > outer > inner` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#outer_inner)
- [2. `root > outer2` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#outer2)

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

| Property             | Pattern | Type   | Deprecated | Definition                    | Title/Description      |
| -------------------- | ------- | ------ | ---------- | ----------------------------- | ---------------------- |
| + [outer](#outer )   | No      | object | No         | In #/definitions/inner schema | We should see this     |
| - [outer2](#outer2 ) | No      | object | No         | Same as [outer](#outer )      | We should see this too |

## <a name="outer"></a>1. `root > outer` ![Required](https://img.shields.io/badge/Required-blue)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/inner schema                                                                               |

**Description:** We should see this

| Property                 | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [inner](#outer_inner ) | No      | string | No         | -          | inner description |

### <a name="outer_inner"></a>1.1. `root > outer > inner` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** inner description

## <a name="outer2"></a>2. `root > outer2` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |
| **Same definition as**    | [outer](#outer)                                                                                          |

**Description:** We should see this too

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
