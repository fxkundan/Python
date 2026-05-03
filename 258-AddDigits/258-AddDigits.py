# Last updated: 04/05/2026, 00:33:08
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0 : return 0
        if num % 9 == 0 : return 9
        else : return (num % 9)