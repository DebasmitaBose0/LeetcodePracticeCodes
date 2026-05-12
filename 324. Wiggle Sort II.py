class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Sort the array
        arr = sorted(nums)
        n = len(nums)
        
        # 2. Find the midpoint
        # We use (n + 1) // 2 so the left half is slightly larger for odd lengths
        mid = (n + 1) // 2
        
        # 3. Partition into two halves
        left = arr[:mid]
        right = arr[mid:]
        
        # 4. Interleave from the back to handle duplicates safely
        # Odd indices get the larger numbers (right half)
        # Even indices get the smaller numbers (left half)
        for i in range(n):
            if i % 2 == 0:
                nums[i] = left.pop()
            else:
                nums[i] = right.pop()