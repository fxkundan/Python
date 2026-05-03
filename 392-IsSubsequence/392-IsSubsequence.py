# Last updated: 04/05/2026, 00:32:58
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # j=0
        # for c in s:
        #     i=t.find(c,j,len(t))
        #     if(i==-1):
        #         return False
        #     else:
        #         j=i+1
        # return True
        i,j=0,0
        while i<len(s) and j <len(t):
            if(s[i]==t[j]):
                i=i+1
                j=j+1
            else:
                j=j+1
                
        return (i==len(s))