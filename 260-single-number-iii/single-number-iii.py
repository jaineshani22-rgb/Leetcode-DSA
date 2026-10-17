class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        # Step 1: Get the XOR sum of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
            
        # Step 2: Find the rightmost set bit
        diff_bit = xor_all & -xor_all
        
        # Step 3: Divide numbers into two groups and XOR them
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]