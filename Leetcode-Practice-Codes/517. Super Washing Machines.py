class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total_dresses = sum(machines)
        n = len(machines)
        
        # Check if redistribution is possible
        if total_dresses % n != 0:
            return -1
        
        target = total_dresses // n
        max_moves = 0
        current_balance = 0
        
        for m in machines:
            # Difference from target for the current machine
            diff = m - target
            
            # Cumulative balance: how many dresses must pass through this point
            current_balance += diff
            
            # The bottleneck is the maximum of:
            # 1. The current cumulative flow (absolute value)
            # 2. The specific machine's need to export dresses (only if positive)
            max_moves = max(max_moves, abs(current_balance), diff)
            
        return max_moves