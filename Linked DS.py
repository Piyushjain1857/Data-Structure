import array as arr

arrName = arr.array('i', [1, 2, 3, 4, 5])
print("Array Name:", arrName)
print("Type of arrName:", type(arrName))
print("Array elements:")
for element in arrName:
    print(element)
    
n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime")