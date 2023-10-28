M = int(input("Enter the number of rows (M) for the first matrix: "))
N = int(input("Enter the number of columns (N) for the first matrix / rows for the second matrix: "))
P = int(input("Enter the number of columns (P) for the second matrix: "))
matrix1 = [[int(x) for x in input(f"Enter row {i + 1} elements separated by spaces: ").split()] for i in range(M)]
matrix2 = [[int(x) for x in input(f"Enter row {i + 1} elements separated by spaces: ").split()] for i in range(N)]

if N != len(matrix2):
    print("Matrix multiplication is not possible!")
else:
    result_matrix = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(N)) for j in range(P)] for i in range(M)]

    print("Matrix 1:")
    for row in matrix1:
        print(row)
    print("Matrix 2:")
    for row in matrix2:
        print(row)
    print("Result Matrix (Multiplication):")
    for row in result_matrix:
        print(row)
