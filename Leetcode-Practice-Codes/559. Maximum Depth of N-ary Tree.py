"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base case: if the tree is empty
        if not root:
            return 0
        
        # Base case: if the node is a leaf (no children)
        if not root.children:
            return 1
        
        # Recursive step: find the max depth among all children
        max_child_depth = 0
        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child))
            
        # The total depth is 1 (current node) + the maximum depth of its children
        return 1 + max_child_depth