import streamlit as st
import pandas as pd
import random
import time

# CONFIG
st.set_page_config(page_title="IoT Dashboard", layout="wide")

# SIDEBAR
st.sidebar.title("⚙️ Menu")
menu = st.sidebar.radio("Pilih Menu:", ["Dashboard", "Tentang"])

# SIMULASI DATA
def get_data():
    return random.uniform(25, 35), random.uniform(60, 90)

# DASHBOARD
if menu == "Dashboard":
    st.title("🌡️ Smart Monitoring System")
    st.markdown("Monitoring suhu & kelembaban berbasis IoT")

    # METRIC
    suhu, kelembaban = get_data()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🌡️ Suhu (°C)", round(suhu, 2))

    with col2:
        st.metric("💧 Kelembaban (%)", round(kelembaban, 2))

    with col3:
        if suhu > 30:
            st.error("🌀 Kipas ON")
        else:
            st.success("❄️ Kipas OFF")

    # PROGRESS BAR (indikator suhu)
    st.subheader("Indikator Suhu")
    st.progress(int((suhu/40)*100))

    # REALTIME GRAPH
    st.subheader("📊 Grafik Real-time")

    chart_data = pd.DataFrame(columns=["Suhu"])

    chart = st.line_chart(chart_data)

    for i in range(20):
        new_data = pd.DataFrame({"Suhu": [random.uniform(25, 35)]})
        chart.add_rows(new_data)
        time.sleep(0.5)

# HALAMAN TENTANG
elif menu == "Tentang":
    st.title("📘 Tentang Project")
    st.write("""
    Project ini adalah sistem monitoring suhu dan kelembaban berbasis IoT.

    🔧 Komponen:
    - Sensor DHT22
    - Arduino
    - Streamlit Dashboard

    🎯 Tujuan:
    Mengontrol kipas otomatis berdasarkan suhu lingkungan.
    """)