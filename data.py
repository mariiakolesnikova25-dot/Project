import yfinance as yf
import pandas as pd

def load_data():
    ticker = "CL=F"

    data = yf.download(
        ticker,
        start="2023-01-01",
        end="2025-01-01"
    )
    #прибираю другий рівень назв колонок (якщо така ж версія як в мене)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    #прибираю пропуски, якщо є
    data = data.ffill().dropna()

    #вибираю потрібні назви колонок
    data = data[["Open", "High", "Low", "Close", "Volume"]]

    return data

