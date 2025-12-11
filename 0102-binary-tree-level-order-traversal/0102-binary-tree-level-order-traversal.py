# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        ans=[]
        queue=[]
        queue.append(root)
        while queue:
            level=[]
            n=len(queue)
            for _ in range(n):
                node=queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans
        '''if not root:
            return []
        result=[]
        queue=[]
        queue.append(root)
        while queue:
            level=[]
            size=len(queue)
            for _ in range(size):
                node=queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result'''
            
