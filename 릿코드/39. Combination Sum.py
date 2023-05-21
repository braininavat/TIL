import copy
class Solution:
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        res = []
        def backtrack(now, idx):
            tot = sum(now)
            if tot == target:
                res.append(now)
            elif tot < target:
                for i in range(idx,len(candidates)):
                    backtrack(now+[candidates[i]],i)
        backtrack([],0)
        return res
    
        
            
            
print(Solution.combinationSum(Solution,[2,3,6,7],7))