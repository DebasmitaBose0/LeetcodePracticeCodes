class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # dict to store {prefix_sum : count}
        # Initialize with 0:1 to account for paths starting from the root
        prefix_sums = {0: 1}
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the prefix sum for the current node
            current_sum += node.val
            
            # How many paths end here that sum to targetSum?
            # (current_sum - old_sum = targetSum) => (old_sum = current_sum - targetSum)
            count = prefix_sums.get(current_sum - targetSum, 0)
            
            # Add current_sum to map for child nodes to use
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            # Recurse to children
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # Backtrack: remove current_sum so it's not used by parallel branches
            prefix_sums[current_sum] -= 1
            
            return count
        
        return dfs(root, 0)