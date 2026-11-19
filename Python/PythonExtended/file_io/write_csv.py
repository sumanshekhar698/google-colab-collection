# Write a sample CSV we can practise on
import os

csv_content = """orderNumber,productCode,quantityOrdered,priceEach
10190,S18_1749,30,136.00
10100,S18_2248,50,55.09
10100,S18_4409,22,75.46
10101,S18_2325,25,108.06
10101,S18_2795,26,167.06
"""

with open("order_details.csv","w") as fi:
    fi.write(csv_content)


for file in os.listdir("."):
    if file.endswith(".csv"):
        print(file)