# Last updated: 04/05/2026, 00:33:01
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1len=len(nums1)
        num2len=len(nums2)
        print(num1len,num2len)
        result=[]
        if(num1len<num2len):
            for i in range(num1len):
                #print(i)
                for j in range(num2len):
                    #print(j)
                    #print(nums2)
                    if(nums1[i]==nums2[j]):
                        nums2[j]=9999
                        result.append(nums1[i])
                        #print(nums2)
                        break
                    #print(nums2)
        else:
            for j in range(num2len):
                for i in range(num1len):
                    #print(i,j)
                    if(nums1[i]==nums2[j]):
                        nums1[i]=9999
                        result.append(nums2[j])
                        #print(nums2)
                        break
                    #print(nums2)
                    
                    
        return result