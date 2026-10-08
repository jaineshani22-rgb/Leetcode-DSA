class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index={}
        max_len=0
        left=0
        right=0

        while right<len(s):
           if s[right] in char_index:
            left=max(left,char_index[s[right]]+1)

           max_len = max(max_len,right -left+1)
           char_index[s[right]]=right
           right+=1

        return max_len