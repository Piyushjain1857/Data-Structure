rows = int(input("Number of rows : "))
cols = int(input("Number of cols : "))

matrix = [
    [int(input(f"Enter value at [{r}][{c}] : ")) for c in range(cols)]
    for r in range(rows)
]
print("Original Matrix : ")
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=" ")
    print()

# print("Printing Lower Corner : ")

# for r in range(rows):
#     for c in range(r):
#         print(matrix[r][c], end=" ")
#     print()

print("Printing Upper Corner : ")   

for r in range(rows-1):
    for c in range(r+1, cols):
        print(matrix[r][c], end=" ")
    print()