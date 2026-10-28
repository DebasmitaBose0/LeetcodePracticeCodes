# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty or single-node lists
        if not head:
            return None
        
        odd = head
        even = head.next
        evenHead = even # Save the start of the even list
        
        # Traverse while there are still even nodes to process
        while even and even.next:
            # Connect current odd node to the next odd node
            odd.next = even.next
            odd = odd.next
            
            # Connect current even node to the next even node
            even.next = odd.next
            even = even.next
            
        # Attach the even list to the end of the odd list
        odd.next = evenHead
        
        return head