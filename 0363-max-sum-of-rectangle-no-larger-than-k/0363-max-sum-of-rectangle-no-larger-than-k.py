class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        # Iterate over all possible left columns
        for left in range(cols):
            row_sums = [0] * rows
            # Iterate over all possible right columns starting from left
            for right in range(left, cols):
                # Accumulate the row sums between 'left' and 'right' columns
                for r in range(rows):
                    row_sums[r] += matrix[r][right]
                    
                # Find the maximum subarray sum <= k in the 1D row_sums array
                current_sum = 0
                prefix_sums = [0]
                
                for val in row_sums:
                    current_sum += val
                    # We want current_sum - prev_sum <= k => prev_sum >= current_sum - k
                    target = current_sum - k
                    idx = bisect.bisect_left(prefix_sums, target)
                    
                    if idx < len(prefix_sums):
                        max_sum = max(max_sum, current_sum - prefix_sums[idx])
                        if max_sum == k:
                            return k # Early exit if we find an exact match
                            
                    bisect.insort(prefix_sums, current_sum)
                    
        return max_sum