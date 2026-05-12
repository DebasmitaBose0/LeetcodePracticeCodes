class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        vals = []
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        # Convert string to a deque of integers for O(1) popping
        from collections import deque
        vals = deque(int(x) for x in data.split(","))
        
        def build(low, high):
            if vals and low < vals[0] < high:
                val = vals.popleft()
                node = TreeNode(val)
                # Left children must be between current low and parent's value
                node.left = build(low, val)
                # Right children must be between parent's value and current high
                node.right = build(val, high)
                return node
            return None
        
        return build(float('-inf'), float('inf'))