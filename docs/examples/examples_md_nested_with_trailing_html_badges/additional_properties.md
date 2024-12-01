# Person

- [1. <code> Person > subType1 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#subType1)
  - [1.1. <code> Person > subType1 > subProp1 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-number-dd8452">](#subType1_subProp1)
- [2. <code> Person > subType2 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#subType2)
  - [2.1. <code> Person > subType2 > subProp2 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-number-dd8452">](#subType2_subProp2)
- [3. <code> Person > anInt </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868">](#anInt)
- [4. <code> Person > additionalProperties </code><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#additionalProperties)
  - [4.1. <code> Person > additionalProperties > propA </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-number-dd8452">](#additionalProperties_propA)

**Title:** Person

|                           |                                                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                                                                     |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#additionalProperties "Each additional property must conform to the following schema") |

<details>
<summary>
<strong> <a name="subType1"></a>1. <code> Person > subType1 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

**Description:** A sub type with additionalProperties false.

<details>
<summary>
<strong> <a name="subType1_subProp1"></a>1.1. <code> Person > subType1 > subProp1 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-number-dd8452"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `number` |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="subType2"></a>2. <code> Person > subType2 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** A sub type with additionalProperties true.

<details>
<summary>
<strong> <a name="subType2_subProp2"></a>2.1. <code> Person > subType2 > subProp2 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-number-dd8452"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `number` |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="anInt"></a>3. <code> Person > anInt </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868"></strong>  

</summary>
<blockquote>

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** This is an integer, it should not show additional properties. (issue #132)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="additionalProperties"></a>4. <code> Person > additionalProperties </code><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** additionalProperties schema.

<details>
<summary>
<strong> <a name="additionalProperties_propA"></a>4.1. <code> Person > additionalProperties > propA </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-number-dd8452"></strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `number` |

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)