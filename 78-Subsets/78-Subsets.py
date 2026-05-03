# Last updated: 04/05/2026, 00:33:36
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            for i in range(len(result)):
                result.append(result[i]+[n])
        return result
