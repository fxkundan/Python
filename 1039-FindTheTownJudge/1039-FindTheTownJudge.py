# Last updated: 04/05/2026, 00:32:42
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        length=len(trust)
        if length == 0 and n == 1:
            return 1
        
        if length == 0 and n > 1:
            return -1
        countermap={}
        checkmap={}
        x=-1
        for i in range(length):
            if(trust[i][1] in countermap):
             countermap[trust[i][1]]=countermap[trust[i][1]]+1
            else:
                countermap[trust[i][1]]=1
            checkmap[trust[i][0]]=trust[i][1]
        print(countermap)
        print(checkmap)
        for k in countermap:
            if countermap[k] == n-1:
                x=k

        if(x==-1):
            return -1
        else:
            if(x in checkmap):
                return -1
            else:
                return x