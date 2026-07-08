from ast import List
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # 1. Filter out non-zero digits and track their original indices
        # non_zero_vals[i] stores the numerical value of the i-th non-zero digit
        non_zero_vals = []
        # original_pos[i] stores the index in string 's' where this non-zero digit appeared
        original_pos = []
        
        for i, ch in enumerate(s):
            if ch != '0':
                non_zero_vals.append(int(ch))
                original_pos.append(i)
                
        k = len(non_zero_vals)
        if k == 0:
            return [0] * len(queries)
            
        # 2. Precompute Prefix Sums for the values of non-zero digits
        prefix_sum = [0] * (k + 1)
        for i in range(k):
            prefix_sum[i + 1] = prefix_sum[i] + non_zero_vals[i]
            
        # 3. Precompute Prefix Concatenation values modulo MOD
        # pref_val[i] represents the number formed by the first i non-zero digits % MOD
        pref_val = [0] * (k + 1)
        for i in range(k):
            pref_val[i + 1] = (pref_val[i] * 10 + non_zero_vals[i]) % MOD
            
        # 4. Precompute powers of 10 modulo MOD for rapid scaling
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        import bisect
        ans = []
        
        for l, r in queries:
            # Find the range of indices in our non_zero_vals array that fall within [l, r]
            idx_start = bisect.bisect_left(original_pos, l)
            idx_end = bisect.bisect_right(original_pos, r) - 1
            
            # If no non-zero digits exist in the range s[l..r]
            if idx_start > idx_end:
                ans.append(0)
                continue
                
            # Number of non-zero digits in this query range
            num_digits = idx_end - idx_start + 1
            
            # Extract the digit sum using the prefix array
            digit_sum = prefix_sum[idx_end + 1] - prefix_sum[idx_start]
            
            # Extract the concatenated value x using the prefix value math formula:
            # x = (pref_val[idx_end + 1] - pref_val[idx_start] * 10^(num_digits)) % MOD
            x = (pref_val[idx_end + 1] - pref_val[idx_start] * pow10[num_digits]) % MOD
            
            # Compute the final query answer
            ans.append((x * digit_sum) % MOD)
            
        return ans