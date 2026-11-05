# LBYL: look before you leap
data= {"a":1}
if "b" in data:
    print(data["b"])
else:
    print("key not present")


# EAFP: "Easier to Ask Forgiveness than Permission"
try:
    value = data["b"]
except KeyError as e:
    print("key not present")