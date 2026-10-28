import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Solving k(k+1)/2 <= n for k
        # k = (sqrt(8n + 1) - 1) / 2
        return int((math.sqrt(8 * n + 1) - 1) / 2)