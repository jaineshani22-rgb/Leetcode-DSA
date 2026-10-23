class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1] * n
        k = len(primes)
        pointers = [0] * k
        next_multiples = list(primes)
        
        for i in range(1, n):
            # Find the smallest next multiple
            next_ugly = min(next_multiples)
            ugly[i] = next_ugly
            
            # Advance pointers for all primes that produced this minimum value
            for j in range(k):
                if next_multiples[j] == next_ugly:
                    pointers[j] += 1
                    next_multiples[j] = ugly[pointers[j]] * primes[j]
                    
        return ugly[n - 1]