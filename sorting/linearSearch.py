def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example usage
arr = [10, 20, 30, 40]
target = 30

result = linear_search(arr, target)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")