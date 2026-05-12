import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        node = None
        
        while queue:
            # Pop the current node
            node = queue.popleft()
            
            # Push children: RIGHT then LEFT
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        # The last node visited is the bottom-left one
        return node.val