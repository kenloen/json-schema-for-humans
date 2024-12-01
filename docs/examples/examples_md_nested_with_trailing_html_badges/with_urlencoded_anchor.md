# Schema Docs

- [1. <code> root > signingTimeInfo </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#signingTimeInfo)
  - [1.1. <code> root > signingTimeInfo > signingTime </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868">](#signingTimeInfo_signingTime)
  - [1.2. <code> root > signingTimeInfo > signingTimeBounds </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52">](#signingTimeInfo_signingTimeBounds)
    - [1.2.1. <code> root > signingTimeInfo > signingTimeBounds > lowerBound </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868">](#signingTimeInfo_signingTimeBounds_lowerBound)
    - [1.2.2. <code> root > signingTimeInfo > signingTimeBounds > upperBound </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868">](#signingTimeInfo_signingTimeBounds_upperBound)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary>
<strong> <a name="signingTimeInfo"></a>1. <code> root > signingTimeInfo </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType                                                                                            |

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTime"></a>1.1. <code> root > signingTimeInfo > signingTime </code><img alt="Required Badge" src="https://img.shields.io/badge/Required-blue"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868"></strong>  

</summary>
<blockquote>

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTimeBounds"></a>1.2. <code> root > signingTimeInfo > signingTimeBounds </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-object-c44e52"></strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries                                                                    |

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTimeBounds_lowerBound"></a>1.2.1. <code> root > signingTimeInfo > signingTimeBounds > lowerBound </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868"></strong>  

</summary>
<blockquote>

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTimeBounds_upperBound"></a>1.2.2. <code> root > signingTimeInfo > signingTimeBounds > upperBound </code><img alt="Optional Badge" src="https://img.shields.io/badge/Optional-yellow"><img alt="type Badge" src="https://img.shields.io/badge/type-integer-55a868"></strong>  

</summary>
<blockquote>

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)