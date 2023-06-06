class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curlist,cur):
            if len(curlist) == 0:
                res.append(cur)
            else:
                for i in range(0,len(curlist)):
                    dfs(curlist[:i]+curlist[i+1:],cur+[curlist[i]])

        dfs(nums,[])
        return res