class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}
        
        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            
            min_cost = float('inf')
            for x in range(left, right + 1):
                # Worst-case cost of choosing x plus the max cost from subranges
                cost = x + max(dp(left, x - 1), dp(x + 1, right))
                min_cost = min(min_cost, cost)
                
            memo[(left, right)] = min_cost
            return min_cost
            
        return dp(1, n)