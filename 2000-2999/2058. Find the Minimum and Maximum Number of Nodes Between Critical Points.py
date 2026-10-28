# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from typing import List
class Solution:
    ListNode = None
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_node = head
        if not prev_node or not prev_node.next or not prev_node.next.next:
            return [-1, -1]
        
        curr_node = head.next
        index = 2
        
        first_critical_index = -1
        prev_critical_index = -1
        min_distance = float('inf')
        max_distance = -1
        
        while curr_node.next:
            next_node = curr_node.next
            
            # Check for local maxima or local minima
            if (curr_node.val > prev_node.val and curr_node.val > next_node.val) or \
               (curr_node.val < prev_node.val and curr_node.val < next_node.val):
                
                if first_critical_index == -1:
                    first_critical_index = index
                else:
                    # Update minimum distance with adjacent critical points
                    min_distance = min(min_distance, index - prev_critical_index)
                
                # Update max distance dynamically to the distance from the first critical point
                max_distance = index - first_critical_index
                prev_critical_index = index
            
            prev_node = curr_node
            curr_node = next_node
            index += 1
            
        if min_distance == float('inf'):
            return [-1, -1]
        
        return [min_distance, max_distance]