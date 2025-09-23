from typing import Optional,List
from inorder_traversal import TreeNode
import unittest

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q:Optional[TreeNode])->bool:
        a = self.traversal(p)
        b = self.traversal(q)
        return a == b

    def traversal(self, p: Optional[TreeNode])->List[int]:
        if not p:
            return [None]
        
        res = [p.val]
        res.extend(self.traversal(p.left))
        res.extend(self.traversal(p.right))
        return res


class TestIsSameTree(unittest.TestCase):
    def setUp(self):
        self.sln = Solution()

    def test_both_none(self):
        self.assertTrue(self.sln.isSameTree(None, None))

    def test_one_none_other_not(self):
        self.assertFalse(self.sln.isSameTree(TreeNode(1), None))
        self.assertFalse(self.sln.isSameTree(None, TreeNode(1)))

    def test_same_single_node(self):
        self.assertTrue(self.sln.isSameTree(TreeNode(1), TreeNode(1)))

    def test_different_single_node_values(self):
        self.assertFalse(self.sln.isSameTree(TreeNode(1), TreeNode(2)))

    def test_same_structure_and_values(self):
        #      2               2
        #     / \             / \
        #    1   3           1   3
        a = TreeNode(2)
        a.left = TreeNode(1)
        a.right = TreeNode(3)

        b = TreeNode(2)
        b.left = TreeNode(1)
        b.right = TreeNode(3)

        self.assertTrue(self.sln.isSameTree(a, b))

    def test_different_structure(self):
        # a:    1        b:   1
        #        \          /
        #         2        2
        a = TreeNode(1)
        a.right = TreeNode(2)

        b = TreeNode(1)
        b.left = TreeNode(2)

        self.assertFalse(self.sln.isSameTree(a, b))


if __name__ == "__main__":
    unittest.main()
