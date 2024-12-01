# Person

- [1. `Person > firstName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#firstName)
- [2. `Person > lastName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string or null](https://img.shields.io/badge/type-string%20or%20null-8c9592)](#lastName)
- [3. `Person > age` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer or number](https://img.shields.io/badge/type-integer%20or%20number-99965d)](#age)
- [4. `Person > anything` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer, string, number or null](https://img.shields.io/badge/type-integer%2C%20string%2C%20number%20or%20null-929577)](#anything)

**Title:** Person

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                   | Pattern | Type                            | Deprecated | Definition | Title/Description                                         |
| -------------------------- | ------- | ------------------------------- | ---------- | ---------- | --------------------------------------------------------- |
| - [firstName](#firstName ) | No      | string                          | No         | -          | The person's first name.                                  |
| - [lastName](#lastName )   | No      | string or null                  | No         | -          | The person's last name.                                   |
| - [age](#age )             | No      | integer or number               | No         | -          | Age in years which must be equal to or greater than zero. |
| - [anything](#anything )   | No      | integer, string, number or null | No         | -          | Ay other info you like                                    |

## <a name="firstName"></a>1. `Person > firstName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's first name.

## <a name="lastName"></a>2. `Person > lastName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string or null](https://img.shields.io/badge/type-string%20or%20null-8c9592)

|          |                  |
| -------- | ---------------- |
| **Type** | `string or null` |

**Description:** The person's last name.

## <a name="age"></a>3. `Person > age` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer or number](https://img.shields.io/badge/type-integer%20or%20number-99965d)

|          |                     |
| -------- | ------------------- |
| **Type** | `integer or number` |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="anything"></a>4. `Person > anything` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: integer, string, number or null](https://img.shields.io/badge/type-integer%2C%20string%2C%20number%20or%20null-929577)

|          |                                   |
| -------- | --------------------------------- |
| **Type** | `integer, string, number or null` |

**Description:** Ay other info you like

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
