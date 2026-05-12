class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur_penalty = 0
        min_penalty = 0
        best_hour = 0
        
        for i, char in enumerate(customers):
            if char == 'Y':
                # Closing later serves a customer who would have been a penalty
                cur_penalty -= 1
            else:
                # Closing later keeps the shop open for an empty hour
                cur_penalty += 1
            
            # If we find a new strictly lower penalty, update best_hour
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                best_hour = i + 1
                
        return best_hour