# Last updated: 04/05/2026, 00:33:27
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn, mx = float('inf'), 0
        for i in range(len(prices)):
            mn= min(prices[i],mn)
            mx= max(mx, prices[i]-mn)
        return mx
        