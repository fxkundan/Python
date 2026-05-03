# Last updated: 04/05/2026, 00:32:32
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        m=max(candies)
        for number in candies:
            res.append(number+extraCandies>=m)
        return res