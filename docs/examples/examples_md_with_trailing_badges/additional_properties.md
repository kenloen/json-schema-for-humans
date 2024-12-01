# Person

- [1. `Person > subType1` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#subType1)
  - [1.1. `Person > subType1 > subProp1` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: number](https://img.shields.io/badge/type-number-dd8452)](#subType1_subProp1)
- [2. `Person > subType2` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#subType2)
  - [2.1. `Person > subType2 > subProp2` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: number](https://img.shields.io/badge/type-number-dd8452)](#subType2_subProp2)
- [3. `Person > anInt` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer](https://img.shields.io/badge/type-integer-55a868)](#anInt)
- [4. `Person > additionalProperties` ![type: object](https://img.shields.io/badge/type-object-c44e52)](#additionalProperties)
  - [4.1. `Person > additionalProperties > propA` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: number](https://img.shields.io/badge/type-number-dd8452)](#additionalProperties_propA)

**Title:** Person

|                           |                                                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                                     |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#additionalProperties "Each additional property must conform to the following schema") |

| Property                     | Pattern | Type    | Deprecated | Definition | Title/Description                                                          |
| ---------------------------- | ------- | ------- | ---------- | ---------- | -------------------------------------------------------------------------- |
| - [subType1](#subType1 )     | No      | object  | No         | -          | A sub type with additionalProperties false.                                |
| - [subType2](#subType2 )     | No      | object  | No         | -          | A sub type with additionalProperties true.                                 |
| - [anInt](#anInt )           | No      | integer | No         | -          | This is an integer, it should not show additional properties. (issue #132) |
| - [](#additionalProperties ) | No      | object  | No         | -          | additionalProperties schema.                                               |

## <a name="subType1"></a>1. `Person > subType1` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

**Description:** A sub type with additionalProperties false.

| Property                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [subProp1](#subType1_subProp1 ) | No      | number | No         | -          | -                 |

### <a name="subType1_subProp1"></a>1.1. `Person > subType1 > subProp1` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: number](https://img.shields.io/badge/type-number-dd8452)

|          |          |
| -------- | -------- |
| **Type** | `number` |

## <a name="subType2"></a>2. `Person > subType2` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** A sub type with additionalProperties true.

| Property                              | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [subProp2](#subType2_subProp2 )     | No      | number | No         | -          | -                 |
| - [](#subType2_additionalProperties ) | No      | object | No         | -          | -                 |

### <a name="subType2_subProp2"></a>2.1. `Person > subType2 > subProp2` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: number](https://img.shields.io/badge/type-number-dd8452)

|          |          |
| -------- | -------- |
| **Type** | `number` |

## <a name="anInt"></a>3. `Person > anInt` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer](https://img.shields.io/badge/type-integer-55a868)

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** This is an integer, it should not show additional properties. (issue #132)

## <a name="additionalProperties"></a>4. `Person > additionalProperties` ![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** additionalProperties schema.

| Property                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [propA](#additionalProperties_propA ) | No      | number | No         | -          | -                 |

### <a name="additionalProperties_propA"></a>4.1. `Person > additionalProperties > propA` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: number](https://img.shields.io/badge/type-number-dd8452)

|          |          |
| -------- | -------- |
| **Type** | `number` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
