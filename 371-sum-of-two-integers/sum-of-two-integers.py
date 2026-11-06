class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask (2^32 - 1)
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            # Calculate sum without carry using XOR and apply 32-bit mask
            sum_without_carry = (a ^ b) & MASK
            # Calculate carry using AND, shift left, and apply mask
            carry = ((a & b) << 1) & MASK
            
            a = sum_without_carry
            b = carry
            
        # If 'a' is negative in 32-bit representation, convert it back from unsigned mask
        return a if a <= MAX_INT else ~(a ^ MASK)