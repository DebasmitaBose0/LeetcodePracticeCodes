import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n, m = len(servers), len(tasks)
        
        # Min-heap of available servers: stores (weight, index)
        available = [(servers[i], i) for i in range(n)]
        heapq.heapify(available)
        
        # Min-heap of busy servers: stores (free_time, weight, index)
        busy = []
        
        ans = []
        current_time = 0
        
        for j in range(m):
            current_time = max(current_time, j)
            
            # Release all servers that become free by current_time
            while busy and busy[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))
            
            # If no servers are available, jump time to when the next server frees up
            if not available:
                current_time = busy[0][0]
                while busy and busy[0][0] <= current_time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))
            
            # Assign the task to the best available server
            weight, index = heapq.heappop(available)
            ans.append(index)
            
            # Push the server into the busy heap with its new release time
            heapq.heappush(busy, (current_time + tasks[j], weight, index))
            
        return ans