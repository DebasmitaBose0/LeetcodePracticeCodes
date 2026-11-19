class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        
        # Option 1: change two smallest elements (new min is nums[2])
        option1 = nums[-1] - nums[2]
        
        # Option 2: change two largest elements (new max is nums[-3])
        option2 = nums[-3] - nums[0]
        
        # Option 3: change one smallest and one largest element
        option3 = nums[-2] - nums[1]
        
        return min(option1, option2, option3)