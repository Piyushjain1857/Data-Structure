# import math
# def missing_number(num):
#     n = len(num)
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(num)
#     return expected_sum - actual_sum
# arr = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# print(f" Missing number: {missing_number(arr)}")

# max_num = arr[0]
# for num in arr:
#     if num > max_num:
#         max_num = num
# print(f"Maximum number: {max_num}")

# second_max = -math.inf
# for num in arr:
#     if num > second_max and num < max_num:
#         second_max = num
# print(f"Second maximum number: {second_max}")



# print("hello world")


l=0 #largest
l2=0 #second largest
arr=[2,3,56,23,8,9,2]
for i in arr:
    if i>l:
        l2=l
        l=i
    elif i>l2 and i!=l:
        l2=i