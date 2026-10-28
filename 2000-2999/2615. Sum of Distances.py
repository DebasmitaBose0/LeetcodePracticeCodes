class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        # Prefix Pass (Left to Right)
        count = {} # val -> count seen so far
        sum_idx = {} # val -> sum of indices seen so far
        
        for i, x in enumerate(nums):
            if x in count:
                res[i] += count[x] * i - sum_idx[x]
                count[x] += 1
                sum_idx[x] += i
            else:
                count[x] = 1
                sum_idx[x] = i
                
        # Suffix Pass (Right to Left)
        count = {}
        sum_idx = {}
        
        for i in range(n - 1, -1, -1):
            x = nums[i]
            if x in count:
                res[i] += sum_idx[x] - count[x] * i
                count[x] += 1
                sum_idx[x] += i
            else:
                count[x] = 1
                sum_idx[x] = i
                
        return res