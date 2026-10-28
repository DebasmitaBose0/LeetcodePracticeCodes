# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    ListNode = None
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Step 3: Find the maximum twin sum
        max_val = 0
        first_half = head
        second_half = prev  # prev is now the head of the reversed second half
        
        while second_half:
            twin_sum = first_half.val + second_half.val
            max_val = max(max_val, twin_sum)
            first_half = first_half.next
            second_half = second_half.next
            
        return max_val