# Person

- [1. <code> Person > firstName </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#firstName)
- [2. <code> Person > lastName </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#lastName)
- [3. <code> Person > age </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868">](#age)
- [4. <code> Person > driverLicenseId </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#driverLicenseId)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1)

**Title:** Person

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary>
<strong> <a name="firstName"></a>1. <code> Person > firstName </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

**Title:** Person

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's first name.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="lastName"></a>2. <code> Person > lastName </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

**Title:** Person

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's last name.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="age"></a>3. <code> Person > age </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868"></strong>  

</summary>
<blockquote>

**Title:** Person

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="driverLicenseId"></a>4. <code> Person > driverLicenseId </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                       |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<blockquote>

| All of(Requirement)                            |
| ---------------------------------------------- |
| [no driver licence](#driverLicenseId_allOf_i0) |
| [driver licence id](#driverLicenseId_allOf_i1) |

<blockquote>

### <a name="driverLicenseId_allOf_i0"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`

**Title:** no driver licence

|          |        |
| -------- | ------ |
| **Type** | `null` |

</blockquote>
<blockquote>

### <a name="driverLicenseId_allOf_i1"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`

**Title:** driver licence id

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)