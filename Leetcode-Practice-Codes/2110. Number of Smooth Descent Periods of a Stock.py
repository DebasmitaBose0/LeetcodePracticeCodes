class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # total_periods starts at 1 because the first element is a period
        total_periods = 1
        # current_streak tracks the length of the smooth descent ending at i
        current_streak = 1
        
        for i in range(1, n):
            # Check if it follows the smooth descent rule: price[i] == price[i-1] - 1
            if prices[i] == prices[i - 1] - 1:
                current_streak += 1
            else:
                # Reset streak if the condition is broken
                current_streak = 1
            
            # Add the number of periods ending at the current index
            total_periods += current_streak
            
        return total_periods