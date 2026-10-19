# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # The bad version is mid or to the left
            else:
                left = mid + 1  # The bad version is to the right
                
        return left