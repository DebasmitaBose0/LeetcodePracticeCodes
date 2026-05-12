class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # Track indices of the min and max values seen so far in the valid range
        min_idx = 0
        max_idx = 0
        
        for j in range(indexDifference, len(nums)):
            # The potential i is j - indexDifference
            i = j - indexDifference
            
            # Update prefix min and max indices using 'max_idx' consistently
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
            
            # Check against the min value found so far
            if abs(nums[j] - nums[min_idx]) >= valueDifference:
                return [min_idx, j]
            
            # Check against the max value found so far
            if abs(nums[j] - nums[max_idx]) >= valueDifference:
                return [max_idx, j]
                
        return [-1, -1]