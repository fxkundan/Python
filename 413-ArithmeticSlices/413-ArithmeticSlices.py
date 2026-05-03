# Last updated: 04/05/2026, 00:32:56
class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         i=0
#         j=1
#         length=len(nums)
#         count=0
        
#         for i in range(length-2):
#             t=i+2
#             diff=nums[i]-nums[i+1]
#             print(diff)
#             for j in range(t,length):
#                 # print("j",j)
#                 # print("in j",nums[j-1]-nums[j])
#                 if(diff==(nums[j-1]-nums[j])):
#                     count=count+1
#                 else:
#                     break
        
#         return count
        def numberOfArithmeticSlices(self, A: List[int]) -> int:
            le=len(A)
            l=[0]*(le)
            for i in range(2,le):
                if A[i]-A[i-1] == A[i-1]-A[i-2]:
                    l[i]=1+l[i-1]
            return sum(l)
            
        