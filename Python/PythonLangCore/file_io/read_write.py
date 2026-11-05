
with open("output.txt", "r+") as f:
    print(type(f))
    print(f.read())
    f.write("new content")



with open("output.txt", "r+") as f:
    f.write("Hello WORLD")
    f.seek(0)
    print(f.read())