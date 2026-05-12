from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        res = []
        
        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]
            
            freq = Counter(window)
            
            # Sort by (frequency desc, value desc)
            sorted_items = sorted(freq.items(), key=lambda t: (-t[1], -t[0]))
            
            total = 0
            count = 0
            
            for num, f in sorted_items:
                if count == x:
                    break
                total += num * f
                count += 1
            
            res.append(total)
        
        return res