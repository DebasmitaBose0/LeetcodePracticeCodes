class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the result array with -1
        res = [-1] * n
        stack = [] # Stores indices of elements
        
        # Iterate twice to simulate circular behavior
        for i in range(2 * n):
            num = nums[i % n]
            
            # While stack is not empty and current num is greater than 
            # the element represented by the index at the top of the stack
            while stack and nums[stack[-1]] < num:
                idx = stack.pop()
                res[idx] = num
            
            # Only push indices from the first pass to avoid redundant work
            if i < n:
                stack.append(i)
                
        return res