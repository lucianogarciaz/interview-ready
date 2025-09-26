import unittest
from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    # 1-2-2-3-4-6   k = 2
    def kthToLast(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <0:
            return None
        count = 0
        cur = head
        while cur:
            count+=1
            cur = cur.next
        
        if k >count:  # this mean that the k element is greater than the length of the ll
            return None

        nr = count-k
        cur = head
        for i in range(nr):
            cur = cur.next
        
        return cur



class TestKthToLast(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def create_linked_list(self, values):
        """Helper method to create a linked list from a list of values"""
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_list(self, head):
        """Helper method to convert linked list to Python list for easy comparison"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def test_single_node_k1(self):
        """Test with single node, k=1 (should return the only node)"""
        head = self.create_linked_list([1])
        result = self.solution.kthToLast(head, 1)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)
    
    # def test_single_node_k_greater_than_length(self):
    #     """Test with single node, k=2 (should return None)"""
    #     head = self.create_linked_list([1])
    #     result = self.solution.kthToLast(head, 2)
    #     self.assertIsNone(result)
    
    def test_two_nodes_k1(self):
        """Test with two nodes, k=1 (should return last node)"""
        head = self.create_linked_list([1, 2])
        result = self.solution.kthToLast(head, 1)
        self.assertEqual(result.val, 2)
        self.assertIsNone(result.next)
    
    def test_two_nodes_k2(self):
        """Test with two nodes, k=2 (should return first node)"""
        head = self.create_linked_list([1, 2])
        result = self.solution.kthToLast(head, 2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
    
    def test_three_nodes_k1(self):
        """Test with three nodes, k=1 (should return last node)"""
        head = self.create_linked_list([1, 2, 3])
        result = self.solution.kthToLast(head, 1)
        self.assertEqual(result.val, 3)
        self.assertIsNone(result.next)
    
    def test_three_nodes_k2(self):
        """Test with three nodes, k=2 (should return second node)"""
        head = self.create_linked_list([1, 2, 3])
        result = self.solution.kthToLast(head, 2)
        self.assertEqual(result.val, 2)
        self.assertEqual(result.next.val, 3)
    
    def test_three_nodes_k3(self):
        """Test with three nodes, k=3 (should return first node)"""
        head = self.create_linked_list([1, 2, 3])
        result = self.solution.kthToLast(head, 3)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
    
    def test_five_nodes_k2(self):
        """Test with five nodes, k=2 (should return 4th node)"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.kthToLast(head, 2)
        self.assertEqual(result.val, 4)
        self.assertEqual(result.next.val, 5)
    
    def test_five_nodes_k5(self):
        """Test with five nodes, k=5 (should return first node)"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.kthToLast(head, 5)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
    
    def test_k_greater_than_length(self):
        """Test with k greater than list length (should return None)"""
        head = self.create_linked_list([1, 2, 3])
        result = self.solution.kthToLast(head, 5)
        self.assertIsNone(result)
    
    def test_k_zero(self):
        """Test with k=0 (edge case, should return None)"""
        head = self.create_linked_list([1, 2, 3])
        result = self.solution.kthToLast(head, 0)
        self.assertIsNone(result)
    
    def test_empty_list(self):
        """Test with empty list (should return None)"""
        head = None
        result = self.solution.kthToLast(head, 1)
        self.assertIsNone(result)
    
    def test_negative_k(self):
        """Test with negative k (edge case, should return None)"""
        head = self.create_linked_list([1, 2, 3])
        result = self.solution.kthToLast(head, -1)
        self.assertIsNone(result)
    
    def test_large_list(self):
        """Test with larger list to verify performance"""
        values = list(range(1, 101))  # 1 to 100
        head = self.create_linked_list(values)
        result = self.solution.kthToLast(head, 50)
        self.assertEqual(result.val, 51)  # 50th from last should be 51


if __name__ == "__main__":
    unittest.main()

