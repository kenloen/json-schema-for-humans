# Delivery Schema

- [1. `Delivery Schema > shipping_address` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#shipping_address)
  - [1.1. `Delivery Schema > shipping_address > street_address` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#shipping_address_street_address)
  - [1.2. `Delivery Schema > shipping_address > city` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#shipping_address_city)
  - [1.3. `Delivery Schema > shipping_address > state` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#shipping_address_state)
- [2. `Delivery Schema > billing_address` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#billing_address)
- [3. `Delivery Schema > delivery_info` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)](#delivery_info)
  - [3.1. Property `Delivery Schema > delivery_info > oneOf > classic`](#delivery_info_oneOf_i0)
    - [3.1.1. `Delivery Schema > delivery_info > oneOf > item 0 > price` ![type: number](https://img.shields.io/badge/type-number-dd8452)](#delivery_info_oneOf_i0_price)
  - [3.2. Property `Delivery Schema > delivery_info > oneOf > gift`](#delivery_info_oneOf_i1)
    - [3.2.1. `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap` ![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)](#delivery_info_oneOf_i1_with_wrap)

**Title:** Delivery Schema

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                 | Pattern | Type   | Deprecated | Definition                                     | Title/Description                            |
| ---------------------------------------- | ------- | ------ | ---------- | ---------------------------------------------- | -------------------------------------------- |
| - [shipping_address](#shipping_address ) | No      | object | No         | In #/definitions/address                       | Exact address                                |
| - [billing_address](#billing_address )   | No      | object | No         | Same as [shipping_address](#shipping_address ) | Exact address                                |
| - [delivery_info](#delivery_info )       | No      | object | No         | In #/definitions/delivery_info                 | Delivery info depending on the delivery type |

## <a name="shipping_address"></a>1. `Delivery Schema > shipping_address` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/address                                                                                                             |

**Description:** Exact address

| Property                                              | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [street_address](#shipping_address_street_address ) | No      | string | No         | -          | -                 |
| + [city](#shipping_address_city )                     | No      | string | No         | -          | -                 |
| + [state](#shipping_address_state )                   | No      | string | No         | -          | -                 |

### <a name="shipping_address_street_address"></a>1.1. `Delivery Schema > shipping_address > street_address` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="shipping_address_city"></a>1.2. `Delivery Schema > shipping_address > city` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="shipping_address_state"></a>1.3. `Delivery Schema > shipping_address > state` ![Required](https://img.shields.io/badge/Required-blue)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="billing_address"></a>2. `Delivery Schema > billing_address` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [shipping_address](#shipping_address)                                                                                             |

**Description:** Exact address

## <a name="delivery_info"></a>3. `Delivery Schema > delivery_info` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                       |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/delivery_info                                                                                                       |

**Description:** Delivery info depending on the delivery type

| One of(Option)                     |
| ---------------------------------- |
| [classic](#delivery_info_oneOf_i0) |
| [gift](#delivery_info_oneOf_i1)    |

### <a name="delivery_info_oneOf_i0"></a>3.1. Property `Delivery Schema > delivery_info > oneOf > classic`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/classic                                                                                                             |

| Property                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [price](#delivery_info_oneOf_i0_price ) | No      | number | No         | -          | -                 |

#### <a name="delivery_info_oneOf_i0_price"></a>3.1.1. `Delivery Schema > delivery_info > oneOf > item 0 > price` ![type: number](https://img.shields.io/badge/type-number-dd8452)

|          |          |
| -------- | -------- |
| **Type** | `number` |

### <a name="delivery_info_oneOf_i1"></a>3.2. Property `Delivery Schema > delivery_info > oneOf > gift`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/gift                                                                                                                |

**Description:** The delivery is a gift, no prices displayed

| Property                                          | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [with_wrap](#delivery_info_oneOf_i1_with_wrap ) | No      | boolean | No         | -          | -                 |

#### <a name="delivery_info_oneOf_i1_with_wrap"></a>3.2.1. `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap` ![type: boolean](https://img.shields.io/badge/type-boolean-da8bc3)

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
