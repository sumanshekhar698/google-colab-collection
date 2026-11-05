from pathlib import Path
import csv

# currency_path = r"C:\Users\suman\Downloads\code\G Collab\google-colab-collection\currency.csv"
# country_path = Path("C:\Users\suman\Downloads\code\G Collab\google-colab-collection\country_full.csv")
country_path = r"C:\Users\suman\Downloads\code\G Collab\google-colab-collection\country_full.csv"

with open("country_full.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("header", header)
    for row in reader:
        print(row)
