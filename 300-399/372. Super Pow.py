class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        res = 1
        # Reduce a to be within the MOD range
        a %= MOD
        
        for digit in b:
            # (previous_result^10 * a^digit) % 1337
            res = pow(res, 10, MOD) * pow(a, digit, MOD) % MOD
            
        return res