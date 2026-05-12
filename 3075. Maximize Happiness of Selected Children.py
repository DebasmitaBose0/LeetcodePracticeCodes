class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # 1. Sort happiness in descending order to pick the largest values first
        happiness.sort(reverse=True)
        
        total_happiness = 0
        
        # 2. Iterate k times to select k children
        for i in range(k):
            # The happiness decreases by 'i' based on the number of turns passed
            # We use max(0, ...) because happiness cannot be negative
            current_happiness = max(0, happiness[i] - i)
            
            # If we hit 0, all subsequent children will also contribute 0
            if current_happiness == 0:
                break
                
            total_happiness += current_happiness
            
        return total_happiness