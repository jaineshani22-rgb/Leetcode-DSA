class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i] will store the number of combinations that add up to i
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: 1 way to make sum 0
        
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
                    
        return dp[target]