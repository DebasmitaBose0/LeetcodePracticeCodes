class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, 1):
            # 'a' has position 26 in reversed alphabet ('z'=1, 'y'=2, ..., 'a'=26)
            rev_alphabet_pos = 26 - (ord(char) - ord('a'))
            total += rev_alphabet_pos * i
        return total