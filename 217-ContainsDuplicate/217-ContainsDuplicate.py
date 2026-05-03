# Last updated: 04/05/2026, 00:33:11
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
            
            
        
        