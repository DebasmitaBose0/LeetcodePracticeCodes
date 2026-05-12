class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            # Use the absolute value as an index
            index = abs(num) - 1
            
            # If the value at this index is negative, we've seen 'abs(num)' before
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                # Mark it as seen by flipping the sign
                nums[index] = -nums[index]
                
        return duplicates