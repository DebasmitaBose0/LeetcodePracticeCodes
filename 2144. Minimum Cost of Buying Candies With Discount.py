from ast import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort costs in descending order to always pick the most expensive candies first
        cost.sort(reverse=True)
        
        total_cost = 0
        
        # Iterate through the sorted list
        for i in range(len(cost)):
            # Every third candy (index 2, 5, 8...) is free
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
                
        return total_cost