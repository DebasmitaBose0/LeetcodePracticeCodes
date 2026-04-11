class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        
        for n in nums:
            # 1. Skip if we've already seen this distinct number
            if n in (first, second, third):
                continue
            
            # 2. Update first and shift others down
            if first is None or n > first:
                first, second, third = n, first, second
            # 3. Update second and shift third down
            elif second is None or n > second:
                second, third = n, second
            # 4. Update third
            elif third is None or n > third:
                third = n
        
        # 5. If third max doesn't exist, return first max
        return third if third is not None else first