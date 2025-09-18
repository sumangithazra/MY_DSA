# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={val:idx for idx,val in enumerate(inorder)}
        self.preorder_idx=0
        def Helper(left,right):
            if left>right: return None
            root_val=preorder[self.preorder_idx]
            root=TreeNode(root_val)
            self.preorder_idx+=1
            mid=inorder_map[root_val]
            root.left=Helper(left,mid-1)
            root.right=Helper(mid+1,right)
            return root
        return Helper(0,len(inorder)-1)
