class Solution:
    def searchRange(self, nums, target):
        
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            ans = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    ans = mid
                    right = mid - 1  # go left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return ans
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            ans = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1  # go right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return ans
        
        return [findFirst(nums, target), findLast(nums, target)]