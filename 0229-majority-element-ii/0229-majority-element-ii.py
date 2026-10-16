class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        # Phase 1: Find potential candidates
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
                
        # Phase 2: Verify the candidates
        result = []
        threshold = len(nums) // 3
        
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > threshold:
                if cand not in result:
                    result.append(cand)
                    
        return result