# One Hot Encoding

## Definition
Converts categorical variables into binary columns.

## Advantages
- Prevents ordinal relationship.
- Works well for nominal data.

## Example

Before

| City |
|------|
| Delhi |
| Pune |

After

| City_Delhi | City_Pune |
|------------|-----------|
| 1 | 0 |
| 0 | 1 |

Use:

```python
pd.get_dummies()
```
