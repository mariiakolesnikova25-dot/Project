from data import load_data
from strategy import calculate_moving_average, generate_signals
import matplotlib.pyplot as plt

data = load_data()
data = calculate_moving_average(data)
data = generate_signals(data)

buys = data[data["Signal"] == 1]
sells = data[data["Signal"] == -1]

buy_prices = list(buys["Close"])
sell_prices = list(sells["Close"])

if len(sell_prices) > 0 and len(buy_prices) > 0 and sells.index[0] < buys.index[0]:
    sell_prices = sell_prices[1:]

total_profit = 0
trades = min(len(buy_prices), len(sell_prices))

for i in range(trades):
    profit = sell_prices[i] - buy_prices[i]
    total_profit += profit

print(f"Загальний прибуток/збиток: ${total_profit}")

plt.figure(figsize=(14, 6))
plt.plot(data.index, data["Close"], label="Ціна закриття", color="gray")
plt.plot(data.index, data["MA20"], label="MA20", color="blue")
plt.plot(data.index, data["MA50"], label="MA50", color="red")
plt.scatter(buys.index, buys["Close"], marker="^", color="green", s=100, label="Купівля")
plt.scatter(sells.index, sells["Close"], marker="v", color="red", s=100, label="Продаж")
plt.title("Стратегія перетину ковзних середніх")
plt.xlabel("Дата")
plt.ylabel("Ціна, $")
plt.grid(True)
plt.legend()
plt.show()