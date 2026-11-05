

# BEST for large files: iterate the file object directly.
# It reads one line at a time — memory stays constant regardless of file size.
with open("order_details.csv") as f:
    header = next(f).strip().split(",")     # consume the header
    print("columns:", header)
    for line_no, line in enumerate(f, start=1):
        fields = line.strip().split(",")
        print(line_no, fields)