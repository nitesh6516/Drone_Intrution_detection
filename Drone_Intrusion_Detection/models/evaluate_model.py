import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/UAVIDS-2025.csv")

df = df.drop(["FlowID","SrcAddr","DstAddr"],axis=1)

protocol_encoder = LabelEncoder()
df["Protocol"] = protocol_encoder.fit_transform(df["Protocol"])

X = df.drop("label",axis=1)
y = df["label"]

model = joblib.load("models/classifier.pkl")
label_encoder = joblib.load("models/encoder.pkl")

y_encoded = label_encoder.transform(y)

preds = model.predict(X)

accuracy = accuracy_score(y_encoded,preds)

print("Model Accuracy:",accuracy)

print("\nClassification Report:\n")

print(classification_report(y_encoded,preds))