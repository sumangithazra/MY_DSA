# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        lh=self.LeftHeight(root.left)
        rh=self.RightHeight(root.right)
        if lh==rh: return 2**(lh+1) -1
        else: 
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
    def LeftHeight(self,node):
        height=0
        while node:
            height+=1
            node=node.left
        return height
    def RightHeight(self,node):
        height=0
        while node:
            height+=1
            node=node.right
        return height
        