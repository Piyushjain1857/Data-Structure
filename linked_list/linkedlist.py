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

    def insertAtLastPosition(self, myData):
        new_node = Node(myData)
        if self.head == None:
            self.head = new_node
            return
        currentNode = self.head
        while currentNode.address != None:
            currentNode = currentNode.address
        currentNode.address = new_node
        
    def insertAtPosition(self, position, myData):
        if position == 1:
            self.insertAtFirstPosition(myData)
            return
        new_node = Node(myData)
        currentNode = self.head
        
        # Traverse to the node just before the desired position
        for i in range(position - 2):
            currentNode = currentNode.address
        
        new_node.address = currentNode.address
        currentNode.address = new_node

    def traversal(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.address


myLinkedList = LinkedList()

myLinkedList.insertAtLastPosition(10)
myLinkedList.insertAtLastPosition(20)
myLinkedList.insertAtLastPosition(30)
myLinkedList.insertAtLastPosition(40)
myLinkedList.insertAtLastPosition(50)

myLinkedList.traversal()
