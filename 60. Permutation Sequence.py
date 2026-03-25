class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        
        nums = list(range(1, n + 1))
        k -= 1  # convert to 0-based index
        
        result = ""
        
        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            
            result += str(nums[index])
            nums.pop(index)
            
            k %= fact
        
        return result