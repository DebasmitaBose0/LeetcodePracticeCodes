from ast import List
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # Count how many patterns are a substring of the given word
        return sum(1 for p in patterns if p in word)