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

myStack = stack(5)
print(myStack.isEmpty())
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
print(myStack.isFull())
print(myStack.peek())
print(myStack.pop())    
print(myStack.peek())   
print(myStack.pop())
print(myStack.peek())   
print(myStack.pop())
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())
print(myStack.pop())
print(myStack.isEmpty())    