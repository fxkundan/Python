# Last updated: 04/05/2026, 00:32:29
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            result.append(total)
        return result