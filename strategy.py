import pandas as pd

def calculate_moving_average(data):
    """Обчислення коротко- і довгострокових ковзних середніх"""

    data["MA20"] = data["Close"].rolling(20).mean()
    data["MA50"] = data["Close"].rolling(50).mean()

    return data

def generate_signals(data):
    data["Signal"] = 0

    #Коли купуємо
    buy_condition = (
        (data["MA20"] > data["MA50"]) &
        (data["MA20"].shift(1) <= data["MA50"].shift(1))
    )
    #Коли продаємо
    sell_condition = (
        (data["MA20"] < data["MA50"]) &
        (data["MA20"].shift(1) >= data["MA50"].shift(1))
    )

    data.loc[buy_condition, "Signal"] = 1
    data.loc[sell_condition, "Signal"] = -1

    return data