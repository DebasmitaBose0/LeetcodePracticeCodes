class Solution:
    def countNodes(self, root):
        def getHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        if not root:
            return 0
        
        left_h = getHeight(root.left)
        right_h = getHeight(root.right)
        
        if left_h == right_h:
            # left subtree is perfect
            return (1 << left_h) + self.countNodes(root.right)
        else:
            # right subtree is perfect
            return (1 << right_h) + self.countNodes(root.left)