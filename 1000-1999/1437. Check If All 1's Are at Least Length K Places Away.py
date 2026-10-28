class Solution:
    def kLengthApart(self, nums, k):
        last = -1  # last position of 1
        
        for i in range(len(nums)):
            if nums[i] == 1:
                if last != -1 and i - last - 1 < k:
                    return False
                last = i
        
        return True