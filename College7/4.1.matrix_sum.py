M = int(input("Enter the number of rows (M): "))
N = int(input("Enter the number of columns (N): "))

matrix1 = [[int(x) for x in input(f"Enter row {i + 1} elements separated by spaces: ").split()] for i in range(M)]
matrix2 = [[int(x) for x in input(f"Enter row {i + 1} elements separated by spaces: ").split()] for i in range(M)]

sum_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(N)] for i in range(M)]

print("Matrix 1:")
for row in matrix1:
    print(row)
print("Matrix 2:")
for row in matrix2:
    print(row)
print("Summation Matrix:")
for row in sum_matrix:
    print(row)
