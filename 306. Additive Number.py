class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        # Try all possible lengths for the first two numbers
        # i is the end index of the first number, j is the end index of the second
        for i in range(1, n):
            for j in range(i + 1, n):
                s1 = num[:i]
                s2 = num[i:j]
                
                # Leading zeros check: numbers > 0 cannot start with '0'
                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                    continue
                
                if self.isValid(s1, s2, j, num):
                    return True
        return False

    def isValid(self, s1: str, s2: str, start: int, num: str) -> bool:
        # If we reached the end of the string, it's a valid sequence
        if start == len(num):
            return True
        
        # Calculate what the next number should be
        sum_str = str(int(s1) + int(s2))
        
        # Check if the remaining string starts with this sum
        if not num.startswith(sum_str, start):
            return False
        
        # Move forward: the old s2 becomes the new s1, and sum_str becomes the new s2
        return self.isValid(s2, sum_str, start + len(sum_str), num)