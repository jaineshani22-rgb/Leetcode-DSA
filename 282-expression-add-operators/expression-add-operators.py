class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res = []
        
        def backtrack(index: int, path: str, value: int, prev_operand: int):
            if index == len(num):
                if value == target:
                    res.append(path)
                return
                
            for i in range(index, len(num)):
                # Numbers with leading zeros are invalid (e.g., "05")
                if i != index and num[index] == '0':
                    break
                    
                curr_str = num[index:i+1]
                curr_val = int(curr_str)
                
                if index == 0:
                    # First number doesn't take an operator preceding it
                    backtrack(i + 1, curr_str, curr_val, curr_val)
                else:
                    backtrack(i + 1, path + "+" + curr_str, value + curr_val, curr_val)
                    backtrack(i + 1, path + "-" + curr_str, value - curr_val, -curr_val)
                    backtrack(i + 1, path + "*" + curr_str, value - prev_operand + prev_operand * curr_val, prev_operand * curr_val)
                    
        backtrack(0, "", 0, 0)
        return res