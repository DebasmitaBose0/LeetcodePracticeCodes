class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. Split the string into words based on spaces
        # 2. For each word, reverse it using slicing [::-1]
        # 3. Join the list of reversed words back into a single string
        return " ".join(word[::-1] for word in s.split(' '))