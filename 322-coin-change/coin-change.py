from typing import List

class Solution:
    def coinChanges(self, coins: List[int], amount: int) -> int:
        pass # placeholder check for method name
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with amount + 1 (infinity sentinel)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != amount + 1 else -1