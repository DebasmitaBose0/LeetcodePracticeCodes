class Solution:
    def grayCode(self, n: int):
        result = []
        
        for i in range(1 << n):   # 2^n numbers
            result.append(i ^ (i >> 1))
        
        return result