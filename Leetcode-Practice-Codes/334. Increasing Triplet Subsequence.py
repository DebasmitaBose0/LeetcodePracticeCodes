class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize the first and second smallest values to infinity
        first = second = float('inf')
        
        for n in nums:
            if n <= first:
                # Update first if n is smaller than or equal to current first
                first = n
            elif n <= second:
                # Update second if n is larger than first but smaller than second
                second = n
            else:
                # If we find n > second, we have first < second < n
                return True
                
        return False