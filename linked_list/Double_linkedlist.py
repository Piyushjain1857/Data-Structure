class Node:
    def __init__(self, myData):
        self.prev = None
        self.data = myData
        self.next = None


class DoublyLinkedListADT:
    def __init__(self):
        self.head = None

    def insertAtFirstPosition(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = newNode
            return

        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def insertAtLastPosition(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return

        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = newNode
        newNode.prev = currentNode

    def insertAtPosition(self, data, pos):
        newNode = Node(data)

        if self.head is None:
            if pos == 0:
                self.head = newNode
                return
            else:
                print("Position out of range")
                return

        if pos == 0:
            self.insertAtFirstPos(data)
            return

        currentNode = self.head
        count = 0

        while currentNode and count < pos - 1:
            currentNode = currentNode.next
            count += 1

        if currentNode is None:
            print("Position out of range")
            return

        newNode.next = currentNode.next
        newNode.prev = currentNode

        if currentNode.next:
            currentNode.next.prev = newNode

        currentNode.next = newNode

    # Delete from front
    def deleteAtFirstPosition(self):
        if self.head == None:
            print("List is empty")
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Delete from end
    def deleteAtLastPosition(self):
        if self.head == None:
            print("List is empty")
            return

        currentNode = self.head
        if currentNode.next is None:
            self.head = None
            return

        while currentNode.next:
            currentNode = currentNode.next

        currentNode.prev.next = None

    def deleteAtPosition(self, pos):
        if self.head == None:
            print("List is empty")
            return

        if pos == 0:
            self.deleteAtFirstPosition()
            return

        currentNode = self.head
        count = 0

        while currentNode and count < pos:
            currentNode = currentNode.next
            count += 1

        if currentNode is None:
            print("Position out of range")
            return

        if currentNode.next:
            currentNode.next.prev = currentNode.prev
        else:
            if currentNode.prev:
                currentNode.prev.next = None

        if currentNode.prev:
            currentNode.prev.next = currentNode.next

    # Search element
    def search(self, key):
        currentNode = self.head
        while currentNode:
            if currentNode.data == key:
                return True
            currentNode = currentNode.next
        return False

    # Display forward
    def displayForward(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" <-> ")
            currentNode = currentNode.next
        print("None")

    # Display backward
    def displayBackward(self):
        currentNode = self.head
        if currentNode is None:
            print("List is empty")
            return

        while currentNode.next:
            currentNode = currentNode.next

        while currentNode:
            print(currentNode.data, end=" <-> ")
            currentNode = currentNode.prev
        print("None")


dl1 = DoublyLinkedListADT()
dl1.insertAtLastPos(10)
dl1.insertAtLastPos(20)
dl1.insertAtLastPos(30)
dl1.insertAtLastPos(40)
dl1.insertAtLastPos(50)
dl1.displayForward()  # Output: 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> None



