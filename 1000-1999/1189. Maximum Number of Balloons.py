from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count frequencies of all characters in the text
        counts = Counter(text)
        
        # Calculate the maximum number of single "balloon" words we can form
        return min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] // 2,
            counts['n']
        )