from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # 1. Initialize the set of people who know the secret
        known = {0, firstPerson}
        
        # 2. Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        m = len(meetings)
        while i < m:
            curr_time = meetings[i][2]
            # Group all meetings happening at the same time
            time_group = []
            while i < m and meetings[i][2] == curr_time:
                time_group.append(meetings[i])
                i += 1
            
            # 3. Build a graph for the current time frame
            adj = defaultdict(list)
            people_at_time = set()
            for u, v, t in time_group:
                adj[u].append(v)
                adj[v].append(u)
                people_at_time.add(u)
                people_at_time.add(v)
            
            # 4. BFS starting from people who already know the secret
            queue = deque([p for p in people_at_time if p in known])
            
            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in known:
                        known.add(neighbor)
                        queue.append(neighbor)
                        
        return list(known)