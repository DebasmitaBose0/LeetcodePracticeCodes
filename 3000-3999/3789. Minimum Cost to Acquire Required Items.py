class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Find how many units both requirements share
        common = min(need1, need2)
        rem1 = need1 - common
        rem2 = need2 - common
        
        # Cost to satisfy the overlapping portion using either Type 3 or (Type 1 + Type 2)
        cost_common = common * min(costBoth, cost1 + cost2)
        
        # Cost to satisfy remaining Type 1 needs using either Type 1 or Type 3
        cost_rem1 = rem1 * min(cost1, costBoth)
        
        # Cost to satisfy remaining Type 2 needs using either Type 2 or Type 3
        cost_rem2 = rem2 * min(cost2, costBoth)
        
        return cost_common + cost_rem1 + cost_rem2
