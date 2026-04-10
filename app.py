import streamlit as st
import random

st.title("Monitoring Suhu & Kelembaban")

suhu = random.uniform(25, 35)
kelembaban = random.uniform(60, 90)

st.metric("Suhu (°C)", round(suhu,2))
st.metric("Kelembaban (%)", round(kelembaban,2))

if suhu > 30:
    st.warning("Suhu panas! Kipas menyala 🔥")
else:
    st.success("Suhu normal ❄️")
