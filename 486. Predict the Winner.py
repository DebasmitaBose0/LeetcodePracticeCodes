from typing import List
from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def max_score_diff(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            # Choose left element vs choose right element
            pick_left = nums[left] - max_score_diff(left + 1, right)
            pick_right = nums[right] - max_score_diff(left, right - 1)
            
            return max(pick_left, pick_right)
        
        # Player 1 wins if the net score difference is >= 0
        return max_score_diff(0, len(nums) - 1) >= 0