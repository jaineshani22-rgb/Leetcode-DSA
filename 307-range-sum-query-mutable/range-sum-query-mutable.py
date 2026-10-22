from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        
        # Build the Fenwick tree initially
        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, i: int, delta: int) -> None:
        """Helper to add delta to index i and propagate upwards."""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def _query(self, i: int) -> int:
        """Helper to get prefix sum from index 1 to i."""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right + 1) - self._query(left)