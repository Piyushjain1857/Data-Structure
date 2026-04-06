# a = 45621
# s1=str(a)
# l1=list(s1)

# print(len(l1))

# print(len(list(str(a))))


# count no of digits
# n = 345621
# counter = 0
# while n > 0:
#     n //= 10
#     counter += 1

# print(counter)


# no reverce
# num = 345621
# r_num = 0
# while num > 0:
#     digit = num % 10
#     r_num = r_num * 10 + digit
#     num //= 10

# print(r_num)

# palindromic
# def is_palindromic(num):
#     original = num
#     reversed_num = 0
#     while num > 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10
#     return original == reversed_num


# num = 12321
# print(f"{num} is palindromic: {is_palindromic(num)}")


# armstrong
# original = num
# num_digits = len(str(num))
# sum_of_powers = 0
# while num > 0:
#     digit = num % 10
#     sum_of_powers += digit ** num_digits
#     num //= 10
# original == sum_of_powers
# num = 153
# print(f"{num} is armstrong: {num}")



# decimal to binary conversion
# def binary_no_convert(n):
#     if n == 0:
#         return "0"
#     binary = ""
#     while n > 0:
#         binary = str(n % 2) + binary
#         n //= 2
#     return binary

# n = 12
# print(f"{n} in binary: {binary_no_convert(n)}")

#   binary to decimal conversion
# def decimal_no(n):
#     result = 0
#     for i in n:
#         result = result * 2 + int(i)
#     return result

# n = "111"
# print(n, "in decimal:", decimal_no(n))

# array = [1, 2, 3, 4, 5]
# k=2
# def rotate_array(arr, k):
#     k = k % len(arr)
#     return arr[-k:] + arr[:-k]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)