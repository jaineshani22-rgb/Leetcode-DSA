class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        n = len(distance)
        if n < 4:
            return False
            
        for i in range(3, n):
            # Case 1: Current line crosses the line 3 steps ahead
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
                
            # Case 2: 5th line meets the 1st line exactly
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True
                
            # Case 3: Expanding spiral crossing
            if i >= 5 and distance[i-2] >= distance[i-4] and distance[i-1] <= distance[i-3] and distance[i] + distance[i-4] >= distance[i-2] and distance[i-1] + distance[i-5] >= distance[i-3]:
                return True
                
        return False