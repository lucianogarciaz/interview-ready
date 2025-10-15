from inorder_traversal import TreeNode
from typing import Optional, List
from collections import deque
import unittest

class BSTIterator:
    def __init__(self, root:Optional[TreeNode]):
        self.stack: List[TreeNode] = []
        self.pushLeft(root)
    def pushLeft(self, node:Optional[TreeNode]):
        if not node:
            return
        self.stack.append(node)
        self.pushLeft(node.left)

    def next(self)->int:
        node = self.stack.pop()
        if node.right:
            self.pushLeft(node.right)
        return node.val

    def hasNext(self)->bool:
        return True if self.stack else False


class BSTIterator2:
    def __init__(self, root: Optional[TreeNode]):
        self.elements = deque([])
        self.buildBST(root, self.elements)

    def buildBST(self, root:Optional[TreeNode], res:List[int]):
        if not root:
            return
        self.buildBST(root.left, res)
        res.append(root.val)
        self.buildBST(root.right, res)
        
    def next(self) -> int:
        el = self.elements.popleft()
        return el

    def hasNext(self) -> bool:
        return True if self.elements else False




class TestBSTIterator(unittest.TestCase):
    def test_basic_bst(self):
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)
        
        iterator = BSTIterator(root)
        
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 7)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 9)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 15)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 20)
        self.assertFalse(iterator.hasNext())

    def test_single_node(self):
        root = TreeNode(1)
        iterator = BSTIterator(root)
        
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 1)
        self.assertFalse(iterator.hasNext())

    def test_left_skewed_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(1)
        
        iterator = BSTIterator(root)
        
        self.assertEqual(iterator.next(), 1)
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 4)
        self.assertEqual(iterator.next(), 5)
        self.assertFalse(iterator.hasNext())

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        
        iterator = BSTIterator(root)
        
        self.assertEqual(iterator.next(), 1)
        self.assertEqual(iterator.next(), 2)
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 4)
        self.assertFalse(iterator.hasNext())

    def test_balanced_bst(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        
        iterator = BSTIterator(root)
        
        expected = [1, 2, 3, 4, 5, 6, 7]
        for val in expected:
            self.assertTrue(iterator.hasNext())
            self.assertEqual(iterator.next(), val)
        
        self.assertFalse(iterator.hasNext())

    def test_hasNext_multiple_calls(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        
        iterator = BSTIterator(root)
        
        self.assertTrue(iterator.hasNext())
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 1)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 2)
        self.assertTrue(iterator.hasNext())
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 3)
        self.assertFalse(iterator.hasNext())
        self.assertFalse(iterator.hasNext())

    def test_inorder_property(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(7)
        root.right.right = TreeNode(20)
        
        iterator = BSTIterator(root)
        
        result = []
        while iterator.hasNext():
            result.append(iterator.next())
        
        self.assertEqual(result, [2, 5, 7, 10, 15, 20])
        for i in range(len(result) - 1):
            self.assertLess(result[i], result[i + 1])


if __name__ == '__main__':
    unittest.main()