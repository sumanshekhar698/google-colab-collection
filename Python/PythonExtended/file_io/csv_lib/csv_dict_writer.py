import csv

# Writing a CSV
rows = [
    {"country": "USA",    "revenue": 1850},
    {"country": "India", "revenue": 2000},
    {"country": "France", "revenue": 1150},
]

with open("summary.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["country","revenue"])
    writer.writeheader()
    writer.writerows(rows)


with open("summary.csv") as f:
    print(f.read())