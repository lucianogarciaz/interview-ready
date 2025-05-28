from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

class TestReverseList(unittest.TestCase):
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
        self.assertIsNone(solution.reverseList(None))

    def test_single_node(self):
        solution = Solution()
        head = ListNode(1)
        result = solution.reverseList(head)
        self.assertEqual(self.linked_list_to_list(result), [1])

    def test_two_nodes(self):
        solution = Solution()
        head = self.create_linked_list([1, 2])
        result = solution.reverseList(head)
        self.assertEqual(self.linked_list_to_list(result), [2, 1])

    def test_multiple_nodes(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = solution.reverseList(head)
        self.assertEqual(self.linked_list_to_list(result), [5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()
