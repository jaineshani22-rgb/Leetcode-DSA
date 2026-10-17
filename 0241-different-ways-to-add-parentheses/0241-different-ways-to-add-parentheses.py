class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}
        
        def compute(s: str) -> List[int]:
            if s in memo:
                return memo[s]
                
            res = []
            for i, char in enumerate(s):
                if char in "+-*":
                    # Divide into left and right sub-expressions
                    left = compute(s[:i])
                    right = compute(s[i+1:])
                    
                    # Combine all possible results from left and right
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
                                
            # Base case: if no operator was found, the string is just a number
            if not res:
                res.append(int(s))
                
            memo[s] = res
            return res
            
        return compute(expression)