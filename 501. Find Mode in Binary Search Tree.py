class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.max_freq = 0
        self.current_freq = 0
        self.current_val = None
        self.modes = []

        def in_order(node):
            if not node:
                return
            
            # Left Subtree
            in_order(node.left)
            
            # Process Current Node
            if node.val == self.current_val:
                self.current_freq += 1
            else:
                self.current_val = node.val
                self.current_freq = 1
            
            # Update Modes
            if self.current_freq > self.max_freq:
                self.max_freq = self.current_freq
                self.modes = [node.val]
            elif self.current_freq == self.max_freq:
                self.modes.append(node.val)
            
            # Right Subtree
            in_order(node.right)

        in_order(root)
        return self.modes