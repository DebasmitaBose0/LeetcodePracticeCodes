class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # While we have removals left and the current digit is 
            # smaller than the last one we kept, remove the last one.
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If we still have removals left (e.g., num was "123"), 
        # chop them off from the end.
        final_stack = stack[:-k] if k > 0 else stack
        
        # Convert to string and strip leading zeros (e.g., "0200" -> "200")
        res = "".join(final_stack).lstrip('0')
        
        # If the result is empty, return "0"
        return res if res else "0"