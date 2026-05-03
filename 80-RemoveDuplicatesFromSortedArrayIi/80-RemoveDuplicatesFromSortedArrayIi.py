# Last updated: 04/05/2026, 00:33:35
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i+2<len(nums):
            if nums[i]==nums[i+2]:
                nums.pop(i+2)
            else:
                i=i+1
        return len(nums)