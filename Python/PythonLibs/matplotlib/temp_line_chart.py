import numpy as np
import matplotlib.pyplot as plt


# 1. Create an array of temperatures in Celsius
celsius = np.array([22, 25, 19, 30, 28, 24, 21, 78, 21])

days = np.arange(1, len(celsius) + 1)

# 2. Convert Celsius to Fahrenheit
fahrenheit = celsius * 9/5 + 32


plt.plot(days, celsius, marker="o", label="Celsius")
plt.plot(days, fahrenheit, marker="s", label="Fahrenheit")

plt.title("Daily Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")
# plt.xticks(days)

# plt.xticks(range(7), ["Day 1", "Day 2", "Day 3", "Day 4",
#                       "Day 5", "Day 6", "Day 7"])


plt.xticks(days, [f"Day {day}" for day in days],rotation=45, ha="right")


plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
