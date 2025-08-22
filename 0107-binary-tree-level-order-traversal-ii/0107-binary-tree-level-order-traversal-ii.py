# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None: return []
        result=[]
        queue=[]
        queue.append(root)
        while queue:
            level=[]
            n=len(queue)
            for i in range(n):
                top=queue.pop(0)
                level.append(top.val)
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)

            result.append(level)
        return result[::-1]




        