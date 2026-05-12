class Solution:
    def canWinNim(self, n: int) -> bool:
        # You can win if n is not divisible by 4
        return n % 4 != 0