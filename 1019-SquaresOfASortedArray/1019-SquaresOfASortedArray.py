# Last updated: 04/05/2026, 00:32:43
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numsLen=len(nums)
        for i in range(numsLen):
            nums[i]=nums[i]**2
            
        nums.sort()
        return nums