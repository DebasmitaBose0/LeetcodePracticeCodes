class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Initial capacity: 1 slot for the root node
        slots = 1
        
        for node in preorder.split(','):
            # Each node (whether '#' or a number) consumes one slot
            slots -= 1
            
            # If slots become negative, we have more nodes than the tree allows
            if slots < 0:
                return False
            
            # Non-null nodes create 2 new slots for their children
            if node != '#':
                slots += 2
        
        # A valid tree must have all slots filled exactly
        return slots == 0