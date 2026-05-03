# Last updated: 04/05/2026, 00:33:16
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''for x in range(k):
            previous = nums[-1]
            for i in range(len(nums)):
                temp = nums[i]
                nums[i] = previous
                previous = temp
        print(nums)'''
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
            
        