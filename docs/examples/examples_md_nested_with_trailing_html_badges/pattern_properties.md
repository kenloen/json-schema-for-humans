# Person

- [1. <code> Person > firstName </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#firstName)
- [2. <code> Person > lastName </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#lastName)
- [3. <code> Person > paperSize </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#pattern1)
  - [3.1. <code> Person > paperSize > rating </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868">](#pattern1_rating)
  - [3.2. <code> Person > paperSize > review </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#pattern1_review)

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
<strong> <a name="pattern1"></a>3. <code> Person > paperSize </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  
> All properties whose name matches the regular expression
```$[a-c][0-9]^``` ([Test](https://regex101.com/?regex=%24%5Ba-c%5D%5B0-9%5D%5E))
must respect the following conditions

</summary>
<blockquote>

**Title:** paperSize

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** Review of a paper size.

<details>
<summary>
<strong> <a name="pattern1_rating"></a>3.1. <code> Person > paperSize > rating </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868"></strong>  

</summary>
<blockquote>

**Title:** Rating

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Numerical rating for paper size.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="pattern1_review"></a>3.2. <code> Person > paperSize > review </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

**Title:** Review

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Narrative review of the paper size.

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)