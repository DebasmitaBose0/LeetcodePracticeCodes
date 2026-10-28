class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        
        # Step 1: Insert all possible prefixes of numbers in arr1 into the set
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10  # Strip the last digit to get the next prefix
                
        max_length = 0
        
        # Step 2: Check all possible prefixes of numbers in arr2 against the set
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    # If found, check its length and update the maximum
                    max_length = max(max_length, len(str(num)))
                    break  # Optimization: shorter prefixes of the same number won't beat max_length
                num //= 10
                
        return max_length