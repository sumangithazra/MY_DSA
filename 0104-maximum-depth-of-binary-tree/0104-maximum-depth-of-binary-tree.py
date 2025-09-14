# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''if root==None:
            return 0
        l_height=self.maxDepth(root.left)
        r_height=self.maxDepth(root.right)
        return 1+max(l_height,r_height)'''
        if not root: return 0
        lh=self.maxDepth(root.left)
        rh=self.maxDepth(root.right)
        return 1+max(lh,rh)
        