class Solution:
    def summaryRanges(self, nums):
        result = []
        
        if not nums:
            return result
        
        start = nums[0]
        
        for i in range(1, len(nums)):
            # break in sequence
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                
                start = nums[i]
        
        # handle last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result