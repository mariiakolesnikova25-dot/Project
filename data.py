import yfinance as yf


def load_data():
    ticker = "CL=F"

    data = yf.download(
        ticker,
        start="2023-01-01",
        end="2025-01-01"
    )
    #прибираю другий рівень назв колонок
    data.columns = data.columns.droplevel(1)

    #вибираю потрібні назви колонок
    data = data[["Open", "High", "Low", "Close", "Volume"]]
    return data

#перевірка
data = load_data()

print(data.head())
print(data.info())