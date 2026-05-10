class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        # Scenario 1: Compare everything with the first house (index 0)
        # Find the furthest house from the right that isn't colors[0]
        d1 = 0
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                d1 = i
                break
        
        # Scenario 2: Compare everything with the last house (index n-1)
        # Find the furthest house from the left that isn't colors[n-1]
        d2 = 0
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                d2 = (n - 1) - i
                break
                
        return max(d1, d2)