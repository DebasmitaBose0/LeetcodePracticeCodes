from ast import List
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            target_count = 0
            total_count = 0
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                total_count += 1
                
                # Check if target is strictly more than half the subarray size
                if target_count * 2 > total_count:
                    ans += 1
                    
        return ans