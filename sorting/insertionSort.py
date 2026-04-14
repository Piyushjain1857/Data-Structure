def insertion_sort(arr):
    n= len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


# Example usage
arr = [7, -8, 2, 3, 0, 5, -18]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
