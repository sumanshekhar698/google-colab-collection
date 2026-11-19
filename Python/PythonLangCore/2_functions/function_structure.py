
def show():
    print("Hello, World!")

def greet(name):
    # """Function to greet a person with their name.\n takes input a name""" # docstring
    """
    Greet a person by their name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message containing the person's name.

    Example:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"

greeting = greet("Alice")
print(greeting)  # Output: Hello, Alice!
print(greet.__doc__)  # Output: Function to greet a person with their name.
print(greet.__name__)  # Output: greet
# print(greet.__module__)  # Output: __main__

print(id(greet))  # Output: Object's identity: a number


print()
print(zip.__doc__)  # Output: zip(...)

show()  # Output: Hello, World!
print(show())  # Output: None
print(show.__doc__)  # Output: None


