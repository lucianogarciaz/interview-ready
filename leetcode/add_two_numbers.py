from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            res = v1 + v2 + carry
            carry = res//10
            res = res % 10

            cur.next = ListNode(res)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
    

class TestAddTwoNumbers(unittest.TestCase):
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

    def test_empty_lists(self):
        solution = Solution()
        self.assertIsNone(solution.addTwoNumbers(None, None))

    def test_one_empty_list(self):
        solution = Solution()
        list1 = self.create_linked_list([1, 2, 3])
        result = solution.addTwoNumbers(list1, None)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3])

    def test_same_length_lists(self):
        solution = Solution()
        list1 = self.create_linked_list([2, 4, 3])
        list2 = self.create_linked_list([5, 6, 4])
        result = solution.addTwoNumbers(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [7, 0, 8])

    def test_different_length_lists(self):
        solution = Solution()
        list1 = self.create_linked_list([9, 9, 9, 9, 9, 9, 9])
        list2 = self.create_linked_list([9, 9, 9, 9])
        result = solution.addTwoNumbers(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

if __name__ == '__main__':
    unittest.main()