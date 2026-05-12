from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count frequencies in the first array
        counts = Counter(nums1)
        res = []
        
        # Iterate through the second array
        for num in nums2:
            # If the number exists in the map and has a remaining count
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
                
        return res