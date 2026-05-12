import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            level_size = len(queue)
            # Initialize max for this specific level with a very small integer
            current_max = float('-inf')
            
            for _ in range(level_size):
                node = queue.popleft()
                current_max = max(current_max, node.val)
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_max)
            
        return result