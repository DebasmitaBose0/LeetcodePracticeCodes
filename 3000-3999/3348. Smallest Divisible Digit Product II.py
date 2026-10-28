class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t
        c2 = c3 = c5 = c7 = 0
        temp = t
        for p, count_var in [(2, 'c2'), (3, 'c3'), (5, 'c5'), (7, 'c7')]:
            while temp % p == 0:
                temp //= p
                if p == 2: c2 += 1
                elif p == 3: c3 += 1
                elif p == 5: c5 += 1
                elif p == 7: c7 += 1
        
        if temp > 1:
            return "-1"

        def min_digits_needed(c2, c3, c5, c7):
            """Returns the minimum number of single digits needed to cover the prime factors."""
            # Combine 2s and 3s into 8, 9, 6, 4
            d8 = c2 // 3
            rem2 = c2 % 3
            d9 = c3 // 2
            rem3 = c3 % 2

            if rem2 == 2 and rem3 == 1:
                # 2*2 = 4 and 3 -> 2 and 6 is 1 digit less or same, 2*2*3 = 12 (needs 8 & 3 or 4 & 6)
                # 2^2 * 3^1 = 12 -> 2 digits (e.g. 2, 6 or 3, 4 or 8 requires 1 two left)
                pass

            # Greedy combination for minimum length
            count = c5 + c7
            count += c2 // 3
            r2 = c2 % 3
            count += c3 // 2
            r3 = c3 % 2

            if r2 == 2 and r3 == 1: # 4 and 3 -> 2 and 6
                count += 2
            elif r2 == 1 and r3 == 1: # 2 and 3 -> 6
                count += 1
            else:
                count += (r2 > 0) + (r3 > 0)
            return count

        def get_min_suffix(len_avail, c2, c3, c5, c7):
            """Fills len_avail positions with the smallest digits (1-9) to satisfy prime requirements."""
            res = []
            for _ in range(len_avail):
                for d in range(1, 10):
                    # Check if placing digit d leaves enough space for remaining factors
                    nc2 = max(0, c2 - (3 if d in (8,) else 2 if d in (4,) else 1 if d in (2, 6) else 0))
                    nc3 = max(0, c3 - (2 if d in (9,) else 1 if d in (3, 6) else 0))
                    nc5 = max(0, c5 - (1 if d == 5 else 0))
                    nc7 = max(0, c7 - (1 if d == 7 else 0))
                    
                    if min_digits_needed(nc2, nc3, nc5, nc7) <= len_avail - 1 - len(res):
                        res.append(str(d))
                        c2, c3, c5, c7 = nc2, nc3, nc5, nc7
                        break
            return "".join(res)

        n = len(num)
        
        # Calculate factor requirements for prefixes
        # First, find if num itself has '0'
        first_zero = num.find('0')
        limit = first_zero if first_zero != -1 else n

        # Try to find a matching prefix of length `i`
        pref_c2, pref_c3, pref_c5, pref_c7 = c2, c3, c5, c7
        
        # Pre-calculate factors required along the prefix
        req = [(pref_c2, pref_c3, pref_c5, pref_c7)]
        for i in range(limit):
            d = int(num[i])
            pref_c2 = max(0, pref_c2 - (3 if d == 8 else 2 if d == 4 else 1 if d in (2, 6) else 0))
            pref_c3 = max(0, pref_c3 - (2 if d == 9 else 1 if d in (3, 6) else 0))
            pref_c5 = max(0, pref_c5 - (1 if d == 5 else 0))
            pref_c7 = max(0, pref_c7 - (1 if d == 7 else 0))
            req.append((pref_c2, pref_c3, pref_c5, pref_c7))

        # 1. Try same length: search from rightmost prefix branch
        for i in range(limit, -1, -1):
            rc2, rc3, rc5, rc7 = req[i]
            
            # If at length n and exact match valid without 0s
            if i == n and first_zero == -1:
                if rc2 == 0 and rc3 == 0 and rc5 == 0 and rc7 == 0:
                    return num
                continue
            
            start_d = int(num[i]) + 1 if i < n else 1
            if i == limit and first_zero != -1:
                # If we are at the first 0, we must pick digit >= 1
                start_d = max(1, int(num[i]) + 1)

            for d in range(start_d, 10):
                nc2 = max(0, rc2 - (3 if d == 8 else 2 if d == 4 else 1 if d in (2, 6) else 0))
                nc3 = max(0, rc3 - (2 if d == 9 else 1 if d in (3, 6) else 0))
                nc5 = max(0, rc5 - (1 if d == 5 else 0))
                nc7 = max(0, rc7 - (1 if d == 7 else 0))
                
                rem_len = n - 1 - i
                if min_digits_needed(nc2, nc3, nc5, nc7) <= rem_len:
                    prefix_str = num[:i] + str(d)
                    suffix_str = get_min_suffix(rem_len, nc2, nc3, nc5, nc7)
                    return prefix_str + suffix_str

        # 2. If no same-length solution exists, expand length
        target_len = max(n + 1, min_digits_needed(c2, c3, c5, c7))
        return get_min_suffix(target_len, c2, c3, c5, c7)