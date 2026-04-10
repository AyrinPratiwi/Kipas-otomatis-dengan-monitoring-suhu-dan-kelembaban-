import streamlit as st
import pandas as pd
import numpy as np
import time

# CONFIG
st.set_page_config(page_title="IoT Smart Dashboard", layout="wide")

# SIDEBAR
st.sidebar.title("⚙️ Smart Control Panel")
menu = st.sidebar.radio("Navigasi", ["🏠 Dashboard", "📊 Analytics", "🔧 Device"])

# SIMULASI DATA HALUS (biar realistis)
if "suhu" not in st.session_state:
    st.session_state.suhu = 28
if "kelembaban" not in st.session_state:
    st.session_state.kelembaban = 70

def update_data():
    st.session_state.suhu += np.random.uniform(-0.5, 0.5)
    st.session_state.kelembaban += np.random.uniform(-1, 1)

# ================= DASHBOARD =================
if menu == "🏠 Dashboard":
    st.title("🌡️ Smart IoT Monitoring System")
    st.caption("Realtime monitoring suhu & kelembaban")

    update_data()
    suhu = st.session_state.suhu
    kelembaban = st.session_state.kelembaban

    # METRICS
    col1, col2, col3 = st.columns(3)

    col1.metric("🌡️ Suhu (°C)", f"{suhu:.2f}")
    col2.metric("💧 Kelembaban (%)", f"{kelembaban:.2f}")

    if suhu > 30:
        col3.error("🌀 Kipas ON")
    else:
        col3.success("❄️ Kipas OFF")

    # GAUGE (PROGRESS BAR STYLE)
    st.subheader("Indikator Suhu")
    st.progress(min(int((suhu/40)*100),100))

    # REALTIME GRAPH
    st.subheader("📈 Grafik Realtime")

    chart = st.line_chart(pd.DataFrame({"Suhu": []}))

    for i in range(30):
        update_data()
        new_data = pd.DataFrame({"Suhu": [st.session_state.suhu]})
        chart.add_rows(new_data)
        time.sleep(0.2)

# ================= ANALYTICS =================
elif menu == "📊 Analytics":
    st.title("📊 Analisis Data")

    data = pd.DataFrame({
        "Suhu": np.random.normal(28, 2, 100),
        "Kelembaban": np.random.normal(70, 5, 100)
    })

    st.subheader("Distribusi Suhu")
    st.bar_chart(data["Suhu"])

    st.subheader("Distribusi Kelembaban")
    st.bar_chart(data["Kelembaban"])

    st.subheader("Statistik")
    st.write(data.describe())

# ================= DEVICE =================
elif menu == "🔧 Device":
    st.title("🔧 Status Device")

    st.write("Status Sensor: ✅ Aktif")
    st.write("Koneksi: 🌐 Online (Simulasi)")
    st.write("Mode: 🤖 Otomatis")

    st.subheader("Kontrol Manual (Simulasi)")
    tombol = st.button("Toggle Kipas")

    if tombol:
        st.success("Kipas di-toggle (simulasi)")