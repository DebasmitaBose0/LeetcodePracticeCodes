from ast import List
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Square all numbers and sort them in ascending order
        squared = sorted([x * x for x in nums])
        n = len(squared)
        
        # The first half (smaller values) will be subtracted,
        # and the second half (larger values) will be added.
        mid = n // 2
        
        # Subtract the sum of the smaller half and add the sum of the larger half
        return sum(squared[mid:]) - sum(squared[:mid])