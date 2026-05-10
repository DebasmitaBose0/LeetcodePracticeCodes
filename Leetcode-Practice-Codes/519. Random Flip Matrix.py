import random

class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.mapping = {}
        self.current_size = self.total

    def flip(self) -> List[int]:
        # Pick a random index from the remaining "virtual" pool
        idx = random.randint(0, self.current_size - 1)
        self.current_size -= 1
        
        # Check if idx has been swapped before; if not, the actual value is idx
        res_idx = self.mapping.get(idx, idx)
        
        # Swap the picked value with the value at the current end of the pool
        # This ensures the picked value is "removed" and the pool stays contiguous
        self.mapping[idx] = self.mapping.get(self.current_size, self.current_size)
        
        # Convert 1D index to 2D coordinates
        return [res_idx // self.n, res_idx % self.n]

    def reset(self) -> None:
        # Clear the map and reset the pool size
        self.mapping.clear()
        self.current_size = self.total