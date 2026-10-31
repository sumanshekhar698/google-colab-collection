s = "hello"
print(s[0])
print(s[4])

# s[0]="H"#TypeError: 'str' object does not support item assignment
# Strings are immutable

s= "H" + s[1:]
print(s)