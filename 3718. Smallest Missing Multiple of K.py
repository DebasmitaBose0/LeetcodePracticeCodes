class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        current = k
        while current in num_set:
            current += k
        return current