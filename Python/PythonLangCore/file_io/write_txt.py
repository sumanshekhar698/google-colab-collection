# "r"	read (default). Errors if the file doesn't exist
# "w"	write. Creates or TRUNCATES — destroys existing content
# "a"	append. Creates if absent, writes at the end
# "x"	exclusive create. Errors if the file exists
# "r+"	read and write
with open("output.txt", "w") as f:
    f.write("Line 1\n")            # \n is NOT added automatically
    f.write("Line 2\n")
    f.writelines(["Line 3\n", "Line 4\n"])


with open("output.txt") as f:
    print(f.read())