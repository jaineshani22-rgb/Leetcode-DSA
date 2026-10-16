class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1  # Start at the top-right corner
        
        while row < rows and col >= 0:
            curr = matrix[row][col]
            
            if curr == target:
                return True
            elif curr > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down
                
        return False