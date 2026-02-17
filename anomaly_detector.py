import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(file="logs.csv"):
    df = pd.read_csv(file)

    model = IsolationForest(contamination=0.1)
    df["anomaly"] = model.fit_predict(df[["cpu", "memory", "disk"]])

    df.to_csv("logs_with_anomalies.csv", index = False)
    print("Anomalies detected and saved to logs_with_anomalies.csv")
    print(df[df["anomaly"]==-1])

    return df

if __name__ == "__main__":
    detect_anomalies()