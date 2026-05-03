# Last updated: 04/05/2026, 00:33:17
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
            alphabet = {chr(ord('A') + i) :1 + i for i in range(26)}
            #print(alphabet)
            length=len(columnTitle)
            value=0
            for i in range(length):
                value=value+ 26**(length-i-1)*alphabet[columnTitle[i]]
            return value
            