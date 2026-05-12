class Solution:
    def recoverTree(self, root):
        self.first = self.second = self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            
            self.prev = node
            
            inorder(node.right)
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val