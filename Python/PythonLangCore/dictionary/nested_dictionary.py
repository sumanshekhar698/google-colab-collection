orders = {
    10100: {"date": "2003-01-06", "customer": 363, "lines": 3},
    10101: {"date": "2003-01-09", "customer": 128, "lines": 2},
}

print(orders[10101]["date"])
print(orders.get(10101, {}).get("date"))
print(orders.get(10102, {}).get("date"))



for num, info in orders.items():
    print(f"Order {num}: {info['lines']} lines on {info['date']}")