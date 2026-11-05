name, qty, price = "Ford Town Car", 555551, 121.647


print(f"{name}: {qty} units at ${price} each")
print(f"{name}: {qty} units at ${price:.1f} each")
print(f"{name}: {qty} units at ${price:.2f} each")
print(f"{name}: {qty} units at ${price:.3f} each")

print(f"Total cost: ${qty * price}")
print(f"Total cost: ${qty * price:.2f}")
print(f"Total cost: ${qty * price:,.2f}")


print(f"{name:<20}|{qty:>10}|")                    # left / right align
print(f"{price:>10.2f}")                          # width 10, 2 dp



print(f"{0.4567:.2%}")                            # 45.7%  percentage
print(f"{name=}, {qty=}, {price=}") # Useful for debugging, shows variable name and value (Python 3.8+)