class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        # 1. Find the indices of all seats ('S')
        seat_indices = [i for i, char in enumerate(corridor) if char == 'S']
        n = len(seat_indices)
        
        # 2. If there are no seats or an odd number of seats, return 0
        if n == 0 or n % 2 != 0:
            return 0
        
        # 3. Calculate the number of ways based on the gaps between pairs of seats
        # We look at the gap between the 2nd seat of pair 'i' and the 1st seat of pair 'i+1'
        # These gaps occur at indices 1, 3, 5, ... in our seat_indices list
        ans = 1
        for i in range(1, n - 1, 2):
            # Number of plants + 1 between seat_indices[i] and seat_indices[i+1]
            gap_size = seat_indices[i+1] - seat_indices[i]
            ans = (ans * gap_size) % MOD
            
        return ans