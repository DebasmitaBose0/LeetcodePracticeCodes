class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_idx = {word: i for i, word in enumerate(words)}
        res = []
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # Case 1: If prefix is a palindrome, look for reversed suffix at the BEGINNING
                if prefix == prefix[::-1]:
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_to_idx and word_to_idx[rev_suffix] != i:
                        res.append([word_to_idx[rev_suffix], i])
                
                # Case 2: If suffix is a palindrome, look for reversed prefix at the END
                # Adding 'j != len(word)' prevents double-counting perfect reverses
                if j != len(word) and suffix == suffix[::-1]:
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_to_idx and word_to_idx[rev_prefix] != i:
                        res.append([i, word_to_idx[rev_prefix]])
                        
        return res