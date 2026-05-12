class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. Search for the node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # 2. Node found! Handle the deletion
            
            # Case 1 & 2: No child or only one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: Two children
            # Find the inorder successor (smallest in the right subtree)
            successor = self.findMin(root.right)
            # Replace current value with successor's value
            root.val = successor.val
            # Delete the successor node
            root.right = self.deleteNode(root.right, successor.val)
            
        return root

    def findMin(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr