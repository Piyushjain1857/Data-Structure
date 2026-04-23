

# 📘 Sorting & Searching Algorithms (Exam Notes)

## 🔹 1. Selection Sort
Steps:
1. Start from first index
2. Find minimum element in remaining array
3. Swap with current index
4. Repeat till sorted

Dry Run Example:
Array: [64, 25, 12]
Pass 1 → [12, 25, 64]
Pass 2 → [12, 25, 64]

**Idea:** Find the smallest element and place it at correct position
**Time Complexity:** O(n²)

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

```

---

## 🔹 2. Insertion Sort
Steps:
1. Assume first element sorted
2. Pick next element
3. Shift larger elements right
4. Insert element at correct place

Dry Run Example:
[12, 11, 13]
→ [11, 12, 13]

**Idea:** Insert element into sorted part
**Time Complexity:** Best O(n), Worst O(n²)

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr
```

---

## 🔹 3. Bubble Sort
Steps:
1. Compare adjacent elements
2. Swap if wrong order
3. Largest element moves to end each pass

Dry Run Example:
[5,1,4]
→ [1,5,4]
→ [1,4,5]

**Idea:** Swap adjacent elements
**Time Complexity:** Best O(n), Worst O(n²)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

---

## 🔹 4. Merge Sort
Steps:
1. Divide array into halves
2. Recursively sort halves
3. Merge sorted halves

Dry Run Example:
[38,27,43]
→ [38] [27,43]
→ [27,43]
→ [27,38,43]

**Idea:** Divide → Sort → Merge
**Time Complexity:** O(n log n)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
```

---

## 🔹 5. Quick Sort
Steps:
1. Choose pivot
2. Put smaller elements left
3. Put larger elements right
4. Repeat recursively

Dry Run Example:
[10,7,8]
Pivot=10 → [7,8] [10]
→ [7,8,10]

**Idea:** Pivot → left smaller, right larger
**Time Complexity:** Best O(n log n), Worst O(n²)

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)
```

---

## 🔹 6. Linear Search
Steps:
1. Start from first element
2. Compare with target
3. If found, return index
4. Else move next

**Idea:** Check each element
**Time Complexity:** O(n)

```python
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
```

---

## 🔹 7. Binary Search
Steps:
1. Find middle element
2. If equal → found
3. If smaller → search right
4. If larger → search left

Dry Run Example:
[10,20,30,40], target=30
mid=20 → right
mid=30 → found

**Idea:** Divide sorted array
**Time Complexity:** O(log n)

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example usage
arr = [10, 20, 30, 40, 50]
target = 30

result = binary_search(arr, target)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")
```

---

## 🧠 Quick Revision
- Selection, Bubble, Insertion → O(n²)
- Merge, Quick → O(n log n)
- Binary Search needs sorted array
- Quick sort uses pivot
- Merge sort uses divide & merge