import sys
# List comprehension: builds the WHOLE list in memory
list_comp = [n ** 2 for n in range(100_000)]# EAGER
print(type(list_comp))


gen_exp = (n ** 2 for n in range(100_000))#LAZY
print(type(gen_exp))

print("list size:", sys.getsizeof(list_comp), "bytes")
print("gen  size:", sys.getsizeof(gen_exp), "bytes")

print(sum(list_comp))
print(sum(list_comp))

print()
range_sum=sum(gen_exp)
print(sum(gen_exp)) # generator can be sonsumed only once
print(sum(gen_exp))




# Use a generator when you only need to aggregate, not store
print(sum(n ** 2 for n in range(1000)))            # no brackets needed inside sum()
print(max(len(w) for w in ["car", "bicycle", "van"]))

print(any(n > 100 for n in [5, 50, 500]))
print(all(n > 0 for n in [5, 50, 500]))