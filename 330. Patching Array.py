class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        patches = 0
        miss = 1  # Smallest number we can't currently form
        i = 0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                # Use existing number to expand our range
                miss += nums[i]
                i += 1
            else:
                # Patch the array with 'miss' to double our range
                miss += miss
                patches += 1
                
        return patches