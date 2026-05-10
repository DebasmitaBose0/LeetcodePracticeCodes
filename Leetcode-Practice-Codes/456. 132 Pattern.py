class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # s3 represents the '2' in the '132' pattern
        # It is the largest value found so far that has a larger value to its left
        s3 = float('-inf')
        stack = [] # This will store potential '3' values (nums[j])
        
        # Iterate from right to left
        for i in range(len(nums) - 1, -1, -1):
            # If we find a number smaller than s3, the 132 pattern is complete
            if nums[i] < s3:
                return True
            
            # If the current number is larger than the top of the stack,
            # it could be a '3'. The popped value becomes our new '2' (s3).
            while stack and nums[i] > stack[-1]:
                s3 = stack.pop()
            
            # Push the current number as a potential '3'
            stack.append(nums[i])
            
        return False