
def generate_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def get_numbers():
    return [1, 2, 3, 4, 5]


num_generator = generate_numbers()
print(type(num_generator))
print(num_generator)

print("1st for loop")
for num in num_generator:
    print(num)

# print("2nd for loop")
# for num in num_generator:
#     print(num)


print()
def even_numbers(limit):
    for num in range(2, limit + 1, 2):
        yield num


even_generator = even_numbers(10)

print(next(even_generator,"END"))
print(next(even_generator,"END"))
print(next(even_generator,"END"))
print(next(even_generator,"END"))
print(next(even_generator,"END"))

print(next(even_generator,"END"))
print(next(even_generator,"END"))
print(next(even_generator,"END"))
print(next(even_generator,"END"))
print(next(even_generator,"END"))
print(next(even_generator,"END"))
