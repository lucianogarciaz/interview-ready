from typing import Optional,List
from inorder_traversal import TreeNode
import unittest

class Solution:
    def isSimetric(self, root: Optional[TreeNode])->bool:
        if not root:
            return True
        a = self.traversal(root.left)
        b = self.traversalMirror(root.right)
        return a == b

    def traversal(self, root:Optional[TreeNode])->List[int]:
        if not root:
            return [None]
        res = [root.val]
        res.extend(self.traversal(root.left))
        res.extend(self.traversal(root.right))
        return res

    def traversalMirror(self, root:Optional[TreeNode])->List[int]:
        if not root:
            return [None]
        
        res = [root.val]
        res.extend(self.traversalMirror(root.right))
        res.extend(self.traversalMirror(root.left))
        return res


class TestIsSimetricTree(unittest.TestCase):
    def setUp(self):
        self.sln = Solution()

    def test_empty_tree_is_symmetric(self):
        self.assertTrue(self.sln.isSimetric(None))

    def test_single_node_is_symmetric(self):
        self.assertTrue(self.sln.isSimetric(TreeNode(1)))

    def test_symmetric_tree(self):
        #        1
        #      /   \
        #     2     2
        #    / \   / \
        #   3   4 4   3
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), TreeNode(4))
        root.right = TreeNode(2, TreeNode(4), TreeNode(3))
        self.assertTrue(self.sln.isSimetric(root))

    def test_asymmetric_values(self):
        #        1
        #      /   \
        #     2     2
        #      \      \
        #       3      3 (but one side missing a mirror node)
        root = TreeNode(1)
        root.left = TreeNode(2, None, TreeNode(3))
        root.right = TreeNode(2, None, TreeNode(3))
        self.assertFalse(self.sln.isSimetric(root))

    def test_asymmetric_structure(self):
        #        1
        #      /   \
        #     2     2
        #    /         \
        #   3           3
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), None)
        root.right = TreeNode(2, None, TreeNode(3))
        # This is actually symmetric; modify to break symmetry
        root.right.right = TreeNode(4)
        self.assertFalse(self.sln.isSimetric(root))


if __name__ == "__main__":
    unittest.main()