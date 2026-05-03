# Last updated: 04/05/2026, 00:32:38
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # l1=len(str1)
        # l2=len(str2)
        # if str1==str2:
        #     return str2
        # if str1+str2==str2+str1:
        #    lgc= math.gcd(l1,l2)
        #    return str2[0:lgc]
        # else:
        #     return ""   

        if (str1 + str2 != str2 + str1):
            return ''
        a = len(str1)
        b = len(str2)
        while (b):
            temp = b
            b = a % b
            a = temp
        return str1[0:a]

        