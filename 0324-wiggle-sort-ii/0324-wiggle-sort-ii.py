from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        
        # Split into two halves
        mid = (n + 1) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        # Interleave backwards into odd and even positions
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1]