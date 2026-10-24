class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Record the last index of each character in the string
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char in seen:
                continue
                
            # Pop from stack if the top element is lexicographically larger 
            # than the current char AND it appears again later in the string
            while stack and stack[-1] > char and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)