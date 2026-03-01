from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        i = 0
        current = l1

        while current:
            print(current.val , i)
            num1 += current.val * (10 ** i)
            current = current.next
            i += 1
        
        print(num1)

        # Convert integer back to linked list (reverse order)
        if num1 == 0:
            return ListNode(0)

        dummy = ListNode(0)
        current_node = dummy

        while num1 > 0:
            digit = num1 % 10
            current_node.next = ListNode(digit)
            current_node = current_node.next
            num1 //= 10

        return dummy.next
        
s = Solution()
l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])

print(s.addTwoNumbers(l1, l2))