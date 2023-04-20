class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        
        if numRows == 1:
                end = 1
        elif numRows == 2:
            end = 2
        else:
            end = 2*numRows-2
        
        mapper = [[""] for _ in range(numRows)]
        
        for i in range(len(s)): 
            if i%end >= numRows:
                mapper[end-i%end].append(s[i])
            else:
                mapper[i%end].append(s[i])
                    
        res = ""
        for x in range(len(mapper)):
            for i in range(len(mapper[x])):
                res = res+ mapper[x][i]
                
        return res