n = int(input("Enter the number of rows and columns: "))
matrix = []

print("Enter the matrix elements row by row:")
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

for i in range(n):
    pivot_row = i
    while pivot_row < n and matrix[pivot_row][i] == 0:
        pivot_row += 1

    if pivot_row == n:
        continue

    if pivot_row != i:
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

    pivot_element = matrix[i][i]
    for j in range(n):
        matrix[i][j] /= pivot_element

    for k in range(i + 1, n):
        factor = -matrix[k][i]
        for j in range(n):
            matrix[k][j] += factor * matrix[i][j]

print("Matrix in row echelon form:")
for row in matrix:
    print(row)
