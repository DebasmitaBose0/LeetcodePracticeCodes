class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        memo = {}

        def can_form(word):
            if word in memo:
                return memo[word]
            
            # Try splitting the word at every possible index
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                # If prefix is in the set AND (suffix is in set OR suffix can be formed)
                if prefix in word_set:
                    if suffix in word_set or can_form(suffix):
                        memo[word] = True
                        return True
            
            memo[word] = False
            return False

        res = []
        for word in words:
            if not word: continue
            if can_form(word):
                res.append(word)
        return res