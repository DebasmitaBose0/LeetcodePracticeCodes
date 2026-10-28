class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        
        for fast in range(len(nums)):
            # If the current element is non-zero
            if nums[fast] != 0:
                # Swap elements at slow and fast pointers
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # Move the slow pointer forward
                slow += 1