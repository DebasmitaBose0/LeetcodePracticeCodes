class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Step 1: Remove dashes and uppercase the string
        clean_s = s.replace("-", "").upper()
        
        # Step 2: Use a list to collect characters (more efficient than string concatenation)
        result = []
        count = 0
        
        # Step 3: Iterate backwards through the cleaned string
        for i in range(len(clean_s) - 1, -1, -1):
            result.append(clean_s[i])
            count += 1
            
            # If we've reached k characters and aren't at the very start of the string, 
            # add a dash
            if count == k and i != 0:
                result.append("-")
                count = 0
        
        # Step 4: Reverse back and join to form the final string
        return "".join(result[::-1])