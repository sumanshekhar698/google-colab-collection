# "w" — create or overwrite
with open("output.txt", "a") as f:
    f.write("Line 1\n")            # \n is NOT added automatically
    f.write("Line 2\n")
    f.writelines(["Line 3\n", "Line 4\n"])


with open("output.txt") as f:
    print(f.read())