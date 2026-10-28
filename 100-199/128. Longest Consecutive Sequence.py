class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:  # start of sequence
                length = 1
                current = num

                while current + 1 in numSet:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest