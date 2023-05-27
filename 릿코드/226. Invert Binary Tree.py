# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        if cur is not None:
            Solution.visit(self,cur)
        return root
        
    def visit(self,cur):
        #change nodes
        tmp = cur.left
        cur.left = cur.right
        cur.right= tmp
    
        if cur.left:
            Solution.visit(self,cur.left)
        if cur.right:
            Solution.visit(self,cur.right)

        if cur.left is None and cur.right is None:
            return