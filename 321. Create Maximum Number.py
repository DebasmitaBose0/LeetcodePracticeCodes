class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        res = []

        # i is the number of elements taken from nums1
        # We must ensure we don't take more than available, 
        # and that nums2 has enough elements to fill the rest of k.
        for i in range(max(0, k - n), min(k, m) + 1):
            # 1. Get max subsequences of lengths i and k-i
            seq1 = self.getMaxSubsequence(nums1, i)
            seq2 = self.getMaxSubsequence(nums2, k - i)
            
            # 2. Merge them and 3. keep the best one
            current_max = self.merge(seq1, seq2)
            if current_max > res:
                res = current_max
        return res

    def getMaxSubsequence(self, nums, length):
        stack = []
        drop = len(nums) - length
        for num in nums:
            while drop > 0 and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:length]

    def merge(self, s1, s2):
        # In Python, list comparison [s1:] > [s2:] handles 
        # the tie-breaking logic automatically.
        return [max(s1, s2).pop(0) for _ in range(len(s1) + len(s2))]