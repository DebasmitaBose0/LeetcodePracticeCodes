import heapq

class MedianFinder:
    def __init__(self):
        # small is a Max-Heap (stores negatives)
        self.small = [] 
        # large is a Min-Heap
        self.large = [] 

    def addNum(self, num: int) -> None:
        # Step 1 & 2: Push to small, then move the largest of small to large
        # This keeps the two heaps correctly partitioned
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Step 3: Maintain size property (small size >= large size)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # If even number of elements, take the average of both tops
        return (-self.small[0] + self.large[0]) / 2.0