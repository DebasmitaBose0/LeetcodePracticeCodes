class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n <= 0:
            return False
            
        # Count the frequency of each number
        counts = Counter(nums)
        
        # Check numbers 1 to n-1
        for i in range(1, n):
            if counts[i] != 1:
                return False
                
        # Check number n
        return counts[n] == 2