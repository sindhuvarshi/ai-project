import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

# Load data
data = pd.read_csv("data.csv")

X = data[['hours']]
Y = data['marks']

# Train model
model = DecisionTreeRegressor()
model.fit(X, Y)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")