# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return Solution.dfs(self,p,q)

    def dfs(self,curq,curp):
        res = False
        if curq is None or curp is None:
            if curq is None and curp is None:
                return True
            else:
                return False
        if curq.val == curp.val:
            res = True
        return res * Solution.dfs(self,curq.left,curp.left) * Solution.dfs(self,curq.right,curp.right)
        
