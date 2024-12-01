# Person

- [1. `Person > firstName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#firstName)
- [2. `Person > lastName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#lastName)
- [3. `Person > age` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer](https://img.shields.io/badge/type-integer-55a868)](#age)
- [4. `Person > driverLicenseId` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#driverLicenseId)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1)

**Title:** Person

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                               | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [firstName](#firstName )             | No      | string      | No         | -          | Person            |
| - [lastName](#lastName )               | No      | string      | No         | -          | Person            |
| - [age](#age )                         | No      | integer     | No         | -          | Person            |
| - [driverLicenseId](#driverLicenseId ) | No      | Combination | No         | -          | -                 |

## <a name="firstName"></a>1. `Person > firstName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

**Title:** Person

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's first name.

## <a name="lastName"></a>2. `Person > lastName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

**Title:** Person

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's last name.

## <a name="age"></a>3. `Person > age` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer](https://img.shields.io/badge/type-integer-55a868)

**Title:** Person

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="driverLicenseId"></a>4. `Person > driverLicenseId` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                       |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| All of(Requirement)                            |
| ---------------------------------------------- |
| [no driver licence](#driverLicenseId_allOf_i0) |
| [driver licence id](#driverLicenseId_allOf_i1) |

### <a name="driverLicenseId_allOf_i0"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`

**Title:** no driver licence

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="driverLicenseId_allOf_i1"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`

**Title:** driver licence id

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
