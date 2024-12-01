# Schema Docs

- [1. `root > address` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#address)
  - [1.1. `root > address > street_address` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#address_street_address)
  - [1.2. `root > address > city` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#address_city)
  - [1.3. `root > address > state` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#address_state)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** Testing $ref with URL with YAML destination

| Property               | Pattern | Type   | Deprecated | Definition                                                                                                                   | Title/Description |
| ---------------------- | ------- | ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| - [address](#address ) | No      | object | No         | In https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/yaml.yaml#/definitions/address | -                 |

## <a name="address"></a>1. `root > address` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/yaml.yaml#/definitions/address         |

| Property                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [street_address](#address_street_address ) | No      | string | No         | -          | -                 |
| + [city](#address_city )                     | No      | string | No         | -          | -                 |
| + [state](#address_state )                   | No      | string | No         | -          | -                 |

### <a name="address_street_address"></a>1.1. `root > address > street_address` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="address_city"></a>1.2. `root > address > city` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="address_state"></a>1.3. `root > address > state` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
