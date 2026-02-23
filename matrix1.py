matrix = []

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for i in range(rows):
    r = []
    for j in range(cols):
        value = int(input(f"Enter value for position [{i}][{j}]: "))
        r.append(value)
    matrix.append(r)

print("Matrix:")
for r in matrix:
    print(r)