import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # Reservoir Sampling
        res = self.head.val
        curr = self.head.next
        n = 2 # Probability of replacing the result is 1/n
        
        while curr:
            # Generate a random number between 1 and n
            # If it equals 1 (probability 1/n), update the result
            if random.randint(1, n) == 1:
                res = curr.val
            
            curr = curr.next
            n += 1
            
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()