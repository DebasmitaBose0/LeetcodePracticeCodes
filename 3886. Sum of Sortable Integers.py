class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        total_sum = 0
        
        for k in divisors:
            is_sortable = True
            for i in range(0, n, k):
                # Extract blocks of length k
                original_block = tuple(nums[i:i+k])
                sorted_block = tuple(sorted_nums[i:i+k])
                
                # Check if sorted_block is a cyclic rotation of original_block
                double_block = original_block + original_block
                found = False
                for j in range(k):
                    if double_block[j:j+k] == sorted_block:
                        found = True
                        break
                
                if not found:
                    is_sortable = False
                    break
                    
            if is_sortable:
                total_sum += k
                
        return total_sum