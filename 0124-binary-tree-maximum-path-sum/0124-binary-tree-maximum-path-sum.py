# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=-float('inf')
        self.max_path(root)
        return self.maxi
    def max_path(self,node):
        if not node: return 0
        l_sum=max(0,self.max_path(node.left))
        r_sum=max(0,self.max_path(node.right))
        self.maxi=max(self.maxi,node.val+l_sum+r_sum)
        return node.val+max(l_sum,r_sum)

        