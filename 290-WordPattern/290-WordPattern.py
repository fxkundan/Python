# Last updated: 04/05/2026, 00:33:04
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        result={}
        if(len(pattern) != len(words)):
            return False
        else:
            for i in range(len(words)):
                if pattern[i] not in result:
                    if words[i] in result.values():
                        return False
                    result[pattern[i]]=words[i]
                else:
                    if result[pattern[i]] != words[i]:
                        return False
        return True
                    
                