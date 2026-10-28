class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge list to a dictionary for O(1) lookups
        k_map = {k: v for k, v in knowledge}
        
        res = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # Find the closing bracket
                j = i + 1
                while j < n and s[j] != ')':
                    j += 1
                
                # Extract the key between '(' and ')'
                key = s[i+1:j]
                
                # Append corresponding value or '?'
                res.append(k_map.get(key, '?'))
                
                # Move index past the closing bracket
                i = j + 1
            else:
                res.append(s[i])
                i += 1
                
        return "".join(res)