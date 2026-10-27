from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        
        def dfs(r: int, c: int) -> int:
            if memo[r][c] != 0:
                return memo[r][c]
                
            max_len = 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
                    
            memo[r][c] = max_len
            return max_len
            
        longest_path = 0
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))
                
        return longest_path