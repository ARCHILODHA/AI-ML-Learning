# Data Preprocessing

## Steps
- Handle missing values
- Encode categorical data
- Feature scaling

## Example (Python)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
