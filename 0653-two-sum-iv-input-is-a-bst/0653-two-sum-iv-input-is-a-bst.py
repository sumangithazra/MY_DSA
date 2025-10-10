# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums=[]
        def inorder(node):
            if not node: return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        i=0
        j=len(nums)-1
        while i<j:
            sumi=nums[i]+nums[j]
            if sumi==k:
                return True
            elif sumi<k:i+=1
            else: j-=1
        return False        