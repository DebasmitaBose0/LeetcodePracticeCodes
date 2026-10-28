class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # Case 1: quadTree1 is a leaf
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        
        # Case 2: quadTree2 is a leaf
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        
        # Case 3: Both are internal nodes
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        
        # Optimization: Check if all children can be merged into one leaf
        children = [topLeft, topRight, bottomLeft, bottomRight]
        if all(c.isLeaf for c in children) and all(c.val == children[0].val for c in children):
            return Node(children[0].val, True, None, None, None, None)
        
        # Otherwise, return the new internal node
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)