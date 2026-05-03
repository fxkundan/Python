# Last updated: 04/05/2026, 00:32:26
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        m=min(len(word1),len(word2))
        for i in range(m):
            res=res+word1[i]+word2[i]
        if(len(word1)>len(word2)):
            res=res+word1[m:len(word1)+1]
        else:
            res=res+word2[m:len(word2)+1]
        return res