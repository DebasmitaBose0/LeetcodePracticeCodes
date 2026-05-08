class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Map to store the next greater element for each number in nums2
        next_greater = {}
        stack = []

        # Traverse nums2 to find the next greater element for every number
        for num in nums2:
            # While the stack is not empty and current num is greater than the top
            while stack and num > stack[-1]:
                # We found the next greater element for stack.pop()
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            
            # Push current number onto the stack
            stack.append(num)
        
        # For any elements left in the stack, there is no next greater element
        # (Though we can just use .get(x, -1) during lookup)
        
        # Build the result for nums1 using the map
        return [next_greater.get(val, -1) for val in nums1]