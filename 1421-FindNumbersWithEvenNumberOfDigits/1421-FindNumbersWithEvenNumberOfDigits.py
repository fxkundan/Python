# Last updated: 04/05/2026, 00:32:33
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numLen=len(nums)
        final=0
        for i in range(numLen):
            count =1 
            while(nums[i]>=10):
                nums[i]/=10
                count=count+1
            if(count%2==0):
                final=final+1
        return final