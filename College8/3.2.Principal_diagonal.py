N = int(input("Enter the dimension of the square matrix (N): "))
matrix = []

print(f"Enter elements of the {N}x{N} square matrix row by row:-")
for i in range(N):
    row = [int(x) for x in input(f"Enter row {i + 1} elements separated by spaces: ").split()]
    matrix.append(row)

principal_diagonal_sum = 0
non_principal_diagonal_sum = 0

for i in range(N):
    principal_diagonal_sum += matrix[i][i]
for i in range(N):
    non_principal_diagonal_sum += matrix[i][N - 1 - i]

print("Sum of principal diagonal elements:", principal_diagonal_sum)
print("Sum of non-principal diagonal elements:", non_principal_diagonal_sum)
