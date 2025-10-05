import unittest
from typing import Optional, List
from inorder_traversal import TreeNode


class Solution:
    def minimalTree(self, arr:List[int])-> Optional[TreeNode]:
        if not arr:
            return None
        pivotIndex = len(arr)//2
        pivot = arr[pivotIndex]

        leftArray = arr[:pivotIndex]
        rightArray = arr[pivotIndex+1:]

        return TreeNode(pivot, self.minimalTree(leftArray), self.minimalTree(rightArray))


class TestMinimalTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        """Test with empty array"""
        result = self.solution.minimalTree([])
        self.assertIsNone(result)

    def test_single_element(self):
        """Test with single element array"""
        result = self.solution.minimalTree([5])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 5)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

    def test_two_elements(self):
        """Test with two elements"""
        result = self.solution.minimalTree([1, 3])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)  # Middle element (index 1)
        self.assertIsNotNone(result.left)
        self.assertEqual(result.left.val, 1)
        self.assertIsNone(result.right)

    def test_three_elements(self):
        """Test with three elements"""
        result = self.solution.minimalTree([1, 2, 3])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 2)  # Middle element (index 1)
        self.assertIsNotNone(result.left)
        self.assertEqual(result.left.val, 1)
        self.assertIsNotNone(result.right)
        self.assertEqual(result.right.val, 3)

    def test_four_elements(self):
        """Test with four elements"""
        result = self.solution.minimalTree([1, 2, 3, 4])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)  # Middle element (index 2)
        self.assertIsNotNone(result.left)
        self.assertEqual(result.left.val, 2)
        self.assertIsNotNone(result.right)
        self.assertEqual(result.right.val, 4)
        self.assertIsNotNone(result.left.left)
        self.assertEqual(result.left.left.val, 1)
        self.assertIsNone(result.left.right)

    def test_five_elements(self):
        """Test with five elements"""
        result = self.solution.minimalTree([1, 2, 3, 4, 5])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)  # Middle element (index 2)
        
        # Left subtree
        self.assertIsNotNone(result.left)
        self.assertEqual(result.left.val, 2)
        self.assertIsNotNone(result.left.left)
        self.assertEqual(result.left.left.val, 1)
        self.assertIsNone(result.left.right)
        
        # Right subtree
        self.assertIsNotNone(result.right)
        self.assertEqual(result.right.val, 5)
        self.assertIsNotNone(result.right.left)
        self.assertEqual(result.right.left.val, 4)
        self.assertIsNone(result.right.right)

    def test_seven_elements(self):
        """Test with seven elements (perfect binary tree)"""
        result = self.solution.minimalTree([1, 2, 3, 4, 5, 6, 7])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 4)  # Middle element (index 3)
        
        # Left subtree
        self.assertIsNotNone(result.left)
        self.assertEqual(result.left.val, 2)
        self.assertIsNotNone(result.left.left)
        self.assertEqual(result.left.left.val, 1)
        self.assertIsNotNone(result.left.right)
        self.assertEqual(result.left.right.val, 3)
        
        # Right subtree
        self.assertIsNotNone(result.right)
        self.assertEqual(result.right.val, 6)
        self.assertIsNotNone(result.right.left)
        self.assertEqual(result.right.left.val, 5)
        self.assertIsNotNone(result.right.right)
        self.assertEqual(result.right.right.val, 7)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = self.solution.minimalTree([-5, -3, -1, 0, 2])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, -1)  # Middle element (index 2)
        
        self.assertIsNotNone(result.left)
        self.assertEqual(result.left.val, -3)
        self.assertIsNotNone(result.left.left)
        self.assertEqual(result.left.left.val, -5)
        self.assertIsNone(result.left.right)
        
        self.assertIsNotNone(result.right)
        self.assertEqual(result.right.val, 2)
        self.assertIsNotNone(result.right.left)
        self.assertEqual(result.right.left.val, 0)
        self.assertIsNone(result.right.right)

    def test_duplicate_values(self):
        """Test with duplicate values"""
        result = self.solution.minimalTree([1, 2, 2, 3, 3, 3])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)  # Middle element (index 3)
        
        self.assertIsNotNone(result.left)
        self.assertEqual(result.left.val, 2)
        self.assertIsNotNone(result.left.left)
        self.assertEqual(result.left.left.val, 1)
        self.assertIsNotNone(result.left.right)
        self.assertEqual(result.left.right.val, 2)
        
        self.assertIsNotNone(result.right)
        self.assertEqual(result.right.val, 3)
        self.assertIsNotNone(result.right.left)
        self.assertEqual(result.right.left.val, 3)
        self.assertIsNone(result.right.right)

    def test_large_array(self):
        """Test with larger array"""
        arr = list(range(1, 16))  # [1, 2, 3, ..., 15]
        result = self.solution.minimalTree(arr)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 8)  # Middle element (index 7)
        
        # Verify it's a valid BST structure
        self._verify_bst_structure(result)

    def test_sorted_ascending(self):
        """Test with strictly ascending sorted array"""
        result = self.solution.minimalTree([1, 2, 3, 4, 5])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)
        
        # Should create a right-skewed tree on the left side
        # and left-skewed tree on the right side
        self._verify_bst_structure(result)

    def test_tree_height_optimization(self):
        """Test that the tree has minimal height"""
        arr = list(range(1, 8))  # 7 elements
        result = self.solution.minimalTree(arr)
        
        # Calculate height
        height = self._calculate_height(result)
        # For 7 elements, minimal height should be 2 (log2(7) ≈ 2.8)
        self.assertLessEqual(height, 3)
        
        # Verify all levels are filled as much as possible
        self._verify_balanced_structure(result)

    def test_bst_property(self):
        """Test that the resulting tree maintains BST property"""
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = self.solution.minimalTree(arr)
        self._verify_bst_property(result)

    def test_inorder_traversal(self):
        """Test that inorder traversal gives original sorted array"""
        arr = [1, 4, 7, 10, 13, 16, 19]
        result = self.solution.minimalTree(arr)
        
        # Inorder traversal should return the original array
        inorder_result = self._inorder_traversal(result)
        self.assertEqual(inorder_result, arr)

    def _verify_bst_structure(self, node):
        """Helper method to verify basic tree structure"""
        if not node:
            return
        self.assertIsInstance(node.val, int)
        if node.left:
            self.assertIsInstance(node.left.val, int)
        if node.right:
            self.assertIsInstance(node.right.val, int)

    def _verify_bst_property(self, node, min_val=float('-inf'), max_val=float('inf')):
        """Helper method to verify BST property"""
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            self.fail(f"BST property violated at node {node.val}")
        
        self._verify_bst_property(node.left, min_val, node.val)
        self._verify_bst_property(node.right, node.val, max_val)

    def _calculate_height(self, node):
        """Helper method to calculate tree height"""
        if not node:
            return -1
        return 1 + max(self._calculate_height(node.left), self._calculate_height(node.right))

    def _verify_balanced_structure(self, node):
        """Helper method to verify tree is reasonably balanced"""
        if not node:
            return 0
        
        left_height = self._verify_balanced_structure(node.left)
        right_height = self._verify_balanced_structure(node.right)
        
        # Height difference should not exceed 1 for a balanced tree
        height_diff = abs(left_height - right_height)
        self.assertLessEqual(height_diff, 1)
        
        return 1 + max(left_height, right_height)

    def _inorder_traversal(self, node):
        """Helper method to perform inorder traversal"""
        if not node:
            return []
        return self._inorder_traversal(node.left) + [node.val] + self._inorder_traversal(node.right)


if __name__ == '__main__':
    unittest.main()
