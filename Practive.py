# class stack:
#     def __init__(self, capacity):
#         self.top = -1
#         self.capacity = capacity
#         self.stackArray = [None] * capacity

#     def push(self, mydata):
#         if self.top == self.capacity - 1:
#             print("Stack Overflow")
#             return
#         self.top += 1
#         self.stackArray[self.top] = mydata

#     def pop(self):
#         if self.top == -1:
#             print("Stack Underflow")
#             return
#         mydata = self.stackArray[self.top]
#         self.top -= 1
#         return mydata

#     def peek(self):
#         if self.top == -1:
#             print("Stack is empty")
#             return
#         return self.stackArray[self.top]

#     def isEmpty(self):
#         if self.top == -1:
#             return True
#         return False

#     def isFull(self):
#         if self.top == self.capacity - 1:
#             return True
#         return False


# class Queue:
#     def __init__(self, capacity):
#         self.front = -1
#         self.rear = -1
#         self.capacity = capacity
#         self.queueArray = [None] * capacity

#     def enqueue(self, mydata):
#         if self.rear == self.capacity - 1:
#             print("stack overflopw")
#             return

#         self.rear += 1
#         self.queueArray[self.rear] = mydata

#     def dequeue(self):
#         if self.front == -1 and self.rear == -1:
#             print("Stack Underflow")
#             return
#         if self.front == self.rear:
#             mydata = self.queueArray[self.front]
#             self.front = -1
#             self.rear = -1
#             return mydata

#         mydata = self.queArray[self.front]
#         self.front += 1
#         return mydata

#     def isEmpty(self):
#         if self.front == -1 and self.rear == -1:
#             return True
#         return False

#     def isFull(self):
#         if self.rear == self.capacity - 1:
#             return True
#         return False

#     def front1(self):
#         if self.front == -1:
#             return
#         return self.queueArray[self.front]

#     def rear1(self):
#         if self.rear == -1:
#             return
#         return self.queueArray[self.rear]


# class Matrix:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.matrix = [[0 for j in range(cols)] for i in range(rows)]

#     def insert(self, row, col, value):
#         self.matrix[row][col] = value

#     def display(self):
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 print(self.matrix[i][j], end=" ")
#             print()

#     def traverse(self):
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 print(self.matrix[i][j])


# class ArrayADT:
#     def __init__(self, capacity):
#         self.length = 0
#         self.capacity = capacity
#         self.arr = [None] * capacity

#     def insert(self, value):
#         if self.length == self.capacity:
#             print("Array is full")
#             return
#         self.arr[self.length] = value
#         self.length += 1

#     def traverse(self):
#         for i in range(self.length):
#             print(self.arr[i], end=" ")

#     def search(self, key):
#         for i in range(self.length):
#             if self.arr[i] == key:
#                 return i
#         return -1
