class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        # Step 1: Find the absolute earliest completion time for the first ride
        min_land_end = float('inf')
        for start, duration in zip(landStartTime, landDuration):
            min_land_end = min(min_land_end, start + duration)
            
        min_water_end = float('inf')
        for start, duration in zip(waterStartTime, waterDuration):
            min_water_end = min(min_water_end, start + duration)
            
        ans = float('inf')
        
        # Step 2: Scenario A (Land -> Water)
        # We start the water ride at either its opening time or when the land ride finishes, whichever is later.
        for start, duration in zip(waterStartTime, waterDuration):
            ans = min(ans, max(min_land_end, start) + duration)
            
        # Step 3: Scenario B (Water -> Land)
        # We start the land ride at either its opening time or when the water ride finishes, whichever is later.
        for start, duration in zip(landStartTime, landDuration):
            ans = min(ans, max(min_water_end, start) + duration)
            
        return ans