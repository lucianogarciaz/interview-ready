import unittest
from typing import List, Callable
from collections import deque
from inorder_traversal import TreeNode

class Solution:
    def dfsRecursive(self, node:TreeNode, visit:Callable[[TreeNode],None])->None:
        if not node:
            return
        
        visit(node)
        self.dfsRecursive(node.left, visit)
        self.dfsRecursive(node.right, visit)
    def dfs(self, node:TreeNode, visit:Callable[[TreeNode],None])->None:
        if not node:
            return
        stack = deque([node])
        while stack:
            son = stack.pop()
            visit(son)
            if son.right:
                stack.append(son.right)
            if son.left:
                stack.append(son.left)
            
    def bfs(self, node:TreeNode, visit:Callable[[TreeNode], None])->None:
        if not node:
            return
        queue = deque([node])
        while queue:
            son = queue.popleft()
            visit(son)
            if son.left:
                queue.append(son.left)
            if son.right:
                queue.append(son.right)


class TestTreeTraversals(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
        # Create test tree:
        #       1
        #      / \
        #     2   3
        #    / \   \
        #   4   5   6
        #  /
        # 7
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.right = TreeNode(6)
        self.root.left.left.left = TreeNode(7)
        
        # Create single node tree
        self.single_node = TreeNode(10)
        
        # Create empty tree (None)
        self.empty_tree = None

    def test_dfs_recursive_preorder(self):
        """Test DFS recursive traversal (preorder: root, left, right)"""
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.dfsRecursive(self.root, visit_func)
        expected = [1, 2, 4, 7, 5, 3, 6]
        self.assertEqual(result, expected)

    def test_dfs_recursive_single_node(self):
        """Test DFS recursive on single node"""
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.dfsRecursive(self.single_node, visit_func)
        self.assertEqual(result, [10])

    def test_dfs_recursive_empty_tree(self):
        """Test DFS recursive on empty tree"""
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.dfsRecursive(self.empty_tree, visit_func)
        self.assertEqual(result, [])

    def test_dfs_iterative_preorder(self):
        """Test DFS iterative traversal (preorder: root, left, right)"""
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.dfs(self.root, visit_func)
        expected = [1, 2, 4, 7, 5, 3, 6]
        self.assertEqual(result, expected)

    def test_dfs_iterative_single_node(self):
        """Test DFS iterative on single node"""
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.dfs(self.single_node, visit_func)
        self.assertEqual(result, [10])

    def test_dfs_iterative_empty_tree(self):
        """Test DFS iterative on empty tree"""
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.dfs(self.empty_tree, visit_func)
        self.assertEqual(result, [])

    def test_bfs_level_order(self):
        """Test BFS traversal (level order)"""
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.bfs(self.root, visit_func)
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(result, expected)

    def test_bfs_single_node(self):
        """Test BFS on single node"""
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.bfs(self.single_node, visit_func)
        self.assertEqual(result, [10])

    def test_bfs_empty_tree(self):
        """Test BFS on empty tree"""
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.bfs(self.empty_tree, visit_func)
        self.assertEqual(result, [])

    def test_bfs_left_skewed_tree(self):
        """Test BFS on left-skewed tree"""
        # Create left-skewed tree: 1 -> 2 -> 3 -> 4
        left_skewed = TreeNode(1)
        left_skewed.left = TreeNode(2)
        left_skewed.left.left = TreeNode(3)
        left_skewed.left.left.left = TreeNode(4)
        
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.bfs(left_skewed, visit_func)
        expected = [1, 2, 3, 4]
        self.assertEqual(result, expected)

    def test_bfs_right_skewed_tree(self):
        """Test BFS on right-skewed tree"""
        # Create right-skewed tree: 1 -> 2 -> 3 -> 4
        right_skewed = TreeNode(1)
        right_skewed.right = TreeNode(2)
        right_skewed.right.right = TreeNode(3)
        right_skewed.right.right.right = TreeNode(4)
        
        result = []
        visit_func = lambda node: result.append(node.val)
        
        self.solution.bfs(right_skewed, visit_func)
        expected = [1, 2, 3, 4]
        self.assertEqual(result, expected)

    def test_dfs_vs_bfs_order_difference(self):
        """Test that DFS and BFS produce different orders for the same tree"""
        dfs_result = []
        bfs_result = []
        
        dfs_visit = lambda node: dfs_result.append(node.val)
        bfs_visit = lambda node: bfs_result.append(node.val)
        
        self.solution.dfs(self.root, dfs_visit)
        self.solution.bfs(self.root, bfs_visit)
        
        # DFS preorder: [1, 2, 4, 7, 5, 3, 6]
        # BFS level order: [1, 2, 3, 4, 5, 6, 7]
        self.assertNotEqual(dfs_result, bfs_result)
        self.assertEqual(set(dfs_result), set(bfs_result))  # Same elements, different order

    def test_visit_function_side_effects(self):
        """Test that visit function can have side effects"""
        counter = {'count': 0}
        
        def counting_visit(node):
            counter['count'] += 1
        
        self.solution.dfsRecursive(self.root, counting_visit)
        self.assertEqual(counter['count'], 7)  # 7 nodes in the tree
        
        counter['count'] = 0
        self.solution.dfs(self.root, counting_visit)
        self.assertEqual(counter['count'], 7)
        
        counter['count'] = 0
        self.solution.bfs(self.root, counting_visit)
        self.assertEqual(counter['count'], 7)

    def test_visit_function_with_node_attributes(self):
        """Test visit function that accesses node attributes"""
        def sum_visit(node):
            # Simple sum calculation - just add the node value to a running total
            if not hasattr(node, 'total_sum'):
                node.total_sum = 0
            node.total_sum = node.val
        
        # This test ensures the visit function can modify node attributes
        self.solution.dfsRecursive(self.root, sum_visit)
        # Verify that all nodes have been visited and have the total_sum attribute
        all_nodes = []
        def collect_nodes(node):
            if node:
                all_nodes.append(node)
        
        self.solution.dfsRecursive(self.root, collect_nodes)
        
        # Check that all nodes have been visited and have the attribute
        for node in all_nodes:
            self.assertTrue(hasattr(node, 'total_sum'))
            self.assertEqual(node.total_sum, node.val)


if __name__ == '__main__':
    unittest.main()
