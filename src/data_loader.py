import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df["month_year"] = pd.to_datetime(df["month_year"])
    df = df.sort_values("month_year")
    return df