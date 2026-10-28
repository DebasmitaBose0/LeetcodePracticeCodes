# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            
            # Swapping
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move forward
            current = first
        
        return dummy.next