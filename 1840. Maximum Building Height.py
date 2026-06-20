class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # 1. Add the absolute boundaries
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        # 2. Sort by building ID
        restrictions.sort()
        
        m = len(restrictions)
        
        # 3. Left-to-Right Pass
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
            
        # 4. Right-to-Left Pass
        for i in range(m - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
            
        # 5. Find the maximum height achieved anywhere in the gaps
        max_height = 0
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            
            # Formula to find the highest peak between two valid restricted points
            current_max = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, current_max)
            
        return max_height