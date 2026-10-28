from collections import Counter

class Solution:
    def countPairs(self, words):
        def normalize(word):
            return tuple((ord(c) - ord(word[0])) % 26 for c in word)
        
        count = Counter(normalize(w) for w in words)
        
        return sum(v * (v - 1) // 2 for v in count.values())