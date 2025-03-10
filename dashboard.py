import streamlit as st
import pandas as pd
import psycopg2

def get_data():
    conn = psycopg2.connect(
        dbname="chat_bot",
        user="postgres",
        password="1",
        host="localhost",
        port="5432"
    )
    query = "SELECT * FROM rasa_logs"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("Аналитика использования чат-бота")

data = get_data()

st.write("### Логи запросов")
st.dataframe(data)

st.write("### Статистика по интентам")
intent_counts = data["intent"].value_counts()
st.bar_chart(intent_counts)

st.write("### Статистика по действиям")
action_counts = data["action"].value_counts()
st.bar_chart(action_counts)

st.write("### Временная динамика запросов")
data["timestamp"] = pd.to_datetime(data["timestamp"])
requests_over_time = data.set_index("timestamp").resample("H").size()
st.line_chart(requests_over_time)