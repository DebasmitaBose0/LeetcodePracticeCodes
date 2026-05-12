class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Map to store {remainder: first_index_seen}
        # Initialize with 0: -1 to handle subarrays starting from index 0
        remainder_map = {0: -1}
        current_sum = 0
        
        for i, n in enumerate(nums):
            current_sum += n
            remainder = current_sum % k
            
            if remainder in remainder_map:
                # If the same remainder was seen more than 1 index ago
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Only store the first occurrence of a remainder
                remainder_map[remainder] = i
                
        return False