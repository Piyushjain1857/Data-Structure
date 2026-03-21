

# # Doubly Linked List ADT Implementation in Python

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     # Insert at beginning
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         if self.head is not None:
#             self.head.prev = new_node
#             new_node.next = self.head
#         self.head = new_node

#     # Insert at end
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
        
#         temp = self.head
#         while temp.next:
#             temp = temp.next
        
#         temp.next = new_node
#         new_node.prev = temp

#     # Delete a node
#     def delete(self, key):
#         temp = self.head

#         while temp:
#             if temp.data == key:
#                 # If node to be deleted is head
#                 if temp.prev is None:
#                     self.head = temp.next
#                     if self.head:
#                         self.head.prev = None
#                 else:
#                     temp.prev.next = temp.next
#                     if temp.next:
#                         temp.next.prev = temp.prev
#                 return
#             temp = temp.next
#         print("Value not found")

#     # Display forward
#     def display_forward(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" <-> ")
#             temp = temp.next
#         print("None")

#     # Display backward
#     def display_backward(self):
#         temp = self.head
#         if temp is None:
#             return
        
#         while temp.next:
#             temp = temp.next
        
#         while temp:
#             print(temp.data, end=" <-> ")
#             temp = temp.prev
#         print("None")


# # Example usage
# if __name__ == "__main__":
#     dll = DoublyLinkedList()

#     dll.insert_at_beginning(10)
#     dll.insert_at_beginning(5)
#     dll.insert_at_end(20)
#     dll.insert_at_end(25)

#     print("Forward:")
#     dll.display_forward()

#     print("Backward:")
#     dll.display_backward()

#     dll.delete(20)
#     print("After deletion:")
#     dll.display_forward()