from ast import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Find all unique elements and sort them
        # Sorting unique elements gives us their exact rank order
        sorted_unique = sorted(list(set(arr)))
        
        # Step 2: Map each unique element to its rank (1-indexed)
        # Using a dictionary allows O(1) lookups later
        ranks = {num: rank for rank, num in enumerate(sorted_unique, 1)}
        
        # Step 3: Replace each original element with its assigned rank
        return [ranks[num] for num in arr]