import pandas as pd


df = pd.read_csv("sales.csv")
print(df)
print(len(df))
print(df.shape)
print(df.columns)
print(list(df.columns))
print()
print(df.head(3))
print()
print(df.tail(3))

print()
print(df["price"].describe())
print(df.describe())

# print(df[["product", "price"]])

df["revenue"] = df["price"]*df["quantity"] # this is a computed column
print(df)


price_gt100_mask = df["price"] > 100
print(price_gt100_mask)
print(df[price_gt100_mask])

print()
print(df[
    (df["city"] == "Delhi") & 
    (df["category"] == "Stationery")])

print()
print(df.sort_values("revenue", ascending=False).head(3))
print(df)


# grouping
# total revenuew per city
print()
print(df.groupby("city")["revenue"].sum())


stats = df.groupby("category").agg(
    total_revenue=("revenue", "sum"),
    avg_price=("price", "mean"),
    items_sold=("quantity", "sum"),
)

print(stats)



