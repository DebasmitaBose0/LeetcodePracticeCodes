# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    TreeNode = None
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node):
            if not node:
                return (0, 0) # (sum, count)
            
            # Post-order traversal: get sum and count from left and right subtrees
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            
            # Check if the node's value equals the average of its subtree
            if total_sum // total_count == node.val:
                self.count += 1
                
            return (total_sum, total_count)
        
        dfs(root)
        return self.count