class Solution:
    def isPowerOfFour(self, n: int) -> bool:
            # n must be positive, a power of two, and satisfy n % 3 == 1
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
   
    