# Tuple as a dict key — a composite key, like SQL's (orderNumber, productCode)
# Dictionary K:V ==> Keys hsould be IMMUTABLE
order_lines = {
    (10100, "S18_1749"): 30,
    (10100, "S18_2248"): 50,
    (10101, "S18_2325"): 25,
}
print(order_lines[(10100, "S18_2248")])



order_lines = {
    [10100, "S18_1749"]: 30,
    [10100, "S18_2248"]: 50,
    [10101, "S18_2325"]: 25,
}
print(order_lines[[10100, "S18_2248"]])  # TypeError: unhashable type: 'list'

# bad = {[1, 2]: "value"}
