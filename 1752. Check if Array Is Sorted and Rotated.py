class Solution:
    def check(self, nums: List[int]) -> bool:
        count_breaks = 0
        n = len(nums)
        
        for i in range(n):
            # Use modulo to easily handle the wrap-around check (nums[-1] vs nums[0])
            if nums[i] > nums[(i + 1) % n]:
                count_breaks += 1
                
            # If we find more than one break, it's impossible to be a sorted, rotated array
            if count_breaks > 1:
                return False
                
        return True