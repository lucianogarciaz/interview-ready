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
    
    # 1-2-3-4-5
    def deleteMiddleNode(self, node: Optional[ListNode]) -> bool:
        if not node or not node.next:
            return False
        
        node.val = node.next.val
        node.next = node.next.next

        return True

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


class TestDeleteMiddleNode(unittest.TestCase):
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
    
    def test_delete_middle_node_three_elements(self):
        """Test deleting middle node from [1,2,3] -> should become [1,3]"""
        head = self.create_linked_list([1, 2, 3])
        middle_node = head.next  # node with value 2
        
        result = self.solution.deleteMiddleNode(middle_node)
        self.assertTrue(result)
        
        # Verify the list is now [1, 3]
        self.assertEqual(self.linked_list_to_list(head), [1, 3])
    
    def test_delete_middle_node_five_elements(self):
        """Test deleting middle node from [1,2,3,4,5] -> should become [1,2,4,5]"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        middle_node = head.next.next  # node with value 3
        
        result = self.solution.deleteMiddleNode(middle_node)
        self.assertTrue(result)
        
        # Verify the list is now [1, 2, 4, 5]
        self.assertEqual(self.linked_list_to_list(head), [1, 2, 4, 5])
    
    def test_delete_second_node_four_elements(self):
        """Test deleting second node from [1,2,3,4] -> should become [1,3,4]"""
        head = self.create_linked_list([1, 2, 3, 4])
        second_node = head.next  # node with value 2
        
        result = self.solution.deleteMiddleNode(second_node)
        self.assertTrue(result)
        
        # Verify the list is now [1, 3, 4]
        self.assertEqual(self.linked_list_to_list(head), [1, 3, 4])
    
    def test_delete_third_node_five_elements(self):
        """Test deleting third node from [1,2,3,4,5] -> should become [1,2,4,5]"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        third_node = head.next.next  # node with value 3
        
        result = self.solution.deleteMiddleNode(third_node)
        self.assertTrue(result)
        
        # Verify the list is now [1, 2, 4, 5]
        self.assertEqual(self.linked_list_to_list(head), [1, 2, 4, 5])
    
    def test_delete_last_node_three_elements(self):
        """Test deleting last node from [1,2,3] -> should fail (not middle)"""
        head = self.create_linked_list([1, 2, 3])
        last_node = head.next.next  # node with value 3
        
        result = self.solution.deleteMiddleNode(last_node)
        self.assertFalse(result)
        
        # Verify the list is unchanged [1, 2, 3]
        self.assertEqual(self.linked_list_to_list(head), [1, 2, 3])
    
    def test_delete_first_node_three_elements(self):
        """Test deleting first node from [1,2,3] -> should become [2,3]"""
        head = self.create_linked_list([1, 2, 3])
        print(head.val)
        first_node = head  # node with value 1
        
        result = self.solution.deleteMiddleNode(first_node)
        self.assertTrue(result)
        
        # Verify the list is now [2, 3] (first node replaced with second node's data)
        self.assertEqual(self.linked_list_to_list(head), [2, 3])
    
    def test_delete_node_single_element(self):
        """Test deleting from single element list -> should fail"""
        head = self.create_linked_list([1])
        single_node = head
        
        result = self.solution.deleteMiddleNode(single_node)
        self.assertFalse(result)
        
        # Verify the list is unchanged [1]
        self.assertEqual(self.linked_list_to_list(head), [1])
    
    def test_delete_node_two_elements(self):
        """Test deleting from two element list"""
        head = self.create_linked_list([1, 2])
        first_node = head
        second_node = head.next
        
        # Try deleting first node (should succeed, becomes [2])
        result1 = self.solution.deleteMiddleNode(first_node)
        self.assertTrue(result1)
        self.assertEqual(self.linked_list_to_list(head), [2])
        
        # Reset for second test
        head = self.create_linked_list([1, 2])
        second_node = head.next
        
        # Try deleting second node (should fail - no next node to copy from)
        result2 = self.solution.deleteMiddleNode(second_node)
        self.assertFalse(result2)
        
        # Verify the list is unchanged [1, 2]
        self.assertEqual(self.linked_list_to_list(head), [1, 2])
    
    def test_delete_node_none(self):
        """Test deleting None node -> should fail"""
        result = self.solution.deleteMiddleNode(None)
        self.assertFalse(result)
    
    def test_delete_middle_large_list(self):
        """Test deleting middle node from larger list"""
        values = list(range(1, 11))  # [1,2,3,4,5,6,7,8,9,10]
        head = self.create_linked_list(values)
        middle_node = head.next.next.next.next  # node with value 5
        
        result = self.solution.deleteMiddleNode(middle_node)
        self.assertTrue(result)
        
        # Verify the list is now [1,2,3,4,6,7,8,9,10]
        expected = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        self.assertEqual(self.linked_list_to_list(head), expected)
    
    def test_delete_node_with_duplicates(self):
        """Test deleting node with duplicate values"""
        head = self.create_linked_list([1, 2, 2, 3, 4])
        duplicate_node = head.next.next  # second node with value 2
        
        result = self.solution.deleteMiddleNode(duplicate_node)
        self.assertTrue(result)
        
        # Verify the list is now [1, 2, 3, 4]
        self.assertEqual(self.linked_list_to_list(head), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()

