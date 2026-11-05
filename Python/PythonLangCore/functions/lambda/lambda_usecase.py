products = [
    {"name": "Ford Town Car", "price": 121.64, "line": "Vintage Cars"},
    {"name": "Harley",        "price":  95.70, "line": "Motorcycles"},
    {"name": "Alfa Romeo",    "price":  92.03, "line": "Vintage Cars"},
]

# sorted_products = sorted(products)#TypeError: '<' not supported between instances of 'dict' and 'dict'
# print(sorted_products)

sorted_products = sorted(products, key=lambda p:p["price"], reverse=True)
print(sorted_products)


# price1 == price2 :: 0
# price1 > price2 :: 5
# -3

sorted_products_2factor = sorted(products, key=lambda p: (p["line"], -p["price"]))
print(sorted_products_2factor)# DESCENDING

sorted_products_2factor = sorted(products, key=lambda p: (p["line"], p["price"]))
print(sorted_products_2factor)# ASCENDING