import pandas as pd
import time

df = pd.read_csv("data/UAVIDS-2025.csv")

for i,row in df.iterrows():

    print("Streaming packet:",row.values)

    time.sleep(0.1)