from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        
        # To quickly find the smallest available character >= a given char
        def find_greater_or_equal(start_char, available):
            for ch in range(ord(start_char), ord('z') + 1):
                c = chr(ch)
                if available[c] > 0:
                    return c
            return None

        def find_strictly_greater(start_char, available):
            for ch in range(ord(start_char) + 1, ord('z') + 1):
                c = chr(ch)
                if available[c] > 0:
                    return c
            return None

        # Try to build prefix matching target as much as possible
        res = []
        # We'll track state to allow backtracking
        # Let's use an iterative or backtracking helper
        
        # Alternatively, a constructive greedy approach from left to right:
        # We can try to match prefix of target.
        matched_prefix = []
        temp_count = count.copy()
        
        i = 0
        while i < n:
            ch = target[i]
            # Can we match target[i]?
            if temp_count[ch] > 0:
                temp_count[ch] -= 1
                matched_prefix.append(ch)
                i += 1
            else:
                break
        
        # If we successfully matched the whole target prefix up to some point:
        # We need to make the string strictly greater.
        # If we matched all n characters identically to target, we need to backtrack and increase the last choice.
        
        def solve(idx, current_count):
            if idx == n:
                return "".join(res_path)
            
            # Try to match target[idx] or something larger
            # Actually, standard backtracking from left to right:
            pass

        # Let's write a clean backtracking builder from left to right
        res_path = []
        
        def backtrack(index, is_greater):
            if index == n:
                return "" if not is_greater else "".join(res_path)
            
            target_char = target[index]
            
            # If we are already strictly greater, we want the smallest possible remaining characters
            if is_greater:
                for ch in range(ord('a'), ord('z') + 1):
                    c = chr(ch)
                    if count[c] > 0:
                        count[c] -= 1
                        res_path.append(c)
                        ans = backtrack(index + 1, True)
                        if ans:
                            return ans
                        res_path.pop()
                        count[c] += 1
                return ""
            else:
                # We need to match target[index] or pick something strictly greater
                # Option 1: Try matching target_char if available
                if count[target_char] > 0:
                    count[target_char] -= 1
                    res_path.append(target_char)
                    ans = backtrack(index + 1, False)
                    if ans:
                        return ans
                    res_path.pop()
                    count[target_char] += 1
                
                # Option 2: Try picking the smallest character strictly greater than target_char
                for ch in range(ord(target_char) + 1, ord('z') + 1):
                    c = chr(ch)
                    if count[c] > 0:
                        count[c] -= 1
                        res_path.append(c)
                        ans = backtrack(index + 1, True)
                        if ans:
                            return ans
                        res_path.pop()
                        count[c] += 1
                
                return ""

        return backtrack(0, False)