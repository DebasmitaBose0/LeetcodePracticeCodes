import itertools

class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        # Step 1: Generate prefix sums
        # prefix[i] is the sum of nums[0...i-1]
        prefix = list(itertools.accumulate(nums, initial=0))
        
        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return 0
            
            mid = (lo + hi) // 2
            # Recursively count in left and right halves
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            
            # Step 2: Count valid pairs across the split (left half i, right half j)
            # Both prefix[lo:mid] and prefix[mid:hi] are sorted at this point
            i = j = mid
            for left_val in prefix[lo:mid]:
                # Find the first j such that prefix[j] - left_val >= lower
                while i < hi and prefix[i] - left_val < lower:
                    i += 1
                # Find the first j such that prefix[j] - left_val > upper
                while j < hi and prefix[j] - left_val <= upper:
                    j += 1
                count += j - i
            
            # Step 3: Standard merge step to keep the array sorted
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return merge_sort(0, len(prefix))