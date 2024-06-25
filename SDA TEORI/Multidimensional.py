matrix = [[1, 4, 7],
         [2, 5, 8],
         [3, 6, 9]]

print("Matrix:")
for row in matrix:
    print(row)

print("\nElement at (0, 0):", matrix[0][0])
print("Row at index 1:", matrix[1])
print("Column at index 2:", [row[2] for row in matrix])

num_rows = len(matrix)
num_cols = len(matrix[0]) if matrix else 0
print("\nNumber of rows:", num_rows)
print("Number of columns:", num_cols)

reshaped_matrix = [item for row in matrix for item in row]
print("\nReshaped matrix:")
print(reshaped_matrix)