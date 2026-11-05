matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


flat = [cell for row in matrix for cell in row ]
print(flat)



flat = []
for row in matrix:            # outer
    for cell in row:          # inner
        flat.append(cell)
print(flat)


# [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix_gen = [[i*j for i in range(1,4)] for j in range(1,4) ]
print(matrix_gen)



flat = [cell for row in matrix for cell in row if cell % 2==0 ]
print(flat)