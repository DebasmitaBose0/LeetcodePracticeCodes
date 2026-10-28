class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0  # Pointer for nums1
        j = 0  # Pointer for nums2
        max_dist = 0
        
        while i < len(nums1) and j < len(nums2):
            # If the condition is met, calculate distance and move j
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                # If nums1[i] is too large, move i forward
                i += 1
                # Standard two-pointer optimization: 
                # j must be at least i to satisfy i <= j
                if i > j:
                    j = i
                    
        return max_dist