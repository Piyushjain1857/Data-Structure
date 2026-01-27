import array as arr

arrName = arr.array('i', [1, 2, 3, 4, 5])
print("Array Name:", arrName)
print("Type of arrName:", type(arrName))
print("Array elements:")
for element in arrName:
    print(element)  