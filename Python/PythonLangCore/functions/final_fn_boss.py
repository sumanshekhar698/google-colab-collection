def report(title, *rows, sep="|", **meta):
    print("TITLE:", title)
    print("ROWS :", rows)
    print("SEP  :", sep)
    print("META :", meta)


report("Sales", "row1", "row2", sep="-", author="Aditi", year=2005)
print()
report("Sales", "row1", "row2", author="Aditi", year=2005)