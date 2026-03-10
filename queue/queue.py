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
            mydata = self.queueArray[self.front]
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


myQueue = Queue(5)
print(myQueue.isEmpty())
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
print(myQueue.isFull())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
# print(myQueue.dequeue())
print(myQueue.isEmpty())
myQueue.enqueue(1)
print(myQueue.front1())
print(myQueue.rear1())
myQueue.enqueue(3)
myQueue.enqueue(4)
print(myQueue.front1())
print(myQueue.rear1())
