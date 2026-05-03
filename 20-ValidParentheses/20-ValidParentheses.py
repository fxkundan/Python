# Last updated: 04/05/2026, 00:33:55
class Solution:
    def isValid(self, s: str) -> bool:
    
        stack = []
    
        for i in s:
            if i in ('(', '{', '['): 
                stack.append(i)

            else:

                if stack == []: 
                    return False

                elif i == ')' and stack[-1] == '(': 
                    stack.pop(-1)

                elif i == '}' and stack[-1] == '{':
                    stack.pop(-1)

                elif i == ']' and stack[-1] == '[':
                    stack.pop(-1)

                else:
                    return False

        if stack == []: 
            return True

        else: 
            return False