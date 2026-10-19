from ast import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lesser = sum(1 for x in nums if x < target)
        count = nums.count(target)
        return list(range(lesser, lesser + count))