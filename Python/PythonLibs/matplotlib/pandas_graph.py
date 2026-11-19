import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales.csv")
df["revenue"] = df["price"] * df["quantity"]


# df.groupby("city")["revenue"].sum().plot(kind="bar", color="teal", figsize=(10,6))
# df.groupby("city")["revenue"].mean().plot(kind="bar", color="teal", figsize=(10,6))
df.groupby("product")["quantity"].sum().plot(kind="bar", color="teal", figsize=(10,6)) #TODO

plt.title("Total Revenue by City")
plt.ylabel("Revenue")
plt.xlabel("CITY")
plt.xticks(rotation=0)
plt.show()