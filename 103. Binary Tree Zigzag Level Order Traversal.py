from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        res = []
        q = deque([root])
        left = True
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if not left:
                level.reverse()
            
            res.append(level)
            left = not left
        
        return res