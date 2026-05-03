# Last updated: 04/05/2026, 00:32:44
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length=len(arr)
        maximum=max(arr)
        maxindex=0
        flag=0
        if(length < 3):
            return False
        if(arr[length-1]==maximum):
            return False
        if(arr[0]==maximum):
            return False
        for i in range(length):
            if(arr[i]==maximum):
                maxindex=i
        for i in range(maxindex):
            if(arr[i]<arr[i+1]):
                flag=1
            else:
                flag=0
                return False
        for i in range(maxindex,length-1):
            if(arr[i]>arr[i+1]):
                flag=1
            else:
                flag=0
                return False
        if(flag==1):
            return True 
        else:
            return False
            
                