# Last updated: 04/05/2026, 00:33:44
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]: #4,3,2,1,0
            if i + nums[i] >= goal:
                goal = i
        return not goal