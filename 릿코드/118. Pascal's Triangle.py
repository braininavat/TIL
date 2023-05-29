class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        prev = []
        for i in range(1,numRows+1):
            prev =Solution.pascal(self,i,prev)
            triangle.append(prev)
        return triangle

    def pascal(self,row,prev):
        cur = []
        if row == 1:
            return [1]
        else:
            cur.append(1)
            for i in range(1,len(prev)):
                cur.append(prev[i-1]+prev[i])
            cur.append(1)
            return cur