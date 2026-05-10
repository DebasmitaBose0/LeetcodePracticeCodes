from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # queue of courses with no prerequisites
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        
        while q:
            course = q.popleft()
            count += 1
            
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return count == numCourses