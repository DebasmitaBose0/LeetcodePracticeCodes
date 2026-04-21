class UF:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UF(n)
        
        # 1. Group indices that can be swapped
        for a, b in allowedSwaps:
            uf.union(a, b)
            
        # 2. Map each root component to the counts of numbers available in 'source'
        groups = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            root = uf.find(i)
            groups[root][source[i]] += 1
            
        # 3. Calculate Hamming Distance
        # For each index i, check if target[i] exists in its connected component
        hamming_distance = 0
        for i in range(n):
            root = uf.find(i)
            if groups[root][target[i]] > 0:
                groups[root][target[i]] -= 1
            else:
                hamming_distance += 1
                
        return hamming_distance