# Last updated: 04/05/2026, 00:32:23
class Solution:
    def finalString(self, s: str) -> str:
        l=len(s)
        res=""
        for i in range(l):
            if s[i]=="i":
                res=res[::-1]
            else:
                res=res+s[i]
        return res

        
        