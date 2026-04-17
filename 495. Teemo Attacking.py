class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_time = 0
        # Iterate through attacks up to the second to last one
        for i in range(len(timeSeries) - 1):
            # Add the minimum of the full duration or the gap to the next attack
            total_time += min(timeSeries[i + 1] - timeSeries[i], duration)
        
        # The last attack always lasts the full duration
        return total_time + duration