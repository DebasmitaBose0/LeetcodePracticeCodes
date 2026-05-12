class Solution:
    def rotateElements(self, nums, k):
        # Step 1: extract non-negative elements
        arr = [x for x in nums if x >= 0]
        
        if not arr:
            return nums
        
        # Step 2: rotate left
        k %= len(arr)
        arr = arr[k:] + arr[:k]
        
        # Step 3: place back
        j = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = arr[j]
                j += 1
        
        return nums