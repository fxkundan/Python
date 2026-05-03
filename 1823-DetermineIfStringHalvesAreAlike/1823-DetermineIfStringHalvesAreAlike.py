# Last updated: 04/05/2026, 00:32:27
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s, n, cand = s.lower(), len(s), set("aeiou")
        return sum(i in cand for i in s[:n//2]) == sum(i in cand for i in s[n//2:])
        