from ast import List
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # component[i] will store the component ID for node i
        component = [0] * n
        curr_id = 0
        
        for i in range(1, n):
            # If the gap between adjacent elements is too large, 
            # they belong to different connected components
            if nums[i] - nums[i-1] > maxDiff:
                curr_id += 1
            component[i] = curr_id
            
        # Answer each query in O(1) time
        return [component[u] == component[v] for u, v in queries]