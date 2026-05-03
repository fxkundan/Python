# Last updated: 04/05/2026, 00:33:43
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordlist = s.split()
        if wordlist:
            return len(wordlist[-1])
        return 0