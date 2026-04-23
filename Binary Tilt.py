# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0

        def get_sum(node):
            if not node:
                return 0
            
            # Recursive calls to get the sum of left and right subtrees
            left_sum = get_sum(node.left)
            right_sum = get_sum(node.right)
            
            # Calculate tilt for the current node and add to total
            self.total_tilt += abs(left_sum - right_sum)
            
            # Return the total sum of values in this subtree
            return node.val + left_sum + right_sum

        get_sum(root)
        return self.total_tilt