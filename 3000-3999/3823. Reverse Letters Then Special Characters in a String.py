class Solution:
    def reverseByType(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        specials = [ch for ch in s if not ch.isalpha()]
        
        letters.reverse()
        specials.reverse()
        
        res = []
        i = j = 0
        
        for ch in s:
            if ch.isalpha():
                res.append(letters[i])
                i += 1
            else:
                res.append(specials[j])
                j += 1
        
        return "".join(res)