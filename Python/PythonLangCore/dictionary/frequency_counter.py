words = ["car", "bike", "car", "plane", "car", "bike"]


# car: 3
# bike: 2
# plane: 1

# 1. The .get() pattern — most common, works everywhere
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("get      :", freq)

# 2. Explicit if/else — verbose but shows the logic
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print("if/else  :", freq)

# 3. setdefault
freq = {}
for w in words:
    freq.setdefault(w, 0)
    freq[w] += 1
print("setdefault:", freq)

# 4. collections.Counter — the shortest, use it when allowed
from collections import Counter
print("Counter  :", dict(Counter(words)))
print(type(Counter(words)))
print("top 2    :", Counter(words).most_common(2))