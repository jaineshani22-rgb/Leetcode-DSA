class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1  # 1 for positive, -1 for negative
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                res += sign * num
                num = 0
                sign = 1
            elif char == '-':
                res += sign * num
                num = 0
                sign = -1
            elif char == '(':
                # Save current result and sign onto the stack
                stack.append(res)
                stack.append(sign)
                # Reset for the inner expression
                res = 0
                sign = 1
            elif char == ')':
                # Complete the current inner expression
                res += sign * num
                num = 0
                # Multiply by the sign before the parenthesis
                res *= stack.pop()
                # Add the result accumulated before the parenthesis
                res += stack.pop()
                
        # Add any remaining number at the end of the string
        res += sign * num
        return res