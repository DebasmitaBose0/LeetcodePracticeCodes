import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_categories = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid_coupons = []
        
        # Regex to check if code is non-empty and contains only [a-zA-Z0-9_]
        pattern = re.compile(r'^[a-zA-Z0-9_]+$')
        
        for i in range(len(code)):
            # Condition 1: Active check
            if not isActive[i]:
                continue
                
            # Condition 2: Business line check
            if businessLine[i] not in valid_categories:
                continue
            
            # Condition 3: Code validity check (non-empty and alphanumeric/underscore)
            if not pattern.match(code[i]):
                continue
            
            # If all passed, store for sorting
            valid_coupons.append((businessLine[i], code[i]))
            
        # Sort by category priority first, then by code lexicographically
        valid_coupons.sort(key=lambda x: (valid_categories[x[0]], x[1]))
        
        # Return only the codes
        return [c[1] for c in valid_coupons]