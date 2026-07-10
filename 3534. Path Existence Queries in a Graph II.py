class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        # 1. Sort nodes by value, keeping track of original indices
        nodes = sorted(range(n), key=lambda x: nums[x])
        
        # Map original index -> sorted position index
        pos = {orig_idx: i for i, orig_idx in enumerate(nodes)}
        
        # 2. Build the greedy parent pointers using two pointers
        # parent[i] will store the sorted position index of the furthest reachable node to the right
        parent = list(range(n))
        right = 0
        for left in range(n):
            while right + 1 < n and nums[nodes[right + 1]] - nums[nodes[left]] <= maxDiff:
                right += 1
            parent[left] = right

        # 3. Precompute Binary Lifting Sparse Table
        # LOG = 17 is enough since n <= 10^5 (2^17 = 131,072)
        LOG = 17
        up = [[0] * LOG for _ in range(n)]
        
        for i in range(n):
            up[i][0] = parent[i]
            
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # 4. Process Queries
        ans = []
        for u_orig, v_orig in queries:
            if u_orig == v_orig:
                ans.append(0)
                continue
                
            # Convert original indices to sorted positions
            u = pos[u_orig]
            v = pos[v_orig]
            
            # Ensure u is the smaller value position to jump forward
            if u > v:
                u, v = v, u
                
            # If even the maximum single jump from u can't bridge the structural gap
            # (i.e., there is a disconnected break in the sorted array values)
            # We must check if the component can reach v.
            # If the furthest reachable node from u cannot even cross into v's zone or reach it:
            
            # Let's count how many jumps it takes to reach or pass 'v'
            jumps = 0
            curr = u
            
            # Jump using binary lifting from highest power down to 0
            for j in range(LOG - 1, -1, -1):
                if up[curr][j] < v:
                    curr = up[curr][j]
                    jumps += (1 << j)
            
            # Take one final step to see if we can reach or exceed v
            curr = up[curr][0]
            jumps += 1
            
            # If after jumping as close as possible, our next max jump still falls short of v,
            # then u and v are in disconnected components.
            if curr < v:
                ans.append(-1)
            else:
                ans.append(jumps)
                
        return ans