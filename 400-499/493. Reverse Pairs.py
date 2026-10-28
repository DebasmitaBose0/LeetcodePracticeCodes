class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, left, right):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = self.mergeSort(nums, left, mid) + self.mergeSort(nums, mid + 1, right)
        
        # Count reverse pairs: nums[i] > 2 * nums[j]
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))
        
        # Standard merge step to keep the array sorted
        nums[left:right + 1] = sorted(nums[left:right + 1])
        return count