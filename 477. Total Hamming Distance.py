class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)
        
        # Iterate through each of the 31 bit positions
        for i in range(31):
            # Count how many numbers have the i-th bit set to 1
            count_ones = 0
            for num in nums:
                # Check if the i-th bit is 1
                if (num >> i) & 1:
                    count_ones += 1
            
            # Count how many numbers have the i-th bit set to 0
            count_zeros = n - count_ones
            
            # Each pair of (1, 0) contributes 1 to the total Hamming distance
            total_distance += count_ones * count_zeros
            
        return total_distance