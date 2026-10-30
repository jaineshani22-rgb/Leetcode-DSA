class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # ans[i >> 1] gives the bit count of i // 2, 
            # and (i & 1) checks if the current last bit is 1 or 0.
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans