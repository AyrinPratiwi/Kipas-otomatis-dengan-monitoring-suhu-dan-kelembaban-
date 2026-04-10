import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.graph_objects as go

# CONFIG
st.set_page_config(page_title="Monitoring Suhu dan Kelembaban pada Kipas Otomatis", layout="wide")

# ================= STYLE =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

section[data-testid="stSidebar"] {
    background: #020617;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 25px rgba(0,255,255,0.1);
}

/* TITLE */
h1 {
    color: #38bdf8;
}

/* FAN */
.fan {
    font-size: 40px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    100% { transform: rotate(360deg); }
}

/* STATUS */
.status-on {
    color: #22c55e;
    font-weight: bold;
}

.status-off {
    color: #60a5fa;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Smart Control Panel")
menu = st.sidebar.radio("Navigasi", ["🏠 Dashboard", "📊 Analytics", "🔧 Device"])

# ================= DATA =================
if "suhu" not in st.session_state:
    st.session_state.suhu = 28

if "kelembaban" not in st.session_state:
    st.session_state.kelembaban = 70

if "history" not in st.session_state:
    st.session_state.history = []

def update_data():
    st.session_state.suhu += np.random.uniform(-0.3, 0.3)
    st.session_state.kelembaban += np.random.uniform(-0.8, 0.8)
    st.session_state.history.append(st.session_state.suhu)

# ================= DASHBOARD =================
if menu == "🏠 Dashboard":

    st.title("🌡️ Smart IoT Monitoring System")
    st.caption("Realtime monitoring suhu & kelembaban")

    update_data()

    suhu = st.session_state.suhu
    kelembaban = st.session_state.kelembaban

<<<<<<< HEAD
    # ===== COLUMNS FIX (ANTI ERROR) =====
    col1, col2, col3 = st.columns(3)
=======
    update_data()
    suhu = st.session_state.suhu
    kelembaban = st.session_state.kelembaban
>>>>>>> 41ebba8deab86d6bf2495e208f04193a26b78b94

    # SUHU
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("🌡️ Suhu", f"{suhu:.2f} °C")
        st.markdown('</div>', unsafe_allow_html=True)

    # KELEMBABAN
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("💧 Kelembaban", f"{kelembaban:.2f} %")
        st.markdown('</div>', unsafe_allow_html=True)

    # FAN STATUS
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        if suhu > 30:
            st.markdown('<div class="fan">🌀</div>', unsafe_allow_html=True)
            st.markdown('<div class="status-on">KIPAS ON</div>', unsafe_allow_html=True)
        else:
            st.markdown("🌀")
            st.markdown('<div class="status-off">KIPAS OFF</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ================= GAUGE =================
    st.subheader("🔥 Indikator Suhu")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=suhu,
        title={'text': "Suhu (°C)"},
        gauge={
            'axis': {'range': [0, 40]},
            'bar': {'color': "#22c55e"},
            'steps': [
                {'range': [0, 25], 'color': "#1e293b"},
                {'range': [25, 30], 'color': "#3b82f6"},
                {'range': [30, 40], 'color': "#ef4444"},
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # ================= STATUS =================
    st.markdown("### ⚡ Status Sistem")
    if suhu > 30:
        st.error("🔥 Suhu tinggi → kipas otomatis aktif")
    else:
        st.success("❄️ Suhu normal → sistem standby")

    # ================= CHART (FIX NO LAG) =================
    st.subheader("📈 Grafik Realtime")

    if len(st.session_state.history) > 50:
        st.session_state.history.pop(0)

    chart_data = pd.DataFrame({
        "Suhu": st.session_state.history
    })

    st.line_chart(chart_data)

    # 🔁 Refresh button (biar realtime tanpa lag)
    if st.button("🔄 Refresh Data"):
        st.rerun()

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

    st.markdown("✅ Sensor aktif")
    st.markdown("🌐 Koneksi: Online (Simulasi)")
    st.markdown("🤖 Mode: Otomatis")

    if st.button("Toggle Kipas"):
        st.success("Kipas berhasil di-toggle (simulasi)")
