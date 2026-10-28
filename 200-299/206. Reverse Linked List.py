class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next   # store next node
            curr.next = prev  # reverse pointer
            prev = curr       # move prev forward
            curr = nxt        # move curr forward
        
        return prev