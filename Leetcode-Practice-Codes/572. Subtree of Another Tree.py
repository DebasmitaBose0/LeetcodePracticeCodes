# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, it can't contain a subtree
        if not root:
            return False
        
        # 1. Check if the current tree starting at 'root' matches 'subRoot'
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. If not, check the left and right children of 'root'
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s, t):
        # If both are null, they are the same
        if not s and not t:
            return True
        # If only one is null or values differ, they are not the same
        if not s or not t or s.val != t.val:
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)