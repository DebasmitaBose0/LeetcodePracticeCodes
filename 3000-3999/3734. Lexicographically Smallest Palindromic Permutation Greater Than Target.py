from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        
        # Check if a palindromic permutation is possible
        odd_chars = [char for char, freq in count.items() if freq % 2 != 0]
        if len(odd_chars) > (1 if n % 2 != 0 else 0):
            return ""
            
        mid_char = ""
        if n % 2 != 0:
            if odd_chars:
                mid_char = odd_chars[0]
                count[mid_char] -= 1
            else:
                # Find any char to put in middle if needed, though odd_chars covers it
                pass
                
        half_len = n // 2
        available = []
        for char in sorted(count.keys()):
            available.extend([char] * (count[char] // 2))
            
        target_half = target[:half_len]
        
        # Backtracking to find the lexicographically smallest first half > target_half (or matching and checking mid/second half)
        res = []
        found = False
        
        used = [False] * len(available)
        
        def dfs(idx, current_half, is_greater):
            nonlocal found
            if found:
                return
            if idx == half_len:
                # Construct full candidate
                candidate = "".join(current_half) + (mid_char if n % 2 != 0 else "") + "".join(reversed(current_half))
                if candidate > target:
                    res.append(candidate)
                    found = True
                return
                
            # Try choices
            seen = set()
            for i in range(len(available)):
                if used[i] or available[i] in seen:
                    continue
                char = available[i]
                
                # Pruning based on target prefix
                if not is_greater and char < target_half[idx]:
                    continue
                
                seen.add(char)
                used[i] = True
                current_half.append(char)
                
                next_is_greater = is_greater or (char > target_half[idx])
                dfs(idx + 1, current_half, next_is_greater)
                
                current_half.pop()
                used[i] = False
                if found:
                    return

        dfs(0, [], False)
        
        return res[0] if res else ""