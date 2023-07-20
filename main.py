def multiplication(matrix, scalar):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = matrix[i][j] * scalar
    return matrix

matrix = [list(map(int, input().split())) for _ in range(int(input("Enter the number of rows: ")))]
B = int(input("Enter the scalar value: "))
matrix = multiplication(matrix,B)
print("Result of scalar multiplication:")
print(matrix)
