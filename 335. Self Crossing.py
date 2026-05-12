class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        d = distance
        n = len(d)
        if n <= 3:
            return False
            
        for i in range(3, n):
            # Case 1: Fourth line crosses first line
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True
            
            # Case 2: Fifth line meets/crosses first line
            if i >= 4:
                if d[i-1] == d[i-3] and d[i] + d[i-4] >= d[i-2]:
                    return True
            
            # Case 3: Sixth line crosses first line
            if i >= 5:
                if d[i-2] >= d[i-4] and d[i] + d[i-4] >= d[i-2] and \
                   d[i-1] <= d[i-3] and d[i-1] + d[i-5] >= d[i-3]:
                    return True
                    
        return False