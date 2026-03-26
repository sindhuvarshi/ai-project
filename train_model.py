import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

data = pd.read_csv("data.csv")

X = data[['hours', 'sleep', 'previous']]
Y = data['marks']

model = DecisionTreeRegressor()
model.fit(X, Y)

joblib.dump(model, "model.pkl")

print("Model trained & saved!")