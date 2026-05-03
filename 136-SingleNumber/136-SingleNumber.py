# Last updated: 04/05/2026, 00:33:24
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            ans=ans^nums[i]
        return ans
    