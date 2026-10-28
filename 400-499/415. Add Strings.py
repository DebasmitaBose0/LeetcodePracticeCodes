class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        
        # Continue as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            # Get digit value or 0 if pointer is out of bounds
            val1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            val2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            # Calculate sum and new carry
            column_sum = val1 + val2 + carry
            carry = column_sum // 10
            res.append(str(column_sum % 10))
            
            # Move pointers to the left
            i -= 1
            j -= 1
            
        # Join the list and reverse to get the final string
        return "".join(res[::-1])