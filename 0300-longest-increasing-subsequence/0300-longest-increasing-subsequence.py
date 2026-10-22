class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        
        for num in nums:
            # Find the index of the smallest element >= num
            idx = bisect.bisect_left(tails, num)
            
            # If num is larger than all elements, extend the tails list
            if idx == len(tails):
                tails.append(num)
            else:
                # Otherwise, update the existing tail to keep elements smaller
                tails[idx] = num
                
        return len(tails)