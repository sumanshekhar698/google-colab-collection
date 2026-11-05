# BAD: a comprehension used for its side effects, discarding the result
# [print(n) for n in range(3)]     # builds a useless list of Nones

# GOOD:
for n in range(3):
    print(n)

# BAD: unreadable, too much logic crammed in
data = [1, -2, 3, -4, 5]
# result = [x*2 if x > 0 else (x*-1 if x < -2 else 0) for x in data if x != 0]

# GOOD: a plain loop when the logic is non-trivial
result = []
for x in data:
    if x == 0:
        continue
    if x > 0:
        result.append(x * 2)
    elif x < -2:
        result.append(-x)
    else:
        result.append(0)
print(result)