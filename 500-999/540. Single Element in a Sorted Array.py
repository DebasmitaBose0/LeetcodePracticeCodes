class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            # Check if mid is even or odd to pair it correctly
            # We want to compare nums[mid] with its partner.
            # If mid is even, partner should be mid + 1.
            # If mid is odd, partner should be mid - 1.
            # A clever trick is mid ^ 1 which gives the 'partner' index.
            if nums[mid] == nums[mid ^ 1]:
                # We are in the left half, single element is further right
                low = mid + 1
            else:
                # We are in the right half (or at the single element)
                high = mid
        
        return nums[low]