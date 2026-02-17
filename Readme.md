# IT Governance & System Health Monitoring Dashboard

A lightweight Python-based IT Governance prototype that automates system health monitoring, anomaly detection, and executive-style reporting.

This project simulates an enterprise IT operations monitoring system aligned with governance, compliance, and operational oversight practices.

---

## 🚀 Project Overview

This system:

- Collects system health metrics (CPU, Memory, Disk usage)
- Detects anomalies using an AI-based Isolation Forest model
- Generates governance-style health reports with recommendations
- Visualizes metrics through an interactive Streamlit dashboard

The goal is to demonstrate automation, monitoring, AI integration, and governance-oriented reporting in a structured and scalable way.

---

## 🏗 Architecture

1. **monitor.py**
   - Collects system metrics using `psutil`
   - Stores metrics in `logs.csv`

2. **anomaly_detector.py**
   - Uses Isolation Forest (scikit-learn)
   - Detects abnormal usage patterns
   - Outputs `logs_with_anomalies.csv`

3. **report_generator.py**
   - Generates a governance-style health summary
   - Produces actionable recommendations
   - Outputs `health_report.txt`

4. **dashboard.py**
   - Interactive Streamlit dashboard
   - Visualizes CPU, memory, disk usage
   - Displays detected anomalies

---

## 🛠 Tech Stack

- Python
- psutil
- pandas
- scikit-learn
- matplotlib
- streamlit

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd IT-health-monitor
Install Dependencies
pip install -r requirements.txt
How to Run
Step 1 – Collect Monitoring Data
python monitor.py
This generates:
logs.csv
Step 2 – Run Anomaly Detection
python anomaly_detector.py
This generates:
logs_with_anomalies.csv
Step 3 – Generate Governance Report
python report_generator.py
This generates:
health_report.txt
Step 4 – Launch Dashboard
streamlit run dashboard.py
```
