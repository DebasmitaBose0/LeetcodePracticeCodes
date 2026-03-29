class Solution:
    def isNumber(self, s: str) -> bool:
        num = False
        dot = False
        exp = False
        
        for i, ch in enumerate(s):
            
            if ch.isdigit():
                num = True
            
            elif ch in ['+', '-']:
                # only valid at start or after e/E
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            
            elif ch == '.':
                # only one dot and not after exponent
                if dot or exp:
                    return False
                dot = True
            
            elif ch in ['e', 'E']:
                # must have number before and only one exponent
                if exp or not num:
                    return False
                exp = True
                num = False  # need number after e
            
            else:
                return False
        
        return num