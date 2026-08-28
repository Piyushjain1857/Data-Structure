#upper triangular matrix
rows = 4
columns = 4
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input("Enter the value:"))
        row.append(value)
    matrix.append(row)
print("Matrix")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end=" ")
    print()

for r in range(rows-1):
    for c in range(r+1,columns):
        print("Upper triangular:",matrix[r][c],end=" ")