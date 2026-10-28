from collections import Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Count total frequencies of all numbers (initially all are to the "right")
        right_freq = Counter(nums)
        # Keep track of frequencies to the "left"
        left_freq = Counter()
        
        total_count = 0
        
        for j in range(n):
            current_val = nums[j]
            target = current_val * 2
            
            # This element is no longer to the "right" of the current middle
            right_freq[current_val] -= 1
            
            # If target exists both to the left and to the right
            if target in left_freq and target in right_freq:
                contribution = left_freq[target] * right_freq[target]
                total_count = (total_count + contribution) % MOD
            
            # Add current element to "left" frequency for the next iteration
            left_freq[current_val] += 1
            
        return total_count