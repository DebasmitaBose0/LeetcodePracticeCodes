class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_max = [0] * n
        suf_min = [0] * n
        
        # Calculate prefix maximums
        curr_max = 0
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            pre_max[i] = curr_max
            
        # Calculate suffix minimums
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suf_min[i] = curr_min
            
        ans = [0] * n
        i = 0
        while i < n:
            j = i
            # Find the end of the current connected component
            # A component ends when the max of the left doesn't exceed the min of the right
            while j + 1 < n and pre_max[j] > suf_min[j+1]:
                j += 1
            
            # The maximum value in this connected range
            component_max = pre_max[j]
            
            # All indices in this range can reach the component's maximum
            for k in range(i, j + 1):
                ans[k] = component_max
            
            i = j + 1
            
        return ans