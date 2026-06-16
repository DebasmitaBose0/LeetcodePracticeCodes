class Solution:
    def processStr(self, s: str) -> str:
        result = []
        
        for char in s:
            if char == '*':
                # Removes the last character if it exists
                if result:
                    result.pop()
            elif char == '#':
                # Duplicates the current result and appends it to itself
                result = result + result
            elif char == '%':
                # Reverses the current result
                result.reverse()
            else:
                # Append lowercase English letters
                result.append(char)
                
        return "".join(result)