from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        # To store frequencies of unmatched digits in secret
        secret_counts = Counter()
        guess_unmatched = []
        
        for s_char, g_char in zip(secret, guess):
            if s_char == g_char:
                bulls += 1
            else:
                secret_counts[s_char] += 1
                guess_unmatched.append(g_char)
                
        for g_char in guess_unmatched:
            if secret_counts[g_char] > 0:
                cows += 1
                secret_counts[g_char] -= 1
                
        return f"{bulls}A{cows}B"