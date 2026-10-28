# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            # Find the midpoint
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # If mid is bad, the first bad version is mid or to the left
                right = mid
            else:
                # If mid is good, the first bad version must be to the right
                left = mid + 1
        
        # When left == right, we've found the first bad version
        return left