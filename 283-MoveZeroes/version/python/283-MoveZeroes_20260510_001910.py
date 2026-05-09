# Last updated: 10/05/2026, 00:19:10
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        l=len(nums)
7        for i in range(l):
8            if nums[i]==0:
9                for j in range(i+1,l):
10                    if nums[j] !=0:
11                        temp=nums[j]
12                        nums[j]=nums[i]
13                        nums[i]=temp
14                        break
15        return nums
16