# Schema Docs

- [1. <code> root > billing_address </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#billing_address)
  - [1.1. <code> root > billing_address > street_address </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#billing_address_street_address)
  - [1.2. <code> root > billing_address > city </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#billing_address_city)
  - [1.3. <code> root > billing_address > state </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#billing_address_state)
  - [1.4. <code> root > billing_address > futureProperty </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-null-ccb974">](#billing_address_futureProperty)
- [2. <code> root > shipping_address </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#shipping_address)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary>
<strong> <a name="billing_address"></a>1. <code> root > billing_address </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/address                                                                                                             |

<details>
<summary>
<strong> <a name="billing_address_street_address"></a>1.1. <code> root > billing_address > street_address </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="billing_address_city"></a>1.2. <code> root > billing_address > city </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="billing_address_state"></a>1.3. <code> root > billing_address > state </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="billing_address_futureProperty"></a>1.4. <code> root > billing_address > futureProperty </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-null-ccb974"></strong>  

</summary>
<blockquote>

|          |        |
| -------- | ------ |
| **Type** | `null` |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="shipping_address"></a>2. <code> root > shipping_address </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [billing_address](#billing_address)                                                                                               |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)