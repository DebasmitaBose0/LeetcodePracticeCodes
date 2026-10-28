# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            
            # Check if this node is a leaf
            if not node.left and not node.right:
                return node.val if is_left else 0
            
            # Recurse through children
            return dfs(node.left, True) + dfs(node.right, False)
        
        # Start DFS with is_left=False because the root is not a left leaf
        return dfs(root, False)