import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

df = pd.read_csv("data/UAVIDS-2025.csv")

df = df.drop(["FlowID","SrcAddr","DstAddr","label"],axis=1)

model = IsolationForest(
    n_estimators=200,
    contamination=0.03,
    random_state=42
)

model.fit(df)

joblib.dump(model,"models/anomaly.pkl")

print("Anomaly model saved")