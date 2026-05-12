class Solution:
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return
            
            result.append(node.val)  # Root
            dfs(node.left)           # Left
            dfs(node.right)          # Right

        dfs(root)
        return result