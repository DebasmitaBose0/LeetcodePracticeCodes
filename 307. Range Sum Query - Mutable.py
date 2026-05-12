class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        # BIT is 1-indexed, so we use size n + 1
        self.tree = [0] * (self.n + 1)
        for i, val in enumerate(nums):
            self.add(i + 1, val)

    def add(self, i: int, delta: int):
        # Propagate the change up the Fenwick Tree
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def update(self, index: int, val: int) -> None:
        # Calculate the difference between new value and old value
        delta = val - self.nums[index]
        self.nums[index] = val
        self.add(index + 1, delta)

    def query(self, i: int) -> int:
        # Get the prefix sum from 1 to i
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def sumRange(self, left: int, right: int) -> int:
        # sumRange(left, right) = prefixSum(right) - prefixSum(left - 1)
        return self.query(right + 1) - self.query(left)