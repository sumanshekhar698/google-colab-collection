s = "  Classic Cars Ltd  "
s_dup = s
print(s)
print(repr(s))

# strip is also a method
# method is also a fn
# m=s.strip();
s=s.strip();
print(repr(s))


print(repr(s_dup.lstrip()))
print(repr(s_dup.rstrip()))
print(repr(s_dup.strip()))



# str = s_dup.strip()
# str_upper = str.upper()

print(repr(s_dup.strip()))
print(repr(s_dup.strip().upper()))
print(repr(s_dup.strip().lower()))

print(repr("too much python for today".strip().title()))
print(repr(s_dup.strip().swapcase()))

