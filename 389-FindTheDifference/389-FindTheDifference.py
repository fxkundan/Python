# Last updated: 04/05/2026, 00:32:59
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        for i,j in enumerate(s):
            if j != t[i]: return t[i]
        return t[-1]
                    
        