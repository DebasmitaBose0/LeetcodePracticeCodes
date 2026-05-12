class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = {}
        count = 0
        
        # 1. Store all sums of nums1 and nums2 in the hash map
        for a in nums1:
            for b in nums2:
                current_sum = a + b
                sum_map[current_sum] = sum_map.get(current_sum, 0) + 1
        
        # 2. Check if the negative of sums of nums3 and nums4 exists in the map
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_map:
                    count += sum_map[target]
                    
        return count