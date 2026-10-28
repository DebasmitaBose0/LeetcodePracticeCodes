class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(index, prev_operand, current_val, expression):
            # Base case: reached the end of the string
            if index == len(num):
                if current_val == target:
                    res.append("".join(expression))
                return

            for i in range(index, len(num)):
                # Handle leading zero: numbers like "05" are invalid
                if i > index and num[index] == '0':
                    break
                
                # Get the current substring and its integer value
                sub_str = num[index : i + 1]
                val = int(sub_str)
                
                if index == 0:
                    # First number in the expression, no operator needed
                    backtrack(i + 1, val, val, [sub_str])
                else:
                    # Try Addition
                    backtrack(i + 1, val, current_val + val, expression + ["+", sub_str])
                    
                    # Try Subtraction
                    backtrack(i + 1, -val, current_val - val, expression + ["-", sub_str])
                    
                    # Try Multiplication (Handle precedence)
                    backtrack(i + 1, prev_operand * val, (current_val - prev_operand) + (prev_operand * val), expression + ["*", sub_str])

        backtrack(0, 0, 0, [])
        return res