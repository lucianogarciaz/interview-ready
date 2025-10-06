import unittest
from typing import List, Optional
from inorder_traversal import TreeNode
from add_two_numbers import ListNode

class Solution:
    def listOfDepths(self, tree:Optional[TreeNode])->List[ListNode]:
        if not tree:
            return None
        return self.dfs(tree, [], 0)
    
    
    def dfs(self, node: Optional[TreeNode], lists:List[ListNode], level:int )->List[ListNode]:
        if not node:
            return lists
        
        if level < len(lists):
            curr = lists[level]
            p = curr
            while p:
                if not p.next:
                    p.next = ListNode(node.val)
                    break
                else:
                    p = p.next
        else:
            lists.append(ListNode(node.val))

        
        lists = self.dfs(node.left, lists, level + 1)
        return self.dfs(node.right, lists, level + 1)
            

class TestListOfDepths(unittest.TestCase):
    def setUp(self) -> None:
        self.sln = Solution()

    def linked_list_to_list(self, head: Optional[ListNode]):
        result = []
        node = head
        while node:
            result.append(node.val)
            node = node.next
        return result

    def levels_to_lists(self, levels):
        return [self.linked_list_to_list(head) if head else [] for head in (levels or [])]

    def test_empty_tree(self):
        root = None
        result = self.sln.listOfDepths(root)
        expected = []
        if result is None:
            self.assertEqual([], expected)
        else:
            self.assertEqual(self.levels_to_lists(result), expected)

    def test_single_node(self):
        root = TreeNode(1)
        result = self.sln.listOfDepths(root)
        self.assertIsNotNone(result)
        self.assertEqual(self.levels_to_lists(result), [[1]])

    def test_complete_three_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        result = self.sln.listOfDepths(root)
        self.assertIsNotNone(result)
        self.assertEqual(self.levels_to_lists(result), [[1], [2, 3], [4, 5, 6, 7]])

    def test_left_skewed(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        result = self.sln.listOfDepths(root)
        self.assertIsNotNone(result)
        self.assertEqual(self.levels_to_lists(result), [[1], [2], [3], [4]])

    def test_right_skewed(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        result = self.sln.listOfDepths(root)
        self.assertIsNotNone(result)
        self.assertEqual(self.levels_to_lists(result), [[1], [2], [3], [4]])

    def test_sparse_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        result = self.sln.listOfDepths(root)
        self.assertIsNotNone(result)
        self.assertEqual(self.levels_to_lists(result), [[1], [2, 3], [5]])


if __name__ == '__main__':
    unittest.main()
