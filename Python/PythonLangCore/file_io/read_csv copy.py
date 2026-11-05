# r stands for read mode
def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


file = read_file("order_details.csv")
print(file)

print(next(file))
print(next(file))
print(next(file))
print(next(file))
print(next(file,"End"))
print(next(file,"End"))
print(next(file,"End"))
print(next(file,"End"))