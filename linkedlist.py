class Node:
    def __init__(self, mydata):
        self.data = mydata
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtFirstPosition(self, new_data):
        new_node = Node(new_data)
        new_node.address = self.head
        self.head = new_node

    def traversal(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.address

myLinkedList = LinkedList()
myLinkedList.insertAtFirstPosition(10)
myLinkedList.insertAtFirstPosition(20)
myLinkedList.insertAtFirstPosition(30)
myLinkedList.insertAtFirstPosition(40)
myLinkedList.insertAtFirstPosition(50)


myLinkedList.traversal()