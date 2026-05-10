class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 0
        
        for i in range(len(nums)):
            # If the number is -1, we've already processed this cycle
            if nums[i] == -1:
                continue
            
            current_length = 0
            curr = i
            
            # Traverse the cycle
            while nums[curr] != -1:
                next_node = nums[curr]
                nums[curr] = -1  # Mark current element as visited
                curr = next_node
                current_length += 1
            
            max_length = max(max_length, current_length)
            
        return max_length