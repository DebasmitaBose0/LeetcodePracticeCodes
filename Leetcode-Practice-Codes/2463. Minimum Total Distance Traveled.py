class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # 1. Sort both to ensure the contiguous subsegment property holds
        robot.sort()
        factory.sort()
        
        # 2. Flatten factories: [pos, limit] -> [pos, pos, pos...]
        factory_positions = []
        for pos, limit in factory:
            factory_positions.extend([pos] * limit)
            
        m, n = len(robot), len(factory_positions)
        
        # 3. DP table: dp[i][j] is min distance for i robots and j factory slots
        # Initialize with a very large value
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: 0 robots require 0 distance
        for j in range(n + 1):
            dp[0][j] = 0
            
        # 4. Fill the DP table
        for i in range(1, m + 1): # For each robot
            for j in range(1, n + 1): # For each factory slot
                # Option 1: Don't use the current factory slot for any robot
                dp[i][j] = dp[i][j-1]
                
                # Option 2: Use the current factory slot for the current robot
                # Distance = |robot_pos - factory_pos| + min distance for remaining
                current_dist = abs(robot[i-1] - factory_positions[j-1])
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + current_dist)
                
        return dp[m][n]