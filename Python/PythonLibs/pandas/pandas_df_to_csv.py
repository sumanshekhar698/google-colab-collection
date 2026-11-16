import pandas as pd


data = {
    "product":  ["Pen", "Notebook", "Bag", "Pen", "Bag", "Notebook", "Pen", "Bottle"],
    "category": ["Stationery", "Stationery", "Accessories", "Stationery",
                 "Accessories", "Stationery", "Stationery", "Accessories"],
    "price":    [10, 50, 500, 10, 450, 55, 12, 200],
    "quantity": [100, 40, 5, 80, 8, 30, 120, 15],
    "city":     ["Delhi", "Mumbai", "Delhi", "Mumbai", "Pune", "Delhi", "Pune", "Mumbai"],
}

df = pd.DataFrame(data)
print(df)
df.to_csv("sales.csv", index=False)