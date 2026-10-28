from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        
        # Step 1: Count frequency of each number
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        # Step 2: Count how many numbers are divisible by each i
        gcd_count = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            count_divisible = 0
            for j in range(i, max_val + 1, i):
                count_divisible += freq[j]
            gcd_count[i] = (count_divisible * (count_divisible - 1)) // 2
            
        # Step 3: Inclusion-Exclusion to find exact pairs with GCD == i
        for i in range(max_val, 0, -1):
            for j in range(2 * i, max_val + 1, i):
                gcd_count[i] -= gcd_count[j]
                
        # Step 4: Compute prefix sums of the exact GCD counts
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_count[i]
            
        # Step 5: Answer each query using binary search
        answer = []
        for q in queries:
            idx = bisect_right(prefix_sums, q)
            answer.append(idx)
            
        return answer