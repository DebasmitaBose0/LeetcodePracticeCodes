class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the number (handles multi-digit numbers like "100")
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current string and number onto the stack
                # and reset them for the content inside the brackets
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == ']':
                # Pop the previous string and the multiplier
                last_str, num = stack.pop()
                # Multiply the current content and append to the previous string
                current_str = last_str + (num * current_str)
            else:
                # If it's a regular character, just add to current string
                current_str += char
                
        return current_str