class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        
        def count_less_equal(mid: int) -> int:
            # Count elements <= mid in O(n) time starting from bottom-left
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    # All elements in this column from top to current row are <= mid
                    count += (row + 1)
                    col += 1
                else:
                    row -= 1
            return count

        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
                
        return left