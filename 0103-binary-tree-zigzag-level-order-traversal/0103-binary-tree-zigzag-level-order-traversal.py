# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        if not root: return []
        queue.append(root)
        LeftToRight=True
        final=[]
        while queue:
            size=len(queue)
            temp=[0]*size
            for i in range(size):
                elem=queue.popleft()
                indx=i if LeftToRight else size-i-1
                temp[indx]=elem.val
                if elem.left: queue.append(elem.left)
                if elem.right: queue.append(elem.right)
            LeftToRight=not LeftToRight
            final.append(temp)
        return final

        