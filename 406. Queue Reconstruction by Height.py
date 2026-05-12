class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending, then by k ascending
        # -x[0] makes height descending, x[1] makes k ascending
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        for p in people:
            # The person's 'k' value becomes their insertion index
            queue.insert(p[1], p)
            
        return queue