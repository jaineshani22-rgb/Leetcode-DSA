class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        # Helper function for the standard linear House Robber I problem
        def rob_linear(houses: List[int]) -> int:
            prev2 = 0  # max money 2 houses ago
            prev1 = 0  # max money 1 house ago
            
            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
                
            return prev1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))    