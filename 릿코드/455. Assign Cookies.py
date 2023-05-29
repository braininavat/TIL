class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        res = 0
        cur =0
        for i in range(len(g)):
            if cur == len(s):
                break
            for j in range(cur,len(s)):
                cur += 1
                if s[j] >= g[i]:
                    res += 1
                    break
                

        return res