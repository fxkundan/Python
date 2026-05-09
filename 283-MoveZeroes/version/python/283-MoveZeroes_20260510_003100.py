# Last updated: 10/05/2026, 00:31:00
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        count=0
7        res=[]
8        for number in nums:
9            if number !=0:
10                res.append(number)
11            else:
12                count=count+1
13        for i in range(len(res)):
14            nums[i]=res[i]
15        for i in range(len(res),len(nums)):
16            nums[i]=0
17        return nums
18