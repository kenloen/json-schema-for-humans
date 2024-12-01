# Bug

- [1. `Bug > Code` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)](#Code)
- [2. `Bug > RecursiveArray` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array](https://img.shields.io/badge/type-array-8172b3)](#RecursiveArray)
  - [2.1. Bug > RecursiveArray > #](#RecursiveArray_items)
- [3. `Bug > DecoratedRecursiveArray` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of object](https://img.shields.io/badge/type-array%20of%20object-a26082)](#DecoratedRecursiveArray)
  - [3.1. Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items](#DecoratedRecursiveArray_items)
    - [3.1.1. `Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > SomeName` ![type: string](https://img.shields.io/badge/type-string-4c72b0)](#DecoratedRecursiveArray_items_SomeName)
    - [3.1.2. `Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > TheThing` ![type: object](https://img.shields.io/badge/type-object-c44e52)](#DecoratedRecursiveArray_items_TheThing)

**Title:** Bug

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** Display the issue.

| Property                                               | Pattern | Type            | Deprecated | Definition | Title/Description                |
| ------------------------------------------------------ | ------- | --------------- | ---------- | ---------- | -------------------------------- |
| - [Code](#Code )                                       | No      | string          | No         | -          | Code property                    |
| - [RecursiveArray](#RecursiveArray )                   | No      | array           | No         | -          | RecursiveArray property          |
| - [DecoratedRecursiveArray](#DecoratedRecursiveArray ) | No      | array of object | No         | -          | DecoratedRecursiveArray property |

## <a name="Code"></a>1. `Bug > Code` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Code property

## <a name="RecursiveArray"></a>2. `Bug > RecursiveArray` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array](https://img.shields.io/badge/type-array-8172b3)

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** RecursiveArray property

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description        |
| ------------------------------- | ------------------ |
| [#](#RecursiveArray_items)      | Display the issue. |

### <a name="RecursiveArray_items"></a>2.1. Bug > RecursiveArray > #

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [Bug](#root)                                                                                                                      |

**Description:** Display the issue.

## <a name="DecoratedRecursiveArray"></a>3. `Bug > DecoratedRecursiveArray` ![Optional](https://img.shields.io/badge/Optional-yellow)![type: array of object](https://img.shields.io/badge/type-array%20of%20object-a26082)

|          |                   |
| -------- | ----------------- |
| **Type** | `array of object` |

**Description:** DecoratedRecursiveArray property

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [DecoratedRecursiveArray items](#DecoratedRecursiveArray_items) | -           |

### <a name="DecoratedRecursiveArray_items"></a>3.1. Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                               | Pattern | Type   | Deprecated | Definition            | Title/Description  |
| ------------------------------------------------------ | ------- | ------ | ---------- | --------------------- | ------------------ |
| - [SomeName](#DecoratedRecursiveArray_items_SomeName ) | No      | string | No         | -                     | -                  |
| - [TheThing](#DecoratedRecursiveArray_items_TheThing ) | No      | object | No         | Same as [Bug](#root ) | Display the issue. |

#### <a name="DecoratedRecursiveArray_items_SomeName"></a>3.1.1. `Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > SomeName` ![type: string](https://img.shields.io/badge/type-string-4c72b0)

|          |          |
| -------- | -------- |
| **Type** | `string` |

#### <a name="DecoratedRecursiveArray_items_TheThing"></a>3.1.2. `Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > TheThing` ![type: object](https://img.shields.io/badge/type-object-c44e52)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [Bug](#root)                                                                                                                      |

**Description:** Display the issue.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
