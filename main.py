from data import load_data
from strategy import calculate_moving_average, generate_signals

data = load_data()
data = calculate_moving_average(data)
data = generate_signals(data)

