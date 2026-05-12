class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1
        
        for _ in range(n):
            res.append(curr)
            
            # Try to go "deeper" (multiply by 10)
            if curr * 10 <= n:
                curr *= 10
            else:
                # If we hit the limit or can't go deeper, go "wider" (increment)
                # But if incrementing ends in a carry (e.g., 19 -> 20),
                # or if we exceed n, we must backtrack (divide by 10)
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
                
        return res