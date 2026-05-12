import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a list of pairs (capital_required, profit) and sort by capital
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        i = 0
        n = len(projects)
        
        # We can pick up to k projects
        for _ in range(k):
            # Add all projects we can afford with current capital 'w' to the max-heap
            while i < n and projects[i][0] <= w:
                # Python's heapq is a min-heap, so we push negative profit to simulate a max-heap
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # If no projects can be afforded, we stop early
            if not max_heap:
                break
            
            # Pick the project with the maximum profit
            w += -heapq.heappop(max_heap)
            
        return w