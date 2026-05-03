# Last updated: 04/05/2026, 00:34:03
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #When index is not asked . (only True and False)
        
#         l,r=0,len(nums)-1
#         nums.sort()
#         result=[]
        
#         while l<r:
#             sum=nums[r]+nums[l]
#             if(sum==target):
#                 return [l,r]
#             if(sum>target):
#                 r=r-1
#             else:
#                 l=l+1
#         return result
        seen = {}
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2

            if remaining in seen: #3
                return [i, seen[remaining]]  #4
            else:
                seen[value] = i  #5