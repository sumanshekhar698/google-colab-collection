import csv


total_rev = 0
with open("order_details.csv") as f:
    d_reader = csv.DictReader(f)
    print(type(d_reader))
    for row in d_reader:
        # print(type(row))
        # print(row)
        line_total = int(row["quantityOrdered"]) * float(row["priceEach"])
        total_rev +=  line_total
        print(f"{row['orderNumber']} {row['productCode']:<10} {line_total:>9.2f}")

print(f"\nTOTAL: {total_rev:.2f}")