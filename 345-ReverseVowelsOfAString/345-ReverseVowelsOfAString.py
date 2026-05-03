# Last updated: 04/05/2026, 00:33:02
class Solution:
    def reverseVowels(self, word: str) -> str:
        s=list(word)
        vow="aeiouAEIOU"
        r={}
        left=0
        right=len(s)-1
        while left < right:
            if  s[left] in vow and s[right] in vow:
                s[left],s[right]=s[right],s[left]
                left=left+1
                right=right-1
            if s[left] not in vow: 
                left=left+1
            if s[right] not in vow:
                right=right-1
            
            
        return "".join(s)



        