# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# def Binary_search(arr,target):
#     low=0
#     high=len(arr)-1
#     while low <= high:
#         mid=(high+low)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] <= target:
#             low = mid +1
#         else :
#             high = mid-1
#     return -1

def binary_search2(arr,low, high ,target):

        if low > high:
            return -1
        
        mid=(high+low)//2
        print(low,high,mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            low = mid +1
            return binary_search2(arr,low,high,target)
        else :
            high = mid-1
            return binary_search2(arr,low,high,target)

arr=[1,2,3,4,5,6]
low=0
high=len(arr)-1
target=4
print(binary_search2(arr,low,high,target))



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr