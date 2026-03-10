class Node:
    def __init__(self, mydata):
        self.data = mydata
        self.address = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFirstPosition(self, new_data):
        new_node = Node(new_data)
        new_node.address = self.head
        self.head = new_node

    def insertAtLastPosition(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        currentNode = self.head
        while currentNode.address != None:
            currentNode = currentNode.address
        currentNode.address = new_node
        
    def insertAtPosition(self, position, new_data):
        if position == 1:
            self.insertAtFirstPosition(new_data)
            return
        new_node = Node(new_data)
        currentNode = self.head
        
        # Traverse to the node just before the desired position
        for i in range(position - 2):
            currentNode = currentNode.address
        
        new_node.address = currentNode.address
        currentNode.address = new_node

    def deleteFirst(self):
        if self.head == None:
            return
        self.head = self.head.address

    def deleteLast(self):
        if self.head == None:
            return
        if self.head.address == None:
            self.head = None
            return
        currentNode = self.head
        while currentNode.address.address != None:
            currentNode = currentNode.address
        currentNode.address = None

    def deleteAtPosition(self, position):
        if self.head == None:
            return
        if position == 1:
            self.deleteFirst()
            return
        currentNode = self.head
        for i in range(position - 2):
            currentNode = currentNode.address
        if currentNode.address == None:
            return
        currentNode.address = currentNode.address.address

    def traversal(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.address


myLinkedList = LinkedList()

myLinkedList.insertAtLastPosition(10)
myLinkedList.insertAtLastPosition(20)
myLinkedList.insertAtLastPosition(30)
myLinkedList.insertAtLastPosition(40)
myLinkedList.insertAtLastPosition(50)

myLinkedList.traversal()
