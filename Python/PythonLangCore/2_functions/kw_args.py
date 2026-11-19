# kw args
def describe(**details):
    print(type(details))

    for k,v in details.items():
        print(f"{k}:{v}")



describe(name="Suman", age=30, citizen_ship="IND")
# describe(name="Suman", age=30, citizen_ship="IND", name="Shekhar") #SyntaxError: keyword argument repeated: name