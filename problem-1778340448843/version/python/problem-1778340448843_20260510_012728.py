# Last updated: 10/05/2026, 01:27:28
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        count=0
4        if len(s)==0:
5            return True
6        for i in range(len(t)):
7            if t[i]==s[count]:
8                count=count+1
9            if count==len(s):
10                return True
11        return False   
12