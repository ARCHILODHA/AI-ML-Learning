import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

data = pd.DataFrame({
    "Age": [22, 25, None, 35, 40],
    "Salary": [30000, 40000, 35000, None, 70000],
    "City": ["Udaipur", "Jaipur", "Delhi", "Udaipur", None]
})

numeric_features = ["Age", "Salary"]
categorical_features = ["City"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])

transformed_data = preprocessor.fit_transform(data)

print("Original Data:")
print(data)

print("\nTransformed Shape:")
print(transformed_data.shape)

print("\nFeature Engineering Pipeline Completed")
