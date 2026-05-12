from collections import defaultdict
from functools import lru_cache

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = defaultdict(list)
        for u, v in hierarchy:
            adj[u].append(v)
            
        # Employee IDs are 1 to n
        pres = [0] + present
        fut = [0] + future

        @lru_cache(None)
        def dfs(u, boss_bought):
            # Base DP for current node: all zeros
            # dp[b] will store max profit for subtree at u with budget b
            dp = [0] * (budget + 1)
            
            # --- OPTION 1: BUY STOCK FOR U ---
            cost_u = pres[u] // 2 if boss_bought else pres[u]
            profit_u = fut[u] - cost_u
            
            res_buy = [float('-inf')] * (budget + 1)
            if cost_u <= budget:
                res_buy[cost_u] = profit_u
                for v in adj[u]:
                    child_dp = dfs(v, True)
                    # Knapsack merge
                    temp = [float('-inf')] * (budget + 1)
                    for b in range(cost_u, budget + 1):
                        if res_buy[b] == float('-inf'): continue
                        for cb in range(budget - b + 1):
                            temp[b + cb] = max(temp[b + cb], res_buy[b] + child_dp[cb])
                    res_buy = temp

            # --- OPTION 2: SKIP STOCK FOR U ---
            res_skip = [0] * (budget + 1)
            for v in adj[u]:
                child_dp = dfs(v, False)
                temp = [0] * (budget + 1)
                for b in range(budget + 1):
                    for cb in range(budget - b + 1):
                        temp[b + cb] = max(temp[b + cb], res_skip[b] + child_dp[cb])
                res_skip = temp
            
            # Combine the best of buying vs skipping for every budget level
            return tuple(max(res_buy[b], res_skip[b]) for b in range(budget + 1))

        return max(dfs(1, False))