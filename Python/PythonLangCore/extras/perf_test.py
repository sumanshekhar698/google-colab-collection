import time


def find_square_of_sum_of_n_bad(n):
    if not isinstance(n, int):
        raise AttributeError("Invalid Datatype, use int")

    squares = [num**2 for num in range(n)]
    print(sum(squares))



def find_square_of_sum_of_n_good(n):
    if not isinstance(n, int):
        raise AttributeError("Invalid Datatype, use int")
    squares = (num**2 for num in range(n))
    print(sum(squares))

start = time.time()
find_square_of_sum_of_n_bad(100000)
end = time.time()
print(f"Delta time for compute Bad= {end-start}")


start = time.time()
find_square_of_sum_of_n_good(100000)
end = time.time()
print(f"Delta time for compute Good = {end-start}")

