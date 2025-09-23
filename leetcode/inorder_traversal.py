from typing import List, Optional
import unittest

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def inorderTraversal(self, root:Optional[TreeNode])->List[int]:
        if not root:
            return []
        
        res = self.inorderTraversal(root.left)
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res
    def postorderTraversal(self, root:Optional[TreeNode])->List[int]:
        if not root:
            return []
        res = self.postorderTraversal(root.left)
        res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res

    def preorderTraversal(self,root:Optional[TreeNode])->List[int]:
        if not root:
            return []
        res = [root.val]
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res


class TestInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.sln = Solution()

    def test_empty_tree_returns_empty_list(self):
        self.assertEqual(self.sln.inorderTraversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.sln.inorderTraversal(root), [1])

    def test_inorder_balanced_tree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(self.sln.inorderTraversal(root), [1, 2, 3])

    def test_inorder_unbalanced_left(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        self.assertEqual(self.sln.inorderTraversal(root), [1, 2, 3])

    def test_inorder_unbalanced_right(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.sln.inorderTraversal(root), [1, 2, 3])


class TestPreorderTraversal(unittest.TestCase):
    def setUp(self):
        self.sln = Solution()

    def test_empty_tree_returns_empty_list(self):
        self.assertEqual(self.sln.preorderTraversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.sln.preorderTraversal(root), [1])

    def test_preorder_balanced_tree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(self.sln.preorderTraversal(root), [2, 1, 3])

    def test_preorder_unbalanced_left(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        self.assertEqual(self.sln.preorderTraversal(root), [3, 2, 1])

    def test_preorder_unbalanced_right(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.sln.preorderTraversal(root), [1, 2, 3])


class TestPostorderTraversal(unittest.TestCase):
    def setUp(self):
        self.sln = Solution()

    def test_empty_tree_returns_empty_list(self):
        self.assertEqual(self.sln.postorderTraversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.sln.postorderTraversal(root), [1])

    def test_postorder_balanced_tree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(self.sln.postorderTraversal(root), [1, 3, 2])

    def test_postorder_unbalanced_left(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        self.assertEqual(self.sln.postorderTraversal(root), [1, 2, 3])

    def test_postorder_unbalanced_right(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.sln.postorderTraversal(root), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
