class Solution:
    def nthSmallest(self, n, k):
        def count_bits(x):
            return bin(x).count('1')
        
        res = []
        num = 1
        
        while len(res) < n:
            if count_bits(num) == k:
                res.append(num)
            num += 1
        
        return res[-1]