class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # Fenwick Tree (Binary Indexed Tree) Implementation
        # Max possible prefix sum value after shifting is 2 * n + 1
        tree = [0] * (2 * n + 2)
        
        def update(idx: int, delta: int):
            while idx < len(tree):
                tree[idx] += delta
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += tree[idx]
                idx -= idx & (-idx)
            return s

        # The initial prefix sum is 0. 
        # To avoid negative indices, we shift everything by (n + 1).
        shift = n + 1
        
        # Insert pref[0] = 0 into the BIT
        update(0 + shift, 1)
        
        ans = 0
        current_pref = 0
        
        for num in nums:
            # Step 1: Update current prefix sum
            if num == target:
                current_pref += 1
            else:
                current_pref -= 1
            
            # Step 2: Query how many previous prefix sums are strictly smaller
            # We look for elements in the range [1, (current_pref + shift) - 1]
            ans += query(current_pref + shift - 1)
            
            # Step 3: Insert the current prefix sum into the tree
            update(current_pref + shift, 1)
            
        return ans