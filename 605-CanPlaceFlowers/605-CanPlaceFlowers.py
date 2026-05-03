# Last updated: 04/05/2026, 00:32:50
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        l=len(flowerbed)
        for i in range(0,len(flowerbed)):
            left=i-1
            right=i+1
            left_available=left<0 or flowerbed[left]==0
            right_available=right>=l or flowerbed[right]==0
            if flowerbed[i]==0 and left_available and right_available:
                count=count+1
                flowerbed[i]=1
        return count>=n

        