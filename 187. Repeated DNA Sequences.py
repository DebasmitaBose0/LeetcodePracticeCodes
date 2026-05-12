from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        seen = set()        # store sequences we've seen
        repeated = set()    # store sequences that appear more than once
        for i in range(len(s) - 9):
            seq = s[i:i+10]  # 10-letter substring
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)
        
        return list(repeated)