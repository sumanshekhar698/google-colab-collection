# r stands for read mode
with open("order_details.csv","r") as fi:
    print(fi.read())

# default mode with open is read "r"
with open("order_details.csv") as fi:
    print(fi.read())


with open("order_details.csv") as fi:
    print(fi.readline())
    print(fi.readline())


with open("order_details.csv") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())


with open("order_details.csv") as f:
    for line in f:
        print(line.strip())


with open("order_details.csv") as f:
    lines = f.readlines()
    print(type(lines))
    print(lines)