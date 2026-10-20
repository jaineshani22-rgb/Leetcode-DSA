from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        # 8 possible directional offsets for neighbors
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        # First Pass: Compute next states using encoded markers
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # Check if neighbor was originally alive (1 or 2)
                        if board[nr][nc] in (1, 2):
                            live_neighbors += 1
                            
                # Apply Conway's rules
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2  # Live -> Dead
                else:
                    if live_neighbors == 3:
                        board[r][c] = 3  # Dead -> Live
                        
        # Second Pass: Finalize states to 0 and 1
        for r in range(rows):
            for c in range(cols):
                board[r][c] %= 2