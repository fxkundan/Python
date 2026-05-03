# Last updated: 04/05/2026, 00:32:49
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_weight_on_left, total_weight_on_right = 0, sum(nums)

        for index, current_weight in enumerate(nums):

            total_weight_on_right -= current_weight

            if total_weight_on_left == total_weight_on_right:
                return index

            total_weight_on_left += current_weight

        return -1