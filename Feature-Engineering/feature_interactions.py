import pandas as pd

df = pd.DataFrame({
    "age": [20, 25, 30],
    "salary": [20000, 30000, 40000]
})

df["age_salary_interaction"] = df["age"] * df["salary"]
print(df)
