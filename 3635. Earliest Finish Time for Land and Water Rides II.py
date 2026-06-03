from typing import List
import bisect

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        # Helper function to evaluate one direction (First Category -> Second Category)
        def get_min_time(start1, dur1, start2, dur2):
            # Pair up and sort the second category by their start times
            rides2 = sorted(zip(start2, dur2), key=lambda x: x[0])
            n2 = len(rides2)
            
            # Precompute prefix minimums of durations for rides that open early
            pref_min_dur = [float('inf')] * n2
            current_min_dur = float('inf')
            for i in range(n2):
                current_min_dur = min(current_min_dur, rides2[i][1])
                pref_min_dur[i] = current_min_dur
                
            # Precompute suffix minimums of individual end times for rides that open late
            suff_min_end = [float('inf')] * n2
            current_min_end = float('inf')
            for i in range(n2 - 1, -1, -1):
                current_min_end = min(current_min_end, rides2[i][0] + rides2[i][1])
                suff_min_end[i] = current_min_end
                
            # Extract just the start times of category 2 for binary searching
            start_times2 = [r[0] for r in rides2]
            
            best_total_finish = float('inf')
            
            # Evaluate each ride from the first category
            for s1, d1 in zip(start1, dur1):
                t1 = s1 + d1 # Finish time of the first ride
                
                # Find the boundary where ride2_start_time > t1
                idx = bisect.bisect_right(start_times2, t1)
                
                # Group A: rides2 that start <= t1 (we can board immediately at t1)
                if idx > 0:
                    best_total_finish = min(best_total_finish, t1 + pref_min_dur[idx - 1])
                    
                # Group B: rides2 that start > t1 (we must wait for them to open)
                if idx < n2:
                    best_total_finish = min(best_total_finish, suff_min_end[idx])
                    
            return best_total_finish

        # The tourist can take the rides in either order, so we check both paths
        path1 = get_min_time(landStartTime, landDuration, waterStartTime, waterDuration)
        path2 = get_min_time(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(path1, path2)