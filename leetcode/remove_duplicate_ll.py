from typing import Optional
import unittest

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    # 1 -> 2 -> 1 -> 3 -> 1
    def deleteDuplicates(self, head: Optional[ListNode])->Optional[ListNode]:
        curr = head
        while curr:
            fast = curr
            # [2, 2, 2]
            # cur    fast   
            #  0       0
            while fast:
                if fast.next and fast.next.val == curr.val:
                    fast.next = fast.next.next
                    continue
                fast = fast.next
            curr = curr.next
        return head


class TestDeleteDuplicates(unittest.TestCase):
    def list_to_linkedlist(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        curr = head
        for val in lst[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def linkedlist_to_list(self, head):
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        head = self.list_to_linkedlist([1,1,2])
        expected = [1,2]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), expected)

    def test_example2(self):
        head = self.list_to_linkedlist([1,1,2,3,3])
        expected = [1,2,3]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), expected)

    def test_empty_list(self):
        head = self.list_to_linkedlist([])
        expected = []
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), expected)

    def test_single_element(self):
        head = self.list_to_linkedlist([5])
        expected = [5]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), expected)

    def test_all_duplicates(self):
        head = self.list_to_linkedlist([2,2,2,2,2])
        expected = [2]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), expected)

    def test_no_duplicates(self):
        head = self.list_to_linkedlist([1,2,3,4,5])
        expected = [1,2,3,4,5]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), expected)

    def test_alternating_duplicates(self):
        head = self.list_to_linkedlist([1,1,2,2,3,3,4,4,5,5])
        expected = [1,2,3,4,5]
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(self.linkedlist_to_list(result), expected)

if __name__ == "__main__":
    unittest.main()
