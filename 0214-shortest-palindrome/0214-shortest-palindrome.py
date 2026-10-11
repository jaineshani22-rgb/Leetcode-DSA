class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
            
        rev_s = s[::-1]
        # Combine original string, a separator, and the reversed string
        combined = s + "#" + rev_s
        
        # Build the KMP LPS (Longest Prefix Suffix) table
        lps = [0] * len(combined)
        j = 0
        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j
                
        # lps[-1] gives the length of the longest palindromic prefix of s
        pal_len = lps[-1]
        
        # Take the remaining un-matched suffix from s, reverse it, and prepend it
        add_to_front = rev_s[:len(s) - pal_len]
        return add_to_front + s