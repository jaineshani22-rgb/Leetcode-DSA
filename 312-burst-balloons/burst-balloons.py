class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] represents max coins from bursting balloons between index i and j
        dp = [[0] * n for _ in range(n)]
        
        # Length of the interval (number of elements between i and j)
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                # Try every balloon k as the LAST one to burst in range (i, j)
                for k in range(i + 1, j):
                    coins = nums[i] * nums[k] * nums[j]
                    total = dp[i][k] + coins + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
                    
        return dp[0][n - 1]