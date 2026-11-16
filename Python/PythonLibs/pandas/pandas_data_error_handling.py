import pandas as pd


df = pd.read_csv("sales.csv")
print(df)
print(len(df))
print(df.shape)
print(df.columns)
print(list(df.columns))


df.loc[2,"price"] = None
df.loc[4,"price"] = None
# df.iloc[2,2] = None
print(df)

# df["price"] = df["price"].fillna(100) # fixed val

# df["price"] = df["price"].fillna(df["price"].mean().round(1))
# df["price"] = df["price"].fillna(df["price"].median().round(1))

# df["price"] = df["price"].ffill()
df["price"] = df["price"].bfill()

print()
print(df)


df.loc[2,"city"] = None
df = df.fillna({
    "price": df["price"].median(),
    "quantity": 0,
    "city": "Unknown",
    "category": "Other"
})
print(df)



df["revenue"] = df["price"] * df["quantity"]

high_quantity = df[df["quantity"] > 50]
print(high_quantity)


city_sales = df.groupby("city")["quantity"].sum()
print(city_sales)

most_revenue = df.groupby("product")["revenue"].sum()
print(most_revenue)
top_product=most_revenue.sort_values(ascending=False).index[0]
print(top_product)  
