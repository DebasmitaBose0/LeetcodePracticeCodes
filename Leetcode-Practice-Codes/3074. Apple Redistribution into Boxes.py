class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # 1. Get the total number of apples
        total_apples = sum(apple)
        
        # 2. Sort capacities from largest to smallest
        capacity.sort(reverse=True)
        
        # 3. Use the largest boxes first until all apples are packed
        boxes_used = 0
        for cap in capacity:
            total_apples -= cap
            boxes_used += 1
            
            # If total_apples is 0 or less, we have enough capacity
            if total_apples <= 0:
                break
                
        return boxes_used