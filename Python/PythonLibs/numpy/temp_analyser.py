import numpy as np

# 1. Create an array of temperatures in Celsius
celsius = np.array([22, 25, 19, 30, 28, 24, 21])

# 2. Convert Celsius to Fahrenheit
fahrenheit = celsius * 9/5 + 32

print("Celsius    :", celsius)
print("Fahrenheit :", fahrenheit.round(1))

# 3. Filter days hotter than 24°C
hot_days = celsius > 24

print("Hot days (Celsius):", celsius[hot_days])