from collections import defaultdict

products = [
    {"name": "1917 Grand Touring Sedan", "line": "Vintage Cars",  "price": 170.00},
    {"name": "1911 Ford Town Car",       "line": "Vintage Cars",  "price": 121.64},
    {"name": "1932 Alfa Romeo",          "line": "Vintage Cars",  "price":  92.03},
    {"name": "1969 Harley Davidson",     "line": "Motorcycles",   "price":  95.70},
    {"name": "1996 Moto Guzzi",          "line": "Motorcycles",   "price":  68.99},
]

# VitageCars: []  MotorCycles:[]

grouped = defaultdict(list)

for product in products:
    grouped[product["line"]].append(product["name"])

print(grouped)


for line, names in grouped.items():
    print(f"{line}: {len(names)} products")
    for n in names:
        print("   -", n)


# Aggregate per group — the equivalent of SELECT line, SUM(price) GROUP BY line
totals = defaultdict(float)
counts = defaultdict(int)

for p in products:
    totals[p["line"]] += p["price"]
    counts[p["line"]] += 1


print(totals)
print(counts)


print()
for line in totals:
    print(f"total={totals[line]:.3f}  avg={totals[line]/counts[line]:0.2f}")