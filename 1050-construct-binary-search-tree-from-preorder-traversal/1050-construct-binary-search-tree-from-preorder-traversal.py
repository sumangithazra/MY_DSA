# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.idx=0
        return self.Build(preorder,float('inf'))
    def Build(self,preorder,bound):
        if self.idx==len(preorder) or preorder[self.idx]>bound: return None
        root=TreeNode(preorder[self.idx])
        self.idx+=1
        root.left=self.Build(preorder,root.val)
        root.right=self.Build(preorder,bound)
        return root       