import random
from collections import defaultdict

class Solution:
    def __init__(self, nums: List[int]):
        # Store indices for each number in a dictionary
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        # random.choice is O(1) once the map is built
        return random.choice(self.indices[target])