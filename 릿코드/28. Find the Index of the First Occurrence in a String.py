class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack)
        nedlen = len(needle)
        
        if haylen < nedlen: return -1
        
        for i in range(haylen-nedlen):
            if haystack[i] == needle[0]:
                for j in range(nedlen):
                    if haystack[i+j] != needle[j]:
                        i = i + j -1
                        break;
                    if j == nedlen-1:
                        return i
        
        return -1
    
print(Solution.strStr(Solution,"a","a"))
            
        