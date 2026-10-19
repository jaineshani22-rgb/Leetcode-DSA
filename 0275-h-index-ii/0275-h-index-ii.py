class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            # If citations[mid] is greater than or equal to the number of papers from mid to the end
            if citations[mid] >= n - mid:
                high = mid - 1  # Try to find a better (smaller index / larger h-index) on the left
            else:
                low = mid + 1   # Need more citations, move right
                
        # The number of papers with at least citations[low] citations is n - low
        return n - low