
# Positional arguments with default values
def order(product, quantity=2, price=0.5):# the default args should be at the end of the function signature
    total = quantity * price
    print(f"Order: {product}, Quantity: {quantity}, Price: {price}, Total: {total}$")

order("Apple", 5, 0.8)  # Output: Order: Apple, Quantity: 5, Price: 0.8, Total: 4.0
order("Banana", 10)     # Output: Order: Banana, Quantity: 10, Price: 0.5, Total: 5.0
order("Cherry")         # Output: Order: Cherry, Quantity: 2, Price: 0.5, Total: 1.0


# Keyword arguments
order(quantity=3, product="Date", price=1.2)  # Output: Order: Date, Quantity: 3, Price: 1.2, Total: 3.6
order(product="Elderberry", quantity=1)      # Output: Order: Elderberry, Quantity: 1, Price: 0.5, Total: 0.5