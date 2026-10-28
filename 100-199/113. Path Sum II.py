class Solution:
    def pathSum(self, root, targetSum):
        res = []
        
        def dfs(node, curr, path):
            if not node:
                return
            
            curr += node.val
            path.append(node.val)
            
            if not node.left and not node.right and curr == targetSum:
                res.append(path[:])
            
            dfs(node.left, curr, path)
            dfs(node.right, curr, path)
            
            path.pop()
        
        dfs(root, 0, [])
        return res