from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def isBalanced(x):
            count = Counter(str(x))
            
            for digit, freq in count.items():
                if int(digit) != freq:
                    return False
            return True
        
        num = n + 1
        while True:
            if isBalanced(num):
                return num
            num += 1