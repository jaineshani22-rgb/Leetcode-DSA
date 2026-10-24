from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        best = []
        
        # Helper to find the maximum subsequence of length length from nums
        def max_subsequence(nums, length):
            drop = len(nums) - length
            stack = []
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]
            
        # Helper to merge two sequences to form the largest possible combined sequence
        def merge(seq1, seq2):
            res = []
            i = j = 0
            while i < len(seq1) or j < len(seq2):
                # Compare remaining slices lexicographically
                if seq1[i:] > seq2[j:]:
                    res.append(seq1[i])
                    i += 1
                else:
                    res.append(seq2[j])
                    j += 1
            return res

        # Try every possible number of digits i to take from nums1
        for i in range(max(0, k - n), min(k, m) + 1):
            sub1 = max_subsequence(nums1, i)
            sub2 = max_subsequence(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > best:
                best = candidate
                
        return best