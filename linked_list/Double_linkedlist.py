class Node:
    def __init__(self, myData):
        self.prev = None
        self.data = myData
        self.next = None


class DoublyLinkedListADT:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insertAtFirstPos(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = newNode

        else:
            self.head.prev = newNode
            newNode.next = self.head


    # Insert at end
    def insertAtLastPos(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode
        newNode.prev = temp

    def insertAtPos(self, data, pos):
        newNode = Node(data)

        if pos == 0:
            self.insertAtFirstPos(data)
            return

        temp = self.head
        count = 0

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        newNode.next = temp.next
        newNode.prev = temp

        if temp.next:
            temp.next.prev = newNode

        temp.next = newNode

    # Delete from front
    def deleteAtFirstPos(self):
        if self.head == None:
            print("List is empty")
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Delete from end
    def deleteAtLastPos(self):
        if self.head == None:
            print("List is empty")
            return

        temp = self.head
        if temp.next is None:
            self.head = None
            return

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def deleteAtPos(self, pos):
        if self.head == None:
            print("List is empty")
            return

        if pos == 0:
            self.deleteAtFirstPos()
            return

        temp = self.head
        count = 0

        while temp and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    # Search element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Display forward
    def displayForward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display backward
    def displayBackward(self):
        temp = self.head
        if temp is None:
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")
