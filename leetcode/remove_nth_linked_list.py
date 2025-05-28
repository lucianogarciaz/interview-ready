import unittest
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for i in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next

class TestRemoveNthFromEnd(unittest.TestCase):
    def create_linked_list(self, values: list[int]) -> Optional[ListNode]:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head: Optional[ListNode]) -> list[int]:
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_empty_list(self):
        solution = Solution()
        self.assertIsNone(solution.removeNthFromEnd(None, 1))

    def test_single_node(self):
        solution = Solution()
        head = ListNode(1)
        result = solution.removeNthFromEnd(head, 1)
        self.assertIsNone(result)

    def test_remove_first_node(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = solution.removeNthFromEnd(head, 5)
        self.assertEqual(self.linked_list_to_list(result), [2, 3, 4, 5])

    def test_remove_last_node(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = solution.removeNthFromEnd(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 4])

    def test_remove_middle_node(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = solution.removeNthFromEnd(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 4, 5])

if __name__ == '__main__':
    unittest.main()
