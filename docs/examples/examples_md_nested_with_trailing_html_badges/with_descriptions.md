# Delivery Schema

- [1. <code> Delivery Schema > shipping_address </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#shipping_address)
  - [1.1. <code> Delivery Schema > shipping_address > street_address </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#shipping_address_street_address)
  - [1.2. <code> Delivery Schema > shipping_address > city </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#shipping_address_city)
  - [1.3. <code> Delivery Schema > shipping_address > state </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#shipping_address_state)
- [2. <code> Delivery Schema > billing_address </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#billing_address)
- [3. <code> Delivery Schema > delivery_info </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#delivery_info)
  - [3.1. Property `Delivery Schema > delivery_info > oneOf > classic`](#delivery_info_oneOf_i0)
    - [3.1.1. <code> Delivery Schema > delivery_info > oneOf > item 0 > price </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-number-dd8452">](#delivery_info_oneOf_i0_price)
  - [3.2. Property `Delivery Schema > delivery_info > oneOf > gift`](#delivery_info_oneOf_i1)
    - [3.2.1. <code> Delivery Schema > delivery_info > oneOf > item 1 > with_wrap </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-boolean-da8bc3">](#delivery_info_oneOf_i1_with_wrap)

**Title:** Delivery Schema

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary>
<strong> <a name="shipping_address"></a>1. <code> Delivery Schema > shipping_address </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/address                                                                                                             |

**Description:** Exact address

<details>
<summary>
<strong> <a name="shipping_address_street_address"></a>1.1. <code> Delivery Schema > shipping_address > street_address </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="shipping_address_city"></a>1.2. <code> Delivery Schema > shipping_address > city </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="shipping_address_state"></a>1.3. <code> Delivery Schema > shipping_address > state </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="billing_address"></a>2. <code> Delivery Schema > billing_address </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [shipping_address](#shipping_address)                                                                                             |

**Description:** Exact address

</blockquote>
</details>

<details>
<summary>
<strong> <a name="delivery_info"></a>3. <code> Delivery Schema > delivery_info </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                       |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/delivery_info                                                                                                       |

**Description:** Delivery info depending on the delivery type

<blockquote>

| One of(Option)                     |
| ---------------------------------- |
| [classic](#delivery_info_oneOf_i0) |
| [gift](#delivery_info_oneOf_i1)    |

<blockquote>

### <a name="delivery_info_oneOf_i0"></a>3.1. Property `Delivery Schema > delivery_info > oneOf > classic`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/classic                                                                                                             |

<details>
<summary>
<strong> <a name="delivery_info_oneOf_i0_price"></a>3.1.1. <code> Delivery Schema > delivery_info > oneOf > item 0 > price </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-number-dd8452"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `number` |

</blockquote>
</details>

</blockquote>
<blockquote>

### <a name="delivery_info_oneOf_i1"></a>3.2. Property `Delivery Schema > delivery_info > oneOf > gift`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/gift                                                                                                                |

**Description:** The delivery is a gift, no prices displayed

<details>
<summary>
<strong> <a name="delivery_info_oneOf_i1_with_wrap"></a>3.2.1. <code> Delivery Schema > delivery_info > oneOf > item 1 > with_wrap </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-boolean-da8bc3"></strong>  

</summary>
<blockquote>

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

</blockquote>
</details>

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)