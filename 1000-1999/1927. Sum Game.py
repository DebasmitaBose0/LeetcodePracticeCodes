class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left_sum = sum(int(c) for c in num[:half] if c != '?')
        right_sum = sum(int(c) for c in num[half:] if c != '?')
        
        left_q = num[:half].count('?')
        right_q = num[half:].count('?')
        
        # If total '?' is odd, Alice wins
        if (left_q + right_q) % 2 != 0:
            return True
        
        # Bob wins if and only if the sum difference is balanced by ? difference at 4.5 per '?'
        # (left_sum - right_sum) + (left_q - right_q) * 4.5 == 0
        # Multiplied by 2 to avoid floating point issues:
        return 2 * (left_sum - right_sum) + 9 * (left_q - right_q) != 0