# r stands for read mode
# with open("order_details.csv","r") as fi:
#     print(fi.read())
    # print(fi.read())
    # print(fi.read())
    # print(fi.read())

# default mode with open is read "r"
# with open("order_details.csv") as fi:
#     print(fi.read())


# with open("order_details.csv") as fi:
#     print(fi.readline(),end="")
#     print(fi.readline(),end="")
#     print(fi.readline(),end="")
    # print(fi.readline(),end="")
    # print(fi.readline(),end="")
    # print(fi.readline(),end="")
    # print(fi.readline(),end="")
    # print(fi.readline(),end="")
    # print(fi.readline(),end="")
    # print(fi.readline(),end="")
    # print(fi.readline(),end="")


# with open("order_details.csv") as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line.strip())


# with open("order_details.csv") as f:
#     for line in f:
#         print(line.strip())


# with open("order_details.csv") as f:
#     lines = f.readlines()
#     print(type(lines))
#     print(lines)



def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


reader = read_file("order_details.csv")
print(type(reader))
print(reader)


print(next(reader,"EOF"))
print(next(reader,"EOF"))
print(next(reader,"EOF"))
print(next(reader,"EOF"))
print(next(reader,"EOF"))
print(next(reader,"EOF"))
print(next(reader,"EOF"))
print(next(reader,"EOF"))
print(next(reader,"EOF"))
