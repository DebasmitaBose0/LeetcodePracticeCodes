class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city):
            # Mark the current city as visited
            visited.add(city)
            # Check all possible neighbors (other cities)
            for neighbor in range(n):
                # If connected and not yet visited, explore that neighbor
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
        
        # Iterate through each city
        for i in range(n):
            # If we find a city not visited, it's a new province
            if i not in visited:
                provinces += 1
                dfs(i)
                
        return provinces