class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedListADT:
    def __init__(self):
        self.head = None

    # Check if list is empty
    def is_empty(self):
        return self.head is None

    # Insert at beginning
    def insertAtFirstPos(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    # Insert at end
    def insertAtLastPos(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insertAtPos(self, data, pos):
        new_node = Node(data)

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

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Delete from front
    def deleteAtFirstPos(self):
        if self.is_empty():
            print("List is empty")
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Delete from end
    def deleteAtLastPos(self):
        if self.is_empty():
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
        if self.is_empty():
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
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display backward
    def display_backward(self):
        temp = self.head
        if temp is None:
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")
