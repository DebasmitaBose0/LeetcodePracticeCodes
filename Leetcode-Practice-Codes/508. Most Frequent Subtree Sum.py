import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Dictionary to store {subtree_sum: frequency}
        counts = collections.defaultdict(int)
        
        def get_sum(node):
            if not node:
                return 0
            
            # Post-order: calculate left and right sums first
            left_sum = get_sum(node.left)
            right_sum = get_sum(node.right)
            
            # Current subtree sum
            current_sum = node.val + left_sum + right_sum
            
            # Record the frequency
            counts[current_sum] += 1
            
            return current_sum
        
        # Start DFS
        get_sum(root)
        
        # Find the maximum frequency value
        max_freq = max(counts.values())
        
        # Return all sums that have the max_freq
        return [s for s in counts if counts[s] == max_freq]