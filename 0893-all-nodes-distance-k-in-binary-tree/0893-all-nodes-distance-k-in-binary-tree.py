# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent={}
        def dfs(node, par=None):
            if not node:
                return
            parent[node]=par
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root)
        queue=deque()
        ans=[]
        queue.append((target,0))
        visited=set()
        visited.add(target)
        while queue:
            node,dist=queue.popleft()
            if dist==k:
                ans.append(node.val)
            elif dist>k:
                break
            for nbr in (node.left,node.right,parent[node]):
                if nbr and nbr not in visited:
                    visited.add(nbr)
                    queue.append((nbr,dist+1))
        return ans
        
        