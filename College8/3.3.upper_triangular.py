N = int(input("Enter the dimension of the square matrix (N): "))
matrix = []

print(f"Enter elements of the {N}x{N} square matrix row by row:-")
for i in range(N):
    row = [int(x) for x in input(f"Enter row {i + 1} elements separated by spaces: ").split()]
    matrix.append(row)

is_upper_triangular = "Yes"
for i in range(N):
    for j in range(i + 1, N):
        if matrix[i][j] != 0:
            is_upper_triangular = "No"
if is_upper_triangular == "Yes":
    print("Matrix is upper triangular: Yes")
else:
    print("Matrix is upper triangular: No")
