class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        from collections import deque
        q = deque([root])
        result = []
        
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                
                # last node of this level
                if i == n - 1:
                    result.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return result