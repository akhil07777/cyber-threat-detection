import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv(
    "dataset/KDDTrain+.txt",
    header=None
)

X = data[[0,4,5]]

y = data[41]

y = y.apply(
    lambda x: 0 if x == "normal" else 1
)

model = RandomForestClassifier()

model.fit(X,y)

joblib.dump(
    model,
    "ml/model.pkl"
)

print("Model Saved Successfully")