def missing_number(num):
    n = len(num)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(num)
    return expected_sum - actual_sum
arr = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(f" Missing number: {missing_number(arr)}")