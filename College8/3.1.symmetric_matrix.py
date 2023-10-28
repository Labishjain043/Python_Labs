N = int(input("Enter the dimension of the square matrix (N): "))
matrix = []

print(f"Enter elements of the {N}x{N} square matrix row by row:-")
for i in range(N):
    row = [int(x) for x in input(f"Enter row {i + 1} elements separated by spaces: ").split()]
    matrix.append(row)

is_symmetric = "Yes"
for i in range(N):
    for j in range(N):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = "No"

if is_symmetric == "Yes":
    print("The matrix is Symmetric")
else:
    print("The matrix is Not Symmetric")
