class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        word_map = {word: i for i, word in enumerate(words)}
        result = set()
        
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                left = word[:j]
                right = word[j:]
                
                # If left part is a palindrome, look for reverse(right)
                if left == left[::-1]:
                    rev_right = right[::-1]
                    if rev_right in word_map and word_map[rev_right] != i:
                        result.add((word_map[rev_right], i))
                        
                # If right part is a palindrome, look for reverse(left)
                if right == right[::-1]:
                    rev_left = left[::-1]
                    if rev_left in word_map and word_map[rev_left] != i:
                        result.add((i, word_map[rev_left]))
                        
        return list(result)