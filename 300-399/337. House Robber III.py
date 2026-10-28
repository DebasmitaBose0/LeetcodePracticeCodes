# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (Money if robbed, Money if skipped)
            
            # Recurse down to children
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we rob this node, we MUST skip its children
            rob_it = node.val + left[1] + right[1]
            
            # If we skip this node, we take the best of both options from children
            skip_it = max(left) + max(right)
            
            return (rob_it, skip_it)
        
        # The answer is the maximum of the two options at the root
        return max(dfs(root))