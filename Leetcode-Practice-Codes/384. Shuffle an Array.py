import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.array = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and returns it.
        """
        self.array = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # Fisher-Yates Shuffle
        for i in range(len(self.array)):
            # Pick a random index from i to the end of the array
            swap_idx = random.randrange(i, len(self.array))
            # Swap current element with the randomly picked element
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
            
        return self.array