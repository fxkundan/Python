# Last updated: 04/05/2026, 00:33:37
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #return nums.sort()
        '''
        count=0
        temp=0
        for i in range(len(nums)):
            if(nums[i]==0):
                temp=nums[i]
                nums[i]=nums[count]
                nums[count]=temp
                count=count+1
        print(nums)
        print(count)
        for i in range(count,len(nums)):
            if(nums[i]==1):
                #print(count)
                temp=nums[i]
                nums[i]=nums[count]
                nums[count]=temp
                count=count+1
        print(nums)
        print(count)
        for i in range(count,len(nums)):
            if(nums[i==2]):
                temp=nums[i]
                nums[i]=nums[count]
                nums[count]=temp
                count=count+1
        print(nums)
        print(count)
        return nums
    '''
        
        count1=0
        length=len(nums)
        i=0
        count2=length-1
        if(length<2):
            return None
        while(i<=count2):
            if(nums[i]==0):
                self.swap(i,count1,nums)
                i=i+1
                count1=count1+1
            elif(nums[i]==2):
                self.swap(i,count2,nums)
                count2=count2-1
            else:
                i=i+1
            
            
    def swap(self,i,j,nums):
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
            
        
                