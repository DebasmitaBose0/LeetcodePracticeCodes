import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []
        
        # create events
        for l, r, h in buildings:
            events.append((l, -h))  # start
            events.append((r, h))   # end
        
        events.sort()
        
        result = []
        heap = [0]  # max heap (store negative heights)
        prev_max = 0
        
        for x, h in events:
            if h < 0:
                heapq.heappush(heap, h)
            else:
                heap.remove(-h)
                heapq.heapify(heap)
            
            curr_max = -heap[0]
            
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max
        
        return result