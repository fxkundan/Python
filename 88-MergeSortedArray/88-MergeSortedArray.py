# Last updated: 04/05/2026, 00:33:34
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2:
            i = j = 0
            while i < m and j < n:
                if nums1[i] > nums2[j]:
                    nums1.insert(i, nums2[j])
                    j+=1
                    m+=1
                i+=1
            if j < n:
                nums1[m:] = nums2[j:]
            else:
                del nums1[-n:]
            
        