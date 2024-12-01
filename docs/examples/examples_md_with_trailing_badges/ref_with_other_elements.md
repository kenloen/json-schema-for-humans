# OF

- [1. `OF > uuid` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#uuid)
- [2. `OF > firstName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#firstName)
- [3. `OF > lastName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#lastName)

**Title:** OF

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                   | Pattern | Type   | Deprecated | Definition          | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ------------------- | ----------------- |
| - [uuid](#uuid )           | No      | string | No         | In #/$defs/ofString | Unique Identifer  |
| - [firstName](#firstName ) | No      | string | No         | In #/$defs/ofString | first name        |
| - [lastName](#lastName )   | No      | string | No         | In #/$defs/ofString | last name         |

## <a name="uuid"></a>1. `OF > uuid` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Defined in** | #/$defs/ofString |

**Description:** Unique Identifer

**Example:** 

```json
"29292929292929292929292"
```

**Example:** 

```json
"29292929292929292929292"
```

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 5   |
| **Max length** | 250 |

## <a name="firstName"></a>2. `OF > firstName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Defined in** | #/$defs/ofString |

**Description:** first name

**Example:** 

```json
"John"
```

**Example:** 

```json
"John"
```

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 10  |
| **Max length** | 250 |

## <a name="lastName"></a>3. `OF > lastName` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Defined in** | #/$defs/ofString |

**Description:** last name

**Example:** 

```json
"Doe"
```

**Example:** 

```json
"Doe"
```

| Restrictions   |    |
| -------------- | -- |
| **Min length** | 5  |
| **Max length** | 10 |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
