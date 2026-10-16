class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        q = deque()  # Stores indices of elements
        
        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # Remove smaller elements from the back as they are useless
            while q and nums[q[-1]] < num:
                q.pop()
                
            q.append(i)
            
            # Once we reach the first full window, record the max
            if i >= k - 1:
                ans.append(nums[q[0]])
                
        return ans