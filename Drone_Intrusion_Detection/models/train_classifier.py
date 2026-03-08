import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

df = pd.read_csv("data/UAVIDS-2025.csv")

df = df.drop(["FlowID","SrcAddr","DstAddr"],axis=1)

protocol_encoder = LabelEncoder()
df["Protocol"] = protocol_encoder.fit_transform(df["Protocol"])

X = df.drop("label",axis=1)
y = df["label"]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

model = XGBClassifier(
    n_estimators=300,
    max_depth=8,
    learning_rate=0.1,
    subsample=0.8
)

model.fit(X_train, y_train)

joblib.dump(model,"models/classifier.pkl")
joblib.dump(label_encoder,"models/encoder.pkl")

print("Model trained successfully")