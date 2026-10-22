class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False
            
        # Try all possible lengths for the first number
        for i in range(1, n // 2 + 1):
            # First number cannot have leading zeros unless it is "0"
            if num[0] == '0' and i > 1:
                break
                
            # Try all possible lengths for the second number
            for j in range(1, n - i):
                # Second number cannot have leading zeros unless it is "0"
                if num[i] == '0' and j > 1:
                    break
                    
                n1_str = num[:i]
                n2_str = num[i:i+j]
                
                if self.isValid(n1_str, n2_str, num[i+j:]):
                    return True
                    
        return False
        
    def isValid(self, n1_str: str, n2_str: str, remainder: str) -> bool:
        n1 = int(n1_str)
        n2 = int(n2_str)
        
        while remainder:
            n3 = n1 + n2
            n3_str = str(n3)
            
            # Check if the remaining string starts with the expected sum
            if not remainder.startswith(n3_str):
                return False
                
            # Shift forward
            remainder = remainder[len(n3_str):]
            n1, n2 = n2, n3
            
        return True