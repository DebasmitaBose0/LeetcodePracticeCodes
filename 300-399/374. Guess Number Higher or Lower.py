# The method must be named 'guessNumber' (camelCase)
class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            mid = low + (high - low) // 2
            # guess(mid) is a pre-defined API provided by LeetCode
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1