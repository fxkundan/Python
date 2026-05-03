# Last updated: 04/05/2026, 00:32:51
class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         l1=len(s1)
#         l2=len(s2)
#         temp=dict()
#         count=0
        
#         if(l1>l2):
#             return False
#         for i in range(l1):
#             if s1[i] in temp:
#                 temp[s1[i]]=temp[s1[i]]+1
#             else:
#                 temp[s1[i]]=1
                
#         while j<=l2
#             if(s2[j] in temp and temp[s2[j]]>=1):
#                 temp[s2[j]]=temp[s2[j]]-1
#                 count=count+1
#             else:
#                 count=0
#             if(count==l1):
#                      return True
            
#         return False
            
        
        def checkInclusion(self, s1: str, s2: str) -> bool:
            counter = Counter(s1)
            for i in range(len(s2)-len(s1)+1):
                if Counter(s2[i:i+len(s1)]) == counter: return True
            return False
        
        