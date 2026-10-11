class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, None))
            
        events.sort()
        
        result = []
        max_heap = [(0, float('inf'))]
        
        for x, neg_height, right in events:
            while max_heap and max_heap[0][1] <= x:
                heappop(max_heap)
                
            if neg_height != 0:
                heappush(max_heap, (neg_height, right))
                
            max_height = -max_heap[0][0]
            
            if not result or result[-1][1] != max_height:
                result.append([x, max_height])
                
        return result