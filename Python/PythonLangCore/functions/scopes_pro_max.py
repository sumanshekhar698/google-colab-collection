counter = 0


def increment_broken():
    # print(counter)
    # counter = 5
    counter += 1
    print(counter)
    # counter = counter + 1


def increment_working():
    global counter
    counter += 1
    # print(counter)

def increment_good(val):
    return val + 1


# increment_working()
# increment_working()
# increment_working()
# increment_working()

counter = increment_good(counter)
counter = increment_good(counter)
counter = increment_good(counter)
counter = increment_good(counter)
counter = increment_good(counter)
print(counter)