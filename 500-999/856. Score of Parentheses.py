class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # If v is 0, it means we closed an empty "()", so score is 1.
                # Otherwise, it means we closed a nested "(A)", so score is 2 * v.
                score = 1 if v == 0 else 2 * v
                stack[-1] += score
                
        return stack[0]