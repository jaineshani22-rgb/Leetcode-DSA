class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
            
        # If target is 0, it's always possible (doing nothing)
        if target == 0:
            return True
            
        # Target must be a multiple of the greatest common divisor of x and y
        return target % math.gcd(x, y) == 0