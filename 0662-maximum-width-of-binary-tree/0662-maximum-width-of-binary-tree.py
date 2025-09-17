# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        max_width=0
        queue=deque()
        queue.append((root,0))
        while queue:
            size=len(queue)
            _,mini=queue[0]
            first=0
            last=0
            for i in range(size):
                node,indx=queue.popleft()
                indx=indx-mini
                if i==0: first=indx
                if i==size-1: last=indx
                if node.left: queue.append((node.left,(2*indx)+1))
                if node.right: queue.append((node.right,(2*indx)+2))
            max_width=max(max_width,last-first+1)
        return max_width
        