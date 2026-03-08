import pandas as pd
from sklearn.preprocessing import StandardScaler

def process(df):

    df = df.drop(["FlowID","SrcAddr","DstAddr"],axis=1)

    scaler = StandardScaler()

    numeric = df.select_dtypes(include=['float64','int64']).columns

    df[numeric] = scaler.fit_transform(df[numeric])

    return df