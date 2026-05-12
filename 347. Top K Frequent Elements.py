class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 2. Create buckets where index = frequency
        # Each index will hold a list of numbers with that frequency
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in count.items():
            freq_buckets[f].append(num)
        
        # 3. Collect top k elements starting from the end of buckets
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res