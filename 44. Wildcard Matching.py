class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star = -1
        match = 0

        while i < len(s):
            # Case 1: match or '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Case 2: '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Case 3: mismatch but previous '*'
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # Case 4: mismatch, no '*'
            else:
                return False

        # Remaining pattern should be all '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)