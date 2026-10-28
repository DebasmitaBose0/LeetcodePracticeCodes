class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        curr = head
        while curr:
            # If there is no child, just move to the next node
            if not curr.child:
                curr = curr.next
                continue
            
            # If there is a child, find the tail of the child list
            temp = curr.child
            while temp.next:
                temp = temp.next
            
            # Connect the tail of the child list to curr.next
            temp.next = curr.next
            if curr.next:
                curr.next.prev = temp
            
            # Connect curr to the child and the child to curr
            curr.next = curr.child
            curr.child.prev = curr
            
            # Set child pointer to None as per requirements
            curr.child = None
            
            # Move to the next node (which is now the former child)
            curr = curr.next
            
        return head