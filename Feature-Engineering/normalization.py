from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df = pd.DataFrame({
    "Salary": [25000, 35000, 50000, 70000]
})

scaler = MinMaxScaler()

df["Salary_Normalized"] = scaler.fit_transform(df[["Salary"]])

print(df)
