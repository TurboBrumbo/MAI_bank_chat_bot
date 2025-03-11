import pandas as pd
from sqlalchemy import create_engine
import json

def load_and_process_data():
    """Загружает и обрабатывает данные из БД"""
    engine = create_engine("postgresql://postgres:1@localhost:5432/chat_bot")

    with engine.connect() as connection:
        query = "SELECT id, sender_id, data FROM events"
        df = pd.read_sql(query, connection)

    df["raw_data"] = df["data"]

    def parse_data(row):
        try:
            parsed = json.loads(row["data"])
            if isinstance(parsed, dict):
                return parsed
            else:
                return {}
        except (json.JSONDecodeError, TypeError):
            return {}

    df["parsed_data"] = df.apply(parse_data, axis=1)

    parsed_df = pd.json_normalize(df["parsed_data"])

    for col in parsed_df.columns:
        if col in df.columns:
            parsed_df.rename(columns={col: f"{col}_parsed"}, inplace=True)

    df = pd.concat([df.drop(columns=["data", "parsed_data"]), parsed_df], axis=1)

    df = df.loc[:, ~df.columns.duplicated()].copy()

    selected_columns = [
        "id", "sender_id", "raw_data", "event", "timestamp", "name", "policy",
        "confidence", "metadata.model_id", "metadata.assistant_id", "text",
        "input_channel", "message_id", "parse_data.intent.name"
    ]
    df = df[selected_columns]

    return df
