from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # Build prefix sum array with an initial 0 for easier range calculations
        self.prefix = [0] * (len(nums) + 1)
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            self.prefix[i + 1] = current_sum

    def sumRange(self, left: int, right: int) -> int:
        # Range sum is prefix[right + 1] minus prefix[left]
        return self.prefix[right + 1] - self.prefix[left]