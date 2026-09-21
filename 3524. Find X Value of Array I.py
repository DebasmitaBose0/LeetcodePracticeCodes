class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        # dp[r] stores the count of subarrays ending at the previous step with product remainder r modulo k
        prev_dp = [0] * k
        
        for num in nums:
            curr_dp = [0] * k
            rem = num % k
            
            # Every previous remainder can be extended with the current number
            for r in range(k):
                if prev_dp[r] > 0:
                    new_rem = (r * rem) % k
                    curr_dp[new_rem] += prev_dp[r]
            
            # The current number itself starts a new subarray
            curr_dp[rem] += 1
            
            # Add current step's valid subarray counts to the global result
            for r in range(k):
                result[r] += curr_dp[r]
                
            prev_dp = curr_dp
            
        return result