class Solution:
    def maxPathSum(self, root):
        self.res = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)
            
            self.res = max(self.res, node.val + l + r)
            
            return node.val + max(l, r)
        
        dfs(root)
        return self.res