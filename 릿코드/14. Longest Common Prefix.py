class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        result = ""
        
        length = min(len(first),len(last))
        
        for i in range(length):
            if(first[i] == last[i]):
                result = result + first[i]
            else: break
            
        return result
