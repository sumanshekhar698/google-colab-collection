# Set comprehension — dedupes automatically
words = ["car", "bike", "car", "plane", "van"]
set_of_words = {word for word in words}
print(set_of_words)
print({len(w) for w in words})           # distinct lengths
print({w[0] for w in words})             # distinct first letters