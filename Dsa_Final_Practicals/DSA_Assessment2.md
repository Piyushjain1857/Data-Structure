# Data Structures & Algorithms - Assessment 2 (Python)

## 1. Matrix Operations

### Row-wise Sum
```python
def row_sum(matrix):
    for i in range(len(matrix)):
        s = 0
        for j in range(len(matrix[i])):
            s = s + matrix[i][j]
        print("Row", i, "sum =", s)

mat = [[1,2,3],[4,5,6],[7,8,9]]
row_sum(mat)
```

### Column-wise Sum
```python
def col_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for j in range(cols):
        s = 0
        for i in range(rows):
            s = s + matrix[i][j]
        print("Column", j, "sum =", s)

col_sum(mat)
```

### Rotate Matrix 90° Clockwise
```python
def rotate_clockwise(matrix):
    n = len(matrix)
    rotated = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        rotated.append(row)

    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]

    return rotated

print(rotate_clockwise(mat))
```

### Rotate Matrix 90° Anti-Clockwise
```python
def rotate_anticlockwise(matrix):
    n = len(matrix)
    rotated = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        rotated.append(row)

    for i in range(n):
        for j in range(n):
            rotated[n-1-j][i] = matrix[i][j]

    return rotated

print(rotate_anticlockwise(mat))
```

---

## 2. Linked List

### Singly Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_last(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    # Insert at position
    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        temp = self.head
        count = 0

        if pos == 0:
            self.insert_first(data)
            return

        while temp != None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp == None:
            print("Invalid Position")
        else:
            new_node.next = temp.next
            temp.next = new_node

    # Delete first
    def delete_first(self):
        if self.head == None:
            print("List is empty")
        else:
            self.head = self.head.next

    # Delete last
    def delete_last(self):
        if self.head == None:
            print("List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None

    # Delete at position
    def delete_at_pos(self, pos):
        if self.head == None:
            print("List empty")
            return

        if pos == 0:
            self.delete_first()
            return

        temp = self.head
        count = 0

        while temp.next != None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp.next == None:
            print("Invalid Position")
        else:
            temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
```

### Doubly Linked List
```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_first(self, data):
        new_node = DNode(data)
        if self.head != None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_last(self, data):
        new_node = DNode(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    # Insert at position
    def insert_at_pos(self, data, pos):
        new_node = DNode(data)
        temp = self.head
        count = 0

        if pos == 0:
            self.insert_first(data)
            return

        while temp != None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp == None:
            print("Invalid Position")
        else:
            new_node.next = temp.next
            if temp.next != None:
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    # Delete first
    def delete_first(self):
        if self.head == None:
            print("List empty")
        else:
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None

    # Delete last
    def delete_last(self):
        if self.head == None:
            print("List empty")
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            if temp.prev != None:
                temp.prev.next = None
            else:
                self.head = None

    # Delete at position
    def delete_at_pos(self, pos):
        if self.head == None:
            print("List empty")
            return

        temp = self.head
        count = 0

        if pos == 0:
            self.delete_first()
            return

        while temp != None and count < pos:
            temp = temp.next
            count += 1

        if temp == None:
            print("Invalid Position")
        else:
            if temp.prev != None:
                temp.prev.next = temp.next
            if temp.next != None:
                temp.next.prev = temp.prev

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
```

### Find Middle Node
```python
def find_middle(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow.data
```

### Detect Cycle
```python
def detect_cycle(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

---

## 3. Stack (Array Implementation)
```python
class Stack:
    def __init__(self, size):
        self.stack = [0] * size
        self.top = -1
        self.size = size

    # Push element
    def push(self, data):
        if self.is_full():
            print("Stack Overflow")
        else:
            self.top = self.top + 1
            self.stack[self.top] = data

    # Pop element
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            val = self.stack[self.top]
            self.top = self.top - 1
            return val

    # Peek (top element)
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]

    # Check if empty
    def is_empty(self):
        if self.top == -1:
            return True
        return False

    # Check if full
    def is_full(self):
        if self.top == self.size - 1:
            return True
        return False

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            i = self.top
            while i >= 0:
                print(self.stack[i], end=" ")
                i = i - 1
            print()
```

---

## 4. Queue (Array Implementation)
```python
class Queue:
    def __init__(self, size):
        self.queue = [0] * size
        self.front = 0
        self.rear = -1
        self.size = size

    def enqueue(self, data):
        if self.rear == self.size - 1:
            print("Queue Overflow")
        else:
            self.rear = self.rear + 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front > self.rear:
            print("Queue Underflow")
        else:
            val = self.queue[self.front]
            self.front = self.front + 1
            return val

    def display(self):
        i = self.front
        while i <= self.rear:
            print(self.queue[i], end=" ")
            i = i + 1
        print()

    def peek(self):
        if self.front > self.rear:
            return None
        return self.queue[self.front]

    def is_empty(self):
        if self.front > self.rear:
            return True
        return False
```