N = int(input("Enter the dimension of the square matrix (N): "))
matrix = []

print(f"Enter elements of the {N}x{N} square matrix row by row:-")
for i in range(N):
    row = [int(x) for x in input(f"Enter row {i + 1} elements separated by spaces: ").split()]
    matrix.append(row)

transpose_matrix = []
for j in range(N):
    row = []
    for i in range(N):
        row.append(0)
    transpose_matrix.append(row)

for i in range(N):
    for j in range(N):
        transpose_matrix[i][j] = matrix[j][i]

print("Transpose of the matrix:")
for row in transpose_matrix:
    print(row)
