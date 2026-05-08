class Solution:
    def bestTower(self, towers, center, radius):
        cx, cy = center
        best_q = -1
        ans = [-1, -1]
        
        for x, y, q in towers:
            dist = abs(x - cx) + abs(y - cy)
            
            if dist <= radius:
                if q > best_q or (q == best_q and [x, y] < ans):
                    best_q = q
                    ans = [x, y]
        
        return ans