# 1 to 10 -----< make a list of there squares >--------------> [1,4,9,16,25,36,49,64,81,100]


# 1. The loop version...
squares = []
for n in range(1, 11):
    squares.append(n ** 2)
print(squares)


# List Comprehension
squares_2 = [ n**2  for n in range(1,11)]
print(squares_2)


# 1 to 10 -----< make a list of there squares IF (n is even) >--------------> [4,16,36,64,100]

squares_3 = [ n**2  for n in range(1,11) if n % 2 == 0]# if n % 2 == 0 ===> filter
print(squares_3)


squares_4 = [ "even" if n%2 ==0 else "odd" for n in range(1,11)]# ------------>['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
print(squares_4)


squares_5 = [ f"even:{n}" if n%2 ==0 else f"odd:{n}" for n in range(1,11) if n > 3]# ------------>['even:4', 'odd:5', 'even:6', 'odd:7', 'even:8', 'odd:9', 'even:10']
print(squares_5)





products = ["ford town car", "alfa romeo", "grand touring sedan"]

print([p.title() for p in products])
print([len(p) for p in products])
print([p for p in products if "car" in p])
print([p.split()[0] for p in products])         # first word of each