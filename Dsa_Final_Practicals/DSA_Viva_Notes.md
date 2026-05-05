# 📘 Data Structures & Algorithms – Viva Notes (Python)

## 👨‍🎓 Student Details
- Name: Piyush Jain  
- Course: BCA (AI & Data Science)  
- University: KR Mangalam University  

---

# 1. Palindrome Number

### 📌 Definition
A number is called a **palindrome** if it reads the same forward and backward.

### 💡 Logic
Reverse the number and compare with original.

### 🧾 Code
```python
def is_palindrome(n):
    original = n
    rev = 0

    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10

    return original == rev
```

### ⏱ Time Complexity
- **O(log n)**

---

# 2. Move Zeros to End

### 📌 Definition
Move all zero elements to the end while maintaining order of non-zero elements.

### 💡 Logic
Use two pointers and swap non-zero elements forward.

### 🧾 Code
```python
def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr
```

### ⏱ Time Complexity
- **O(n)**

---

# 3. Middle of Linked List

### 📌 Definition
Find the middle node of a linked list.

### 💡 Logic
Use slow and fast pointer technique.

### 🧾 Code
```python
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def find_middle(head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data
```

### ⏱ Time Complexity
- **O(n)**

---

# 4. Stack & Queue

## Stack (LIFO)

### 📌 Definition
Last In First Out structure.

```python
class stack:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.stackArray = [None] * capacity

    def push(self, mydata):
        if self.top == self.capacity - 1:
            print("Stack Overfolow")
            return
        self.top += 1
        self.stackArray[self.top] = mydata

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        mydata = self.stackArray[self.top]
        self.top -= 1
        return mydata

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return
        return self.stackArray[self.top]

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def isFull(self):
        if self.top == self.capacity - 1:
            return True
        return False
```

---

## Queue (FIFO)

### 📌 Definition
First In First Out structure.

```python
class Queue:
    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.capacity = capacity
        self.queueArray = [None] * capacity

    def enqueue(self, data):
        if self.rear == self.capacity - 1:
            print("Queue overflow")
            return

        if self.rear == -1:
            self.front = 0
            self.rear = 0
            self.queueArray[self.rear] = data
            return

        self.rear += 1
        self.queueArray[self.rear] = data

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Queue underflow")
            return

        if self.front == self.rear:
            mydata = self.queueArray[self.front]ƒ
            self.front = -1
            self.rear = -1
            return mydata

        mydata = self.queueArray[self.front]
        self.front += 1
        return mydata

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def isFull(self):
        if self.rear == self.capacity - 1:
            return True
        return False

    def front1(self):
        if self.front == -1:
            return
        return self.queueArray[self.front]

    def rear1(self):
        if self.rear == -1:
            return
        return self.queueArray[self.rear]
```

---

# 5. Sorting Algorithms

## Bubble Sort
```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
- **Time Complexity:** O(n²)

## Selection Sort
```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```
- **Time Complexity:** O(n²)

## Insertion Sort
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```
- **Time Complexity:** O(n²)

---

# 6. Searching Algorithms

## Linear Search
```python
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
```
- **Time Complexity:** O(n)

## Binary Search
```python
def binary_search(arr, key):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
- **Time Complexity:** O(log n)

---

# 7. Tree Traversals

- Inorder (Left → Root → Right)
- Preorder (Root → Left → Right)
- Postorder (Left → Right → Root)

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
```

---

# 8. BFS & DFS

## BFS
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])
```

## DFS
```python
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

---

# 9. Sum of Digits
```python
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
```
- **Time Complexity:** O(log n)

---

# 10. Second Maximum Element
```python
def second_max(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second
```
- **Time Complexity:** O(n)

---
