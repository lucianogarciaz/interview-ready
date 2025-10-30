# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
      1
    2   3
  4  5

  '1,2,4,nul,nul,5,nul,nul,3,nul,nul'  

    """
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return 'nul'
        res = f'{root.val}'
        res += ','+self.serialize(root.left)
        res += ','+self.serialize(root.right)
        return res
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        arr = deque(data.split(','))
        return self._des(arr)
    
    def _des(self, data)->Optional[TreeNode]:
        if not data:
            return None
        if data[0]=='nul':
            data.popleft()
            return None
        
        val = data.popleft()
        node = TreeNode(int(val))
        node.left = self._des(data)
        node.right = self._des(data)
        return node
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans