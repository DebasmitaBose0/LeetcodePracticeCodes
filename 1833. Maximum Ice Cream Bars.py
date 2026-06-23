from ast import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # The maximum possible cost based on constraints
        MAX_COST = 100000
        
        # Create a frequency array to store the count of each ice cream cost
        count = [0] * (MAX_COST + 1)
        for cost in costs:
            count[cost] += 1
            
        ice_cream_count = 0
        
        # Iterate through all possible costs from cheapest to most expensive
        for cost in range(1, MAX_COST + 1):
            if count[cost] == 0:
                continue
                
            # If we can't even afford one ice cream of this cost, we are done
            if coins < cost:
                break
                
            # Determine how many ice creams of this cost we can afford
            # It's bounded by how many are available and our total coins
            buy = min(count[cost], coins // cost)
            
            # Update our totals
            ice_cream_count += buy
            coins -= buy * cost
            
        return ice_cream_count