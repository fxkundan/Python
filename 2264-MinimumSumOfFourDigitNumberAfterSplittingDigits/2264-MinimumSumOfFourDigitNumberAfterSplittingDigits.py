# Last updated: 04/05/2026, 00:32:21
class Solution:
    def minimumSum(self, num: int) -> int:
        sl = sorted(list(str(num)))
        return(int(sl[0] + sl[3])+int(sl[1] + sl[2]))