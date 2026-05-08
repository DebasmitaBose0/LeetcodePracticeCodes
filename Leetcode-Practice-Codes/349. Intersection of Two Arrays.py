class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both to sets to handle uniqueness automatically
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Use the set intersection operator
        return list(set1 & set2)