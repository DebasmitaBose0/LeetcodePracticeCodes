class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(curr, open_count, close_count):
            # Base case: when the current string reaches a length of 2 * n
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return
            
            # We can add an opening parenthesis if we haven't used all n of them
            if open_count < n:
                curr.append("(")
                backtrack(curr, open_count + 1, close_count)
                curr.pop()
                
            # We can add a closing parenthesis if there are unclosed opening parentheses
            if close_count < open_count:
                curr.append(")")
                backtrack(curr, open_count, close_count + 1)
                curr.pop()
                
        backtrack([], 0, 0)
        return res