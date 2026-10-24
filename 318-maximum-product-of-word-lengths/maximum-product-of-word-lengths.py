from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lengths = [len(w) for w in words]
        
        # Precompute bitmasks for each word
        for i, word in enumerate(words):
            bitmask = 0
            for char in word:
                bitmask |= (1 << (ord(char) - ord('a')))
            masks[i] = bitmask
            
        max_val = 0
        for i in range(n):
            for j in range(i + 1, n):
                # If they share no common characters (bitwise AND is 0)
                if (masks[i] & masks[j]) == 0:
                    max_val = max(max_val, lengths[i] * lengths[j])
                    
        return max_val