# Last updated: 04/05/2026, 00:32:28
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = ([sum(x) for x in accounts])
        return max(res)