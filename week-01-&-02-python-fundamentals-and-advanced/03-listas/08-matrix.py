
matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [9, 8, 7]
]

print(matrix) # [[1, 2, 3], [2, 4, 6], [9, 8, 7]]
print(matrix[1]) # [[1, 2, 3]]
print(matrix[1][1]) # 4

matrix[1][1] = 10

print(matrix)# [[1, 2, 3], [2, 10, 6], [9, 8, 7]]