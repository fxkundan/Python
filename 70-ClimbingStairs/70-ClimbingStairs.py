# Last updated: 04/05/2026, 00:33:38
class Solution:
    def climbStairs(self, n: int) -> int:
        x=1
        y=2
        if n<1:
            print("Invalid Input")
        elif n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        for i in range(2,n):
            z=x+y
            x=y
            y=z
        return y