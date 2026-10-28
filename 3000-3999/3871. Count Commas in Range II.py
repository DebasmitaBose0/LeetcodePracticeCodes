class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        total_commas = 0
        start = 1000
        commas = 1
        
        while start <= n:
            # The upper bound for the current digit group (e.g., 999999 for 1-comma group)
            end = min(n, (start * 1000) - 1)
            
            # Count how many numbers fall into this range and multiply by the comma count
            total_commas += (end - start + 1) * commas
            
            # Move to the next group (e.g., from thousands to millions)
            start *= 1000
            commas += 1
            
        return total_commas