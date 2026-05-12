import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []  # Max-heap (inverted)
        large = []  # Min-heap
        delayed = collections.Counter()
        
        def balance_heaps(small_size, large_size):
            # Keep heaps balanced: small can have at most one more than large
            nonlocal small, large
            if small_size > large_size + 1:
                heapq.heappush(large, -heapq.heappop(small))
                return -1, 1
            if small_size < large_size:
                heapq.heappush(small, -heapq.heappop(large))
                return 1, -1
            return 0, 0

        def prune(heap, is_small):
            while heap:
                num = -heap[0] if is_small else heap[0]
                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        # Initialize first window
        for i in range(k):
            heapq.heappush(small, -nums[i])
        for _ in range(k // 2):
            heapq.heappush(large, -heapq.heappop(small))
            
        res = []
        small_size, large_size = k - k // 2, k // 2
        
        for i in range(k, len(nums) + 1):
            # 1. Add median to result
            if k % 2 == 1:
                res.append(float(-small[0]))
            else:
                res.append((-small[0] + large[0]) / 2.0)
            
            if i == len(nums): break
            
            # 2. Setup window sliding
            out_num = nums[i - k]
            in_num = nums[i]
            diff = 0
            
            # 3. Handle outgoing element
            delayed[out_num] += 1
            if out_num <= -small[0]:
                diff -= 1
            else:
                diff += 1
                
            # 4. Handle incoming element
            if small and in_num <= -small[0]:
                heapq.heappush(small, -in_num)
                diff += 1
            else:
                heapq.heappush(large, in_num)
                diff -= 1
            
            # 5. Rebalance and prune
            if diff > 0:
                heapq.heappush(large, -heapq.heappop(small))
                prune(small, True)
            elif diff < 0:
                heapq.heappush(small, -heapq.heappop(large))
                prune(large, False)
                
            prune(small, True)
            prune(large, False)
            
        return res