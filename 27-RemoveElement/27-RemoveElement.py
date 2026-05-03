# Last updated: 04/05/2026, 00:33:51
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length=len(nums)
        count=0
        for i in range(len(nums)):
            if(nums[i]==val):
                nums[i]=-1
                count=count+1
        nums.sort(reverse=True)
        return length-count
        
    
        
                