# Last updated: 04/05/2026, 00:32:40
class Solution:
    def Dec2Bin(self,n):
        list1=[]
        if(n==0):
            list1.append(0)
            return list1
        while(n>=1):
            list1.append(n%2)
            n=int(n/2)
        list1.reverse()
        return list1
    def bitwiseComplement(self, n: int) -> int:         
        Result=self.Dec2Bin(n)
        print(Result)
        length=len(Result)
        for i in range(length):
            if(Result[i]==0):
                Result[i]=1
            else:
                Result[i]=0
        print(Result)
        for i in range(1,len(Result)+1):
            #print("i = ",i)
            #print("resulti = ",Result[i])
            if(Result[-i]==1):
                Result[-i]=2**(i-1)
        Sum=sum(Result)
        return Sum        