# key= controls what to sort BY
import re


words = ["banana", "kiwi", "apple", "fig"]

print(sorted(words))  # Output: ['apple', 'banana', 'fig', 'kiwi']
print(sorted(words, key=len))  # Output: ['fig', 'apple', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # Output: ['banana', 'kiwi', 'apple', 'fig']
print(words)  # Output: ['banana', 'kiwi', 'apple', 'fig'] (original list remains unchanged)
