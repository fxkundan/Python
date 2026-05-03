# Last updated: 04/05/2026, 00:33:06
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        return (l*(l+1))//2 -(sum(nums))
    
        