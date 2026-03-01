import array as arr

# arr1 = [1, 2, 3, 4, 5, 6, 7]
# k=3

# def Rotate(arr,k):
#     last = arr[-1]
#     while k>0:
#         for i in range(len(arr)-1, 0, -1):
#             arr[i] = arr[i-1]
#         arr[0] = last
#         return arr
#         k -= 1
#     return arr
# print(Rotate(arr1,k))

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

arr1 = [1, 2, 3, 4, 5, 6, 7]
k=3
def rotate(nums, k):
    n = len(nums)
    k = k % n 
    nums= nums[-k:] + nums[:-k] 
    return nums

print(rotate(arr1, k))