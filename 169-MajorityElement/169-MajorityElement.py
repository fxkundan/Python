# Last updated: 04/05/2026, 00:33:18
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]
    
        count = 0
        majorElement = None
        for num in nums:
            if count == 0:
                majorElement = num
            count += 1 if majorElement == num else -1
        return majorElement
        