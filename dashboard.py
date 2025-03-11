import streamlit as st
import pandas as pd
from data_extract import load_and_process_data

st.title("Аналитика использования чат-бота")

df = load_and_process_data()

if df.empty:
    st.warning("Данные отсутствуют.")
else:
    st.write("### Логи запросов")
    st.dataframe(df)

    if "intent" in df.columns:
        st.write("### Статистика по интентам")
        intent_counts = df["intent"].value_counts()
        st.bar_chart(intent_counts)

    if "action" in df.columns:
        st.write("### Статистика по действиям")
        action_counts = df["action"].value_counts()
        st.bar_chart(action_counts)

    if "timestamp" in df.columns:
        st.write("### Временная динамика запросов")
        try:
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
        except ValueError:
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

        requests_over_time = df.set_index("timestamp").resample("h").size()
        st.line_chart(requests_over_time)
