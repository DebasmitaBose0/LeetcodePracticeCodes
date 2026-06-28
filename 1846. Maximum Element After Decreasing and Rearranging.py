class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Step 1: Sort the array to allow a steady, greedy increase
        arr.sort()
        
        # Step 2: The first element must always be 1
        arr[0] = 1
        
        # Step 3: Iterate through the array and ensure the condition holds
        for i in range(1, len(arr)):
            # The current element can at most be 1 greater than the previous element
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
                
        # The last element will represent the maximum possible value achieved
        return arr[-1]