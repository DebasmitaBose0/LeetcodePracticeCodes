from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # 1. Count the frequency of each character
        counts = Counter(s)
        
        # 2. Sort characters by frequency in descending order
        # counts.items() returns (char, freq) pairs
        sorted_chars = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        
        # 3. Build the resulting string
        res = []
        for char, freq in sorted_chars:
            res.append(char * freq)
            
        return "".join(res)