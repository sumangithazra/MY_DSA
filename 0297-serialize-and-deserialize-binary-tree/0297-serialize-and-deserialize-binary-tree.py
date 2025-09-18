# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        queue=deque()
        queue.append(root)
        res=[]
        while queue:
            node=queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('#')
        return ",".join(res)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        nodes=data.split(',')
        root=TreeNode(int(nodes[0]))
        i=1
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            if nodes[i]!='#':
                node.left=TreeNode(nodes[i])
                queue.append(node.left)
            i+=1
            if nodes[i]!='#':
                node.right=TreeNode(nodes[i])
                queue.append(node.right)
            i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))