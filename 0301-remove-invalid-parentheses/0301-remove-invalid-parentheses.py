class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Helper function to check if a string has valid parentheses
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        if not s:
            return [""]

        # BFS queue/level set
        level = {s}
        
        while True:
            # Check if any string in the current level is valid
            valid_res = [curr for curr in level if isValid(curr)]
            if valid_res:
                return valid_res
            
            # Generate next level by removing one parenthesis at a time
            next_level = set()
            for curr in level:
                for i in range(len(curr)):
                    if curr[i] in ('(', ')'):
                        next_level.add(curr[:i] + curr[i+1:])
            level = next_level