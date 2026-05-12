class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        min_sum = float('inf')
        found = False
        
        # Brute force through all possible triplets
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if it's a mountain triplet
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        current_sum = nums[i] + nums[j] + nums[k]
                        min_sum = min(min_sum, current_sum)
                        found = True
        
        return min_sum if found else -1