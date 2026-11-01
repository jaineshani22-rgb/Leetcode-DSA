class Solution:
    def isPalindrome(self, x: int) -> bool:
       if x<0:
        return False
       s=0 
       i=x
       while(i!=0):
        digit = i % 10
        i//=10
        s = s * 10 + digit
       if (s==x):
        return True
       return False  
