import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_len = n // 2
        
        # 1. Count character frequencies for the left half
        freq = [0] * 26
        for i in range(half_len):
            freq[ord(s[i]) - ord('a')] += 1

        INF = k + 1  # Cap total permutations at k + 1 to prevent overflow

        # Helper function to compute total unique permutations given current frequencies
        def count_permutations(f_list, sz):
            ans = 1
            curr_sz = sz
            for f in f_list:
                if f > 0:
                    ans *= math.comb(curr_sz, f)
                    if ans >= INF:
                        return INF
                    curr_sz -= f
            return ans

        # Check if there are at least k valid palindromic permutations
        total_perms = count_permutations(freq, half_len)
        if k > total_perms:
            return ""

        # 2. Build the left half character by character
        left = []
        rem_len = half_len

        for _ in range(half_len):
            for c in range(26):
                if freq[c] == 0:
                    continue

                # Try placing character c
                freq[c] -= 1
                cnt = count_permutations(freq, rem_len - 1)

                if cnt >= k:
                    # Fix character c
                    left.append(chr(ord('a') + c))
                    rem_len -= 1
                    break
                else:
                    # Skip cnt permutations and backtrack
                    k -= cnt
                    freq[c] += 1

        left_str = "".join(left)
        
        # 3. Reconstruct full palindrome
        middle = s[half_len] if n % 2 != 0 else ""
        return left_str + middle + left_str[::-1]