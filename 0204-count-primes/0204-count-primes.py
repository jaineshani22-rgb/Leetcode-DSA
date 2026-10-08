class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
            
        # Initialize a boolean array assuming all numbers are prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False # 0 and 1 are not prime
        
        # Sieve of Eratosthenes
        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                # Mark multiples of p as non-prime, starting from p*p
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
                    
        # Sum up all the True values remaining in the list
        return sum(is_prime)           