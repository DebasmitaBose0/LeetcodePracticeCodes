class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Helper function to get the next index in a circular fashion
        def get_next(curr_idx):
            # (current + steps) % length handles circularity in both directions
            return (curr_idx + nums[curr_idx]) % n

        for i in range(n):
            if nums[i] == 0:
                continue
            
            slow = i
            fast = i
            
            # Standard Floyd's Cycle-finding: slow moves 1 step, fast moves 2
            # We also check that the direction (sign) remains the same
            while nums[get_next(fast)] * nums[i] > 0 and \
                  nums[get_next(get_next(fast))] * nums[i] > 0:
                
                slow = get_next(slow)
                fast = get_next(get_next(fast))
                
                if slow == fast:
                    # Check if the cycle length is greater than 1
                    if slow == get_next(slow):
                        break
                    return True
            
            # Optimization: Mark all nodes in this failed path as 0
            curr = i
            sign = nums[i]
            while nums[curr] * sign > 0:
                next_node = get_next(curr)
                nums[curr] = 0
                curr = next_node
                
        return False