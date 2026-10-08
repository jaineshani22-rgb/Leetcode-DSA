class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def get_next(number):
            output=0
            while number>0:
                digit=number%10
                output+=digit**2
                number//=10
            return output
        while n!=1 and n not in seen:
            seen.add(n)
            n=get_next(n)
        return n==1            