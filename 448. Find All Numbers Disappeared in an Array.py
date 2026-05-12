class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 1. Mark each number's corresponding index as negative
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # 2. If an index remains positive, that number (index + 1) is missing
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
                
        return result