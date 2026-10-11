class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, path: List[int], current_sum: int):
            # Base case: valid combination found
            if len(path) == k and current_sum == n:
                result.append(list(path))
                return
            
            # Pruning condition: stop if path is too long, sum exceeds n, or numbers run out
            if len(path) > k or current_sum > n or start > 9:
                return
            
            # Iterate through available numbers from start to 9
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, current_sum + i)
                path.pop()  # Backtrack
                
        backtrack(1, [], 0)
        return result