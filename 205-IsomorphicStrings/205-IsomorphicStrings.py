# Last updated: 04/05/2026, 00:33:14
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        if len(set(s)) != len(set(t)):
            return False
        for char in range(len(t)):
            if t[char] not in hash_map:
                hash_map[t[char]] = s[char]
            elif hash_map[t[char]] != s[char]:
                return False
        return True
        