class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            # If both nodes are smaller → go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # If both nodes are greater → go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # Split point → this is LCA
            else:
                return root