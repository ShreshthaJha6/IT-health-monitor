import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("IT System Health Dashboard")
df = pd.read_csv("logs_with_anomalies.csv")

st.subheader("System Metrics")
st.line_chart(df[["cpu", "memory", "disk"]])

st.subheader("Anomalies")
st.write(df[df["anomaly"] == -1])