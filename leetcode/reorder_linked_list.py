import unittest
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head:Optional[ListNode]):
        if not head:
            return 
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow = it's in the middle of the list
        # fast = is at the end.
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        # first = 1 2 3   second = 4 5
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
class TestReorderList(unittest.TestCase):
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
        head = None
        solution.reorderList(head)
        self.assertIsNone(head)

    def test_single_node(self):
        solution = Solution()
        head = ListNode(1)
        solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1])

    def test_two_nodes(self):
        solution = Solution()
        head = self.create_linked_list([1, 2])
        solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 2])

    def test_multiple_nodes(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4])
        solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 4, 2, 3])

    def test_odd_number_of_nodes(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 5, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()
