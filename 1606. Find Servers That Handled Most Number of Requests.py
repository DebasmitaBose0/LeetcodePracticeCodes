import bisect
from heapq import heappop, heappush

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Heap to store (free_time, server_id) for currently busy servers
        busy = []
        
        # Available servers stored in sorted order
        # We can use a list and bisect, maintaining sorted order, or sortedcontainers.
        # Below is an efficient approach using a sorted list / array with bisect.
        # pyrefly: ignore[missing-import]
        from sortedcontainers import SortedList
        available = SortedList(range(k))
        
        request_count = [0] * k
        
        for i, start_time in enumerate(arrival):
            # Free up servers whose task has finished by current arrival time
            while busy and busy[0][0] <= start_time:
                _, sid = heappop(busy)
                available.add(sid)
                
            # If no servers are available, the request is dropped
            if not available:
                continue
                
            # Find the first available server >= (i % k)
            target = i % k
            idx = available.bisect_left(target)
            
            # If no server >= target, wrap around to the beginning (index 0)
            if idx == len(available):
                idx = 0
                
            server_id = available[idx]
            
            # Assign the request to this server
            available.remove(server_id)
            heappush(busy, (start_time + load[i], server_id))
            request_count[server_id] += 1
            
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]