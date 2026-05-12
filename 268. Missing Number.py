class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # The sum of all numbers from 0 to n is (n * (n + 1)) // 2
        expected_sum = (n * (n + 1)) // 2
        
        # The difference between the expected sum and actual sum is the missing number
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum