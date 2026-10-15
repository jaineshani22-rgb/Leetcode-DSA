class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        last_sign = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                
            # If it's an operator or we reached the end of the string
            if char in "+-*/" or i == len(s) - 1:
                if char == ' ' and i != len(s) - 1:
                    continue
                    
                if last_sign == '+':
                    stack.append(current_num)
                elif last_sign == '-':
                    stack.append(-current_num)
                elif last_sign == '*':
                    stack.append(stack.pop() * current_num)
                elif last_sign == '/':
                    # Truncate towards zero in Python integer division
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-((-prev) // current_num))
                    else:
                        stack.append(prev // current_num)
                        
                last_sign = char
                current_num = 0
                
        return sum(stack)