import unittest
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode])->Optional[ListNode]:
        res = ListNode()
        head = res

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        
        return res.next
    
class TestMergeTwoLists(unittest.TestCase):
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
        self.assertIsNone(solution.mergeTwoLists(None, None))

    def test_one_empty_list(self):
        solution = Solution()
        list1 = self.create_linked_list([1, 2, 3])
        result = solution.mergeTwoLists(list1, None)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3])

    def test_both_lists_have_values(self):
        solution = Solution()
        list1 = self.create_linked_list([1, 2, 4])
        list2 = self.create_linked_list([1, 3, 4])
        result = solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [1, 1, 2, 3, 4, 4])

    def test_different_length_lists(self):
        solution = Solution()
        list1 = self.create_linked_list([1, 3, 5])
        list2 = self.create_linked_list([2, 4, 6, 8, 10])
        result = solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 4, 5, 6, 8, 10])

if __name__ == '__main__':
    unittest.main()
