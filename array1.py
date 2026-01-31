import array as arr

# input list1 = ["Rohit", 18, "KR Mangalam University"]
# output: ["KR Mangalam University", 18, "Rohit"]
# input list2 = [2]
# output: [2]

# marks = [90, 98, 55, 20, 33, 58, 100]
# above_75 = [90, 98, 100]
# below_40 = [55, 20,33, 58]


# list = []

# for i in range(5):
#     list1 = int(input("enter numbers:"))
#     list.append(list1)

# print(list[::-1])


# marks = [90, 98, 55, 20, 33, 58, 100]
# above = 0
# below = 0
# for i in marks:
#     if(i > 75):
#         above += 1
#     elif(i < 40):
#         below += 1
# print(above, below, sep=" ")

# list = [30, 40, 65, 90]

# i = 0
# above = 0
# below = 0
# while i < len(list):
#     if(list[i] > 75):
#         above += 1
#     elif(list[i] < 40):
#         below += 1
#     i += 1
# print(above, below, sep=" ")


# list = [1, 3, 4, -2, -9, 7, -3, 6]
# positive = 0
# negative = 0
# for i in list:
#     if(i > 0):
#         positive += 1
#     elif(i < 0):
#         negative += 1
# print(positive, negative, sep=" ")


# count the numbers of digits of a number

# num = 12345
# count = 0

# while num > 0:
#     num = num // 10
#     count += 1

# print(count)


# count the numbers of digits of a number

# number = 123456789
# count = 0

# while number > 0:
#     number = number // 10
#     count = count + 1

# print(count)


# Reverse a number

# num = 1234
# number = 0

# while num > 0:
#     digit = num % 10

#     number = number*10 + digit

#     num = num // 10

# print(number)


# n = int(input('enter a number: '))
# rev = 0
# sign = 1

# if(n < 0):
#     sign = -1

#     n = n * -1     #n = abs(n)

# while n > 0:

#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print(rev * sign)


# check if a number is palindromic or not

# num = 12321
# original = num
# rev = 0

# while num > 0:
#     digit = num % 10

#     rev = rev*10 + digit

#     num = num // 10

# print(rev)

# if rev == original:
#     print('Number is Palindrome')
# else :
#     print('Number is not Palindrome')


# Check if the given number is Armstrong Number

# num = 370
# original = num
# temp = num
# sum = 0
# count = 0

# while original > 0:
#     original = original // 10
#     count += 1

# print(count)


# while temp > 0:
#     digit = temp % 10

#     sum = sum + digit**count

#     temp = temp // 10

# print(sum)


# if sum == num:
#     print('Given number is a Armstrong number')
# else :
#     print('Given number is not a Armstrong number')


# convert decimal to binary (1017) 1100

# binary = " "
# n = 12

# while n>0:
#     bit = n % 2

#     binary = str(bit) + binary
#     n = n//2

# print(binary)

# convert binary to decimal

# binary = 1011

# decimal = 0

# pow = 0

# while binary > 0:
#     bit = binary % 10
#     decimal += (bit) * 2**pow
#     binary = binary // 10
#     pow += 1

# print(decimal)


# count number of digits of a given number

# n = int(input("Enter a numbers: "))
# count = 0

# while n > 0:
#     n = n // 10
#     count += 1

# print(count)

# reverse a number

# n = int(input("Enter a number: "))

# rev = 0
# original = n

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print(rev)

# reverse a number for both positive and negative value
# n = int(input("Enter a number: "))

# rev = 0
# original = n
# sign = 1

# if n < 0:
#     sign = -1
#     n = n * -1

# while n > 0:
#     digit = n % 10

#     rev = rev * 10 + digit

#     n = n // 10

# print(rev * sign)    #we can check the maxLimit and minLimit if constraints are given


# Check if a number is a Palindrome

# n = int(input("Enter a number: "))
# rev = 0
# original = n

# if n < 0:
#     print("False")

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if rev == original:
#     print("True")
# else:
#     print("False")


# Check if a given number is armstrong or not

# n = int(input("Enter a number: "))
# count = 0
# temp = n
# original = n

# while n > 0:
#     n = n // 10
#     count += 1

# print(count)

# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit**count
#     temp = temp // 10

# print(sum)

# if sum == original:
#     print("Given Number is a Armstrong Number")
# else:
#     print("Given Number is Not a Armstrong Number")

# operation

# 1. Add
# a. Append() creates new array of origanal's double array and copy original array (every time twice new array when array space completes), space available O(1), if space not available O(n)

# arrName.append(10) space O(n)
# print(arrName)
# arrName.insert(0, -9)
# print(arrName)

# b. Insert
# insert(index, value) (when value insert in mid of the array O(n), when insert at the last, time complexity O(1))

# 2. Delete
# a. remove() value search and then delete
# b. pop() or pop(index) delete 2 ways paramete wali O(n), and if without paramete wali the delete last wali O(1)

arrName = arr.array("i", [12, 6, 8, 9, 5])
print(arrName)


arrName.remove(
    12
)  # -->> when remove from 1 st and mid position O(n), when we remove from last position O(1) shifting karni padti h
print(arrName)


arrName.pop(1)

print(arrName)

arrName[0] = 40  # --> values update and access

print(arrName)


for i in range(0, len(arrName), 2):
    print(arrName[i], end=" ")


# sum = 0
# pro = 1

# for val in arrName:
#     sum += val
#     pro *= val

# print("\nSum:", sum)
# print("Product:", pro)


# count ooccurance of a given array
# arr_to_search = 40
# count = 0

# for val in arrName:
#     if val == arr_to_search:
#         count += 1

# print(f"Occurrences of {arr_to_search}: {count}")

# check if an array is sorted forwad, backward, or not at all

# is_sorted_forward = True
# is_sorted_backward = True
# n = len(arrName)
# for i in range(n - 1):
#     if arrName[i] > arrName[i + 1]:
#         is_sorted_forward = False
#     if arrName[i] < arrName[i + 1]:
#         is_sorted_backward = False


