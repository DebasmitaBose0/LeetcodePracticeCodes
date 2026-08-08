class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # last_pos[j] stores the largest starting index in word1 
        # where suffix word2[j:] can be matched as a subsequence.
        last_pos = [-1] * (m + 1)
        last_pos[m] = n

        ptr = n - 1
        for j in range(m - 1, -1, -1):
            while ptr >= 0 and word1[ptr] != word2[j]:
                ptr -= 1
            last_pos[j] = ptr
            if ptr >= 0:
                ptr -= 1

        res = []
        changed = False
        j = 0

        for i in range(n):
            if j == m:
                break

            # If characters match
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            # If characters mismatch, try using the 1 allowed change
            elif not changed and last_pos[j + 1] > i:
                res.append(i)
                changed = True
                j += 1

        return res if len(res) == m else []