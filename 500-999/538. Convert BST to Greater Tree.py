# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.running_sum = 0
        
        def traverse(node):
            if not node:
                return
            
            # 1. Visit the Right subtree first (largest values)
            traverse(node.right)
            
            # 2. Update the running sum and the current node's value
            self.running_sum += node.val
            node.val = self.running_sum
            
            # 3. Visit the Left subtree (smallest values)
            traverse(node.left)
            
        traverse(root)
        return root