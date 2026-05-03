# Last updated: 04/05/2026, 00:33:46
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        temp_max = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]>temp_max+nums[i]):
                temp_max=nums[i]
            else:
                temp_max=temp_max+nums[i]
            if(temp_max> max):
                max=temp_max
                 
        return max