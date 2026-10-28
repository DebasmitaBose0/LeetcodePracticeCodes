class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Target found
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[low] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Shrink right
                else:
                    low = mid + 1   # Search right half
                    
            # Otherwise, the right half must be sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Shrink left
                else:
                    high = mid - 1  # Search left half
                    
        return -1
    