class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = [0] * 26   # for lowercase English letters
        
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        for ch in t:
            count[ord(ch) - ord('a')] -= 1
        
        return all(c == 0 for c in count)