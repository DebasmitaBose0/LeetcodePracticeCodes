# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev_val = None
        
        def in_order(node):
            if not node:
                return
            
            # Traverse Left
            in_order(node.left)
            
            # Process Current Node
            if self.prev_val is not None:
                # Compare current value with the previous one in sorted order
                self.min_diff = min(self.min_diff, node.val - self.prev_val)
            
            # Update previous value for the next comparison
            self.prev_val = node.val
            
            # Traverse Right
            in_order(node.right)
            
        in_order(root)
        return self.min_diff