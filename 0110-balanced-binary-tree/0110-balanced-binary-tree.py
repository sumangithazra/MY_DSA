# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_balance(root)!=-1

    def check_balance(self,root):
        if not root:
            return 0
        lh=self.check_balance(root.left)
        rh=self.check_balance(root.right)
        if abs(lh-rh)>1: return -1
        if lh==-1: return -1
        if rh==-1: return -1
        return 1+max(lh,rh)
        '''if root==None: return 0
        l_height=self.check_balance(root.left)
        r_height=self.check_balance(root.right)
        if l_height==-1 or r_height==-1: return -1
        if abs(l_height-r_height)>1: return -1
        return 1+max(l_height,r_height)'''
        