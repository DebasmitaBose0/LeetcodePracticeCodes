class Solution:
    def maxSumDivThree(self, nums):
        total = sum(nums)
        
        r1 = sorted([x for x in nums if x % 3 == 1])
        r2 = sorted([x for x in nums if x % 3 == 2])
        
        rem = total % 3
        
        if rem == 0:
            return total
        
        if rem == 1:
            option1 = r1[0] if len(r1) >= 1 else float('inf')
            option2 = r2[0] + r2[1] if len(r2) >= 2 else float('inf')
            return total - min(option1, option2)
        
        if rem == 2:
            option1 = r2[0] if len(r2) >= 1 else float('inf')
            option2 = r1[0] + r1[1] if len(r1) >= 2 else float('inf')
            return total - min(option1, option2)