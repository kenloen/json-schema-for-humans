# OF

- [1. [Optional] Property OF > uuid](#uuid)
- [2. [Optional] Property OF > firstName](#firstName)
- [3. [Optional] Property OF > lastName](#lastName)

**Title:** OF

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

<details>
<summary>
<strong> <a name="uuid"></a>1. [Optional] Property OF > uuid</strong>  

</summary>
<blockquote>

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/ofString |

**Description:** Unique Identifer

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 5   |
| **Max length** | 250 |

**Example:** 

```json
"29292929292929292929292"
```

</blockquote>
</details>

<details>
<summary>
<strong> <a name="firstName"></a>2. [Optional] Property OF > firstName</strong>  

</summary>
<blockquote>

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/ofString |

**Description:** first name

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 10  |
| **Max length** | 250 |

**Example:** 

```json
"John"
```

</blockquote>
</details>

<details>
<summary>
<strong> <a name="lastName"></a>3. [Optional] Property OF > lastName</strong>  

</summary>
<blockquote>

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/ofString |

**Description:** last name

| Restrictions   |    |
| -------------- | -- |
| **Min length** | 5  |
| **Max length** | 10 |

**Example:** 

```json
"Doe"
```

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)