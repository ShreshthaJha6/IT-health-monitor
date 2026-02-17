import psutil
import pandas as pd
import time
from datetime import datetime

def collect_metrics(duration=60, interval=5):
    data = []

    for _ in range(int(duration/interval)):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        data.append({
            "timestamp" : datetime.now(),
            "cpu": cpu,
            "memory": memory,
            "disk": disk
        })

        time.sleep(interval)
    
    df = pd.DataFrame(data)
    df.to_csv("logs.csv", index = False)
    print("Metrics collected and saved to logs.csv")
    return df

if __name__ == "__main__":
    collect_metrics()