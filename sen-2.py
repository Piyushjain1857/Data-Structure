#  2.⁠ ⁠Write a Python program to perform insertion and deletion operations in an Array.
class Array:
    def __init__(self):
        self.array = []

    def insertAtFirstPosition(self, Data):
        self.array.insert(0, Data)

    def insertAtLastPosition(self, Data):
        self.array.append(Data)

    def insertAtPosition(self, position, Data):
        if position < 1 or position > len(self.array) + 1:
            print("Invalid position")
            return
        self.array.insert(position - 1, Data)

    def deleteFirst(self):
        if not self.array:
            print("Array is empty")
            return
        self.array.pop(0)

    def deleteLast(self):
        if not self.array:
            print("Array is empty")
            return
        self.array.pop()

    def deleteAtPosition(self, position):
        if position < 1 or position > len(self.array):
            print("Invalid position")
            return
        self.array.pop(position - 1)