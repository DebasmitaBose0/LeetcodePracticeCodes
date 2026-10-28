from ast import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []
        
        # Partition elements into three separate lists
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        
        # Combine the lists to maintain the required relative order
        return less + equal + greater