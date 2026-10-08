class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = [-1] * 256
        map_t = [-1] * 256
        
        for c1, c2 in zip(s, t):
            i1, i2 = ord(c1), ord(c2)
            
            # Check for existing mapping conflicts
            if map_s[i1] != -1 and map_s[i1] != i2:
                return False
            if map_t[i2] != -1 and map_t[i2] != i1:
                return False
                
            # Establish the mapping
            map_s[i1] = i2
            map_t[i2] = i1
            
        return True