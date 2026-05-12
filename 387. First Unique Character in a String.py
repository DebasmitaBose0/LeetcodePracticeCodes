from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 1. Build a frequency map of all characters in the string
        # This takes O(n) time
        count = Counter(s)
        
        # 2. Iterate through the string a second time in order
        # This ensures we find the FIRST unique character
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        # 3. If no unique character is found, return -1
        return -1