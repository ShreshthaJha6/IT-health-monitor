import pandas as pd

def generate_report(file="logs_with_anomalies.csv"):
    df = pd.read_csv(file)

    avg_cpu = df["cpu"].mean()
    avg_memory = df["memory"].mean()
    avg_disk = df["disk"].mean()

    anomalies = df[df["anomaly"] == -1].shape[0]

    report = f"""
    ====================
    SYSTEM HEALTH REPORT
    ====================

    Average CPU usag: {avg_cpu:.2f}%
    Average Memory usage: {avg_memory:.2f}%
    Average Disk usage: {avg_disk:.2f}%

    Number of anomalies detected: {anomalies}

    RECOMMMENDATIONS:
    """

    if avg_cpu > 80:
        report += "\n- High CPU usage. Consider scaling resources."
    if avg_memory > 80:
        report += "\n- High Memory usage. Check for memory leaks."
    if avg_disk > 85:
        report += "\n- Disk usga eis critical. Clean logs or expand storage."
    if anomalies > 0:
        report += "\n- Anomalies detectd. Investigate the root cause."
    
    with open("health_report.txt", "w") as f:
        f.write(report)
    
    print(report)

if __name__ == "__main__":
    generate_report()