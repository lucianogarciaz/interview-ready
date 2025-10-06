import unittest
from inorder_traversal import TreeNode
from typing import Optional

#     1
#   2   3
#  4 5 6 7
# 
# height = 0
#  
# 
class Solution:
    def checkBalanced(self, tree: Optional[TreeNode]) -> bool:
        if not tree:
            return True
        result, _ = self.dfs(tree)
        return result
    
    def dfs(self, tree: Optional[TreeNode])->tuple[bool, int]:
        if not tree:
            return True, 0

        leftBal,l = self.dfs(tree.left)
        rightBal,r = self.dfs(tree.right)

        if not rightBal or not leftBal:
            return False, 0
        
        return abs(r-l)<=1, max(r,l)+1


class TestCheckBalanced(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Empty tree should be balanced"""
        self.assertTrue(self.solution.checkBalanced(None))

    def test_single_node(self):
        """Single node tree should be balanced"""
        root = TreeNode(1)
        self.assertTrue(self.solution.checkBalanced(root))

    def test_two_nodes_balanced(self):
        """Two nodes in a line should be balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertTrue(self.solution.checkBalanced(root))

    def test_three_nodes_perfect(self):
        """Perfect binary tree with 3 nodes should be balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertTrue(self.solution.checkBalanced(root))

    def test_three_nodes_unbalanced(self):
        """Tree with 3 nodes in a line should be balanced (height diff = 1)"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertFalse(self.solution.checkBalanced(root))

    def test_four_nodes_unbalanced(self):
        """Tree with 4 nodes where left subtree has height 2 and right has height 0"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        self.assertFalse(self.solution.checkBalanced(root))

    def test_skewed_tree(self):
        """Completely skewed tree should not be balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.left.left = TreeNode(5)
        self.assertFalse(self.solution.checkBalanced(root))

    def test_complex_balanced_tree(self):
        """Complex tree that is balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertTrue(self.solution.checkBalanced(root))

    def test_complex_unbalanced_tree(self):
        """Complex tree that is not balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.left.left = TreeNode(5)
        root.left.left.right = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertFalse(self.solution.checkBalanced(root))

    def test_minimal_unbalanced(self):
        """Minimal case where tree becomes unbalanced"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(5)
        self.assertFalse(self.solution.checkBalanced(root))

    def test_right_skewed_unbalanced(self):
        """Right-skewed tree should not be balanced"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        self.assertFalse(self.solution.checkBalanced(root))

    def test_height_difference_exactly_one(self):
        """Tree where height difference is exactly 1 should be balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertTrue(self.solution.checkBalanced(root))

    def test_height_difference_two(self):
        """Tree where height difference is 2 should not be balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.right = TreeNode(5)
        self.assertFalse(self.solution.checkBalanced(root))

    def test_large_balanced_tree(self):
        """Large balanced tree"""
        # Create a tree with 4 levels, perfectly balanced
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(11)
        root.right.left.left = TreeNode(12)
        root.right.left.right = TreeNode(13)
        root.right.right.left = TreeNode(14)
        root.right.right.right = TreeNode(15)
        self.assertTrue(self.solution.checkBalanced(root))


if __name__ == "__main__":
    unittest.main()
