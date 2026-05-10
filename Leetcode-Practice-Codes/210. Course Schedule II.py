from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # start with nodes having 0 indegree
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        order = []
        
        while q:
            course = q.popleft()
            order.append(course)
            
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # if all courses processed → valid
        return order if len(order) == numCourses else []