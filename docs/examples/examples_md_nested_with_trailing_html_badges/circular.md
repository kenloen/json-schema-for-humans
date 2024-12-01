# Circular reference Schema

- [1. <code> Circular reference Schema > person </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#person)
  - [1.1. <code> Circular reference Schema > person > a1 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0">](#person_a1)

**Title:** Circular reference Schema

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary>
<strong> <a name="person"></a>1. <code> Circular reference Schema > person </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/a                                                                                                                   |

<details>
<summary>
<strong> <a name="person_a1"></a>1.1. <code> Circular reference Schema > person > a1 </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-string-4c72b0"></strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Default**    | `"Default from c"` |
| **Defined in** | #/definitions/b    |

**Description:** Description from b

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)