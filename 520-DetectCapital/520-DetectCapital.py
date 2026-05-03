# Last updated: 04/05/2026, 00:32:52
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word[1:]==word[1:].lower() or word==word.upper()
