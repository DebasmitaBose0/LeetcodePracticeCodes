from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each letter
        freqs = Counter(word).values()
        
        # Sort frequencies in descending order
        sorted_freqs = sorted(freqs, reverse=True)
        
        total_pushes = 0
        
        # Calculate total pushes needed based on rank
        for i, count in enumerate(sorted_freqs):
            pushes = (i // 8) + 1
            total_pushes += count * pushes
            
        return total_pushes