class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        # Array to store count of papers for each citation number up to n
        count = [0] * (n + 1)
        
        # Count the frequency of each citation
        for citation in citations:
            # If a paper has more than n citations, cap it at n
            count[min(citation, n)] += 1 
            
        accumulate = 0
        # Iterate backwards from maximum possible h-index (n) down to 0
        for i in range(n, -1, -1):
            accumulate += count[i]
            # If the cumulative papers with >= i citations is >= i, we found the H-Index
            if accumulate >= i:
                return i
                
        return 0