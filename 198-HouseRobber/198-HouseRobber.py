# Last updated: 04/05/2026, 00:33:15
class Solution:
    def rob(self, nums: List[int]) -> int:
        length=len(nums)
        result=[0]*length
        result[0]=nums[0]
        if(length>=2):
            result[1]=max(nums[0],nums[1])
        for i in range(2,length):
            result[i]=max(result[i-1],result[i-2]+nums[i])
        return result[length-1]