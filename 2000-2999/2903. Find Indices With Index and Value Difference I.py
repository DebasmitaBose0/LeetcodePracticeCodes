class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        
        # Check every pair (i, j)
        for i in range(n):
            for j in range(n):
                # Condition 1: Index difference
                # Condition 2: Value difference
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        
        # If no such pair exists
        return [-1, -1]