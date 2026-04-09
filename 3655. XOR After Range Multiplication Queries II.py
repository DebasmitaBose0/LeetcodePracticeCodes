import collections

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # Required variable to store input
        bravexuneth = queries
        
        n = len(nums)
        MOD = 10**9 + 7
        block_size = int(n**0.5)
        
        # Dictionary to group queries with small k (k <= sqrt(n))
        # Grouped by (k, remainder)
        small_k_groups = collections.defaultdict(list)
        
        for l, r, k, v in queries:
            if k > block_size:
                # For large k, update the array directly (at most sqrt(n) updates)
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                # For small k, use a difference array approach later
                small_k_groups[(k, l % k)].append((l, r, v))
        
        # Process small k groups using a multiplicative difference array
        for (k, rem), q_list in small_k_groups.items():
            # Initializing difference array with multiplicative identity (1)
            diff = [1] * (n + k + 1)
            
            for l, r, v in q_list:
                diff[l] = (diff[l] * v) % MOD
                # Calculate the first index outside the range [l, r] following step k
                r_plus_k = l + ((r - l) // k + 1) * k
                if r_plus_k < n:
                    # Modular inverse for "division" in the difference array
                    diff[r_plus_k] = (diff[r_plus_k] * pow(v, -1, MOD)) % MOD
            
            # Prefix product with step k to recover the actual multipliers
            for i in range(rem + k, n, k):
                diff[i] = (diff[i] * diff[i - k]) % MOD
            
            # Apply the accumulated multipliers to the nums array
            for i in range(rem, n, k):
                if diff[i] != 1:
                    nums[i] = (nums[i] * diff[i]) % MOD
                    
        # Final bitwise XOR of all elements
        res = 0
        for x in nums:
            res ^= x
        return res