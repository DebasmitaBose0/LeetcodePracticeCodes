class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []
        for i, char in enumerate(seq):
            if char == '(':
                # Alternate assignment based on the index parity 
                # to distribute nesting depths evenly between A (0) and B (1)
                answer.append(i % 2)
            else:
                answer.append((i + 1) % 2)
        return answer