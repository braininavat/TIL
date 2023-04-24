class Solution:
    def isValid(self, s: str) -> bool:
        cur = ""
        for idx in range(len(s)):
            if s[idx] in ['(','[','{']:
                cur  = cur + s[idx]
            else:
                if len(cur) == 0:
                    return False
                if s[idx] == ')':
                    if cur[-1] == '(':
                        cur = cur[:-1]
                    else:
                        return False
                elif s[idx] == ']':
                    if cur[-1] == '[':
                        cur = cur[:-1]
                    else:
                        return False
                elif s[idx] == '}':
                    if cur[-1] == '{':
                        cur = cur[:-1]
                    else:
                        return False

        if len(cur) != 0:
            return False
        else:
            return True
    
