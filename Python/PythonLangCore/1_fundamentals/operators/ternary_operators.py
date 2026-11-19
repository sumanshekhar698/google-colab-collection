# Useful for defaults
name = input("Enter your name: ")
display = name if name else "Anonymous"
print(display)


display = name or "Anonymous"
print(display)