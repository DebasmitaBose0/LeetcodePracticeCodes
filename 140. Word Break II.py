class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            res = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    subsentences = dfs(end)

                    for sub in subsentences:
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sub)

            memo[start] = res
            return res

        return dfs(0)