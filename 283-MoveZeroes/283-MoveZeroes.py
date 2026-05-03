# Last updated: 04/05/2026, 00:33:05
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        for i in range(length):
            if(nums[i]==0):
                for j in range(i+1,length):
                    if nums[j] is not 0:
                        temp=nums[j]
                        nums[j]=nums[i]
                        nums[i]=temp
                        break
        return nums