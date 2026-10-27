from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1
        i = 0
        m = len(nums)
        
        while miss <= n:
            if i < m and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # Patch with 'miss', which doubles our coverage up to 2 * miss - 1
                miss += miss
                patches += 1
                
        return patches