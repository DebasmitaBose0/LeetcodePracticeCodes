import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        # Convert list into a heap structure in-place
        heapq.heapify(self.heap)
        
        # Maintain only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Push the new value onto the heap
        heapq.heappush(self.heap, val)
        
        # If the size exceeds k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root of the min-heap is the kth largest element
        return self.heap[0]