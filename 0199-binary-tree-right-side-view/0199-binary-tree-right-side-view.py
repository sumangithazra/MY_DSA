# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue=deque()
        ans=[]
        queue.append(root)
        while queue:
            size=len(queue)
            for i in range(size):
                elem=queue.popleft()
                if i==size-1: ans.append(elem.val)
                if elem.left: queue.append(elem.left)
                if elem.right: queue.append(elem.right)
        return ans

        