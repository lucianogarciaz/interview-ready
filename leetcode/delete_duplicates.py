import unittest
from typing import Optional

class ListNode:
    def __init__(self,val = 0, next=None):
            self.val = val
            self.next= next
class Solution:    
    def delete_duplicates(self, head:Optional[ListNode])->Optional[ListNode]:
        node = head
        while node:
            if not node.next:
                break
            if node.next.val == node.val:
                node.next=node.next.next
            else:
                node = node.next
        
        return head



def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    node = head
    for val in lst[1:]:
        node.next = ListNode(val)
        node = node.next
    return head

def linkedlist_to_list(head):
    res = []
    node = head
    while node:
        res.append(node.val)
        node = node.next
    return res

class TestDeleteDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        head = list_to_linkedlist([])
        result = self.solution.delete_duplicates(head)
        self.assertEqual(linkedlist_to_list(result), [])

    def test_single_element(self):
        head = list_to_linkedlist([1])
        result = self.solution.delete_duplicates(head)
        self.assertEqual(linkedlist_to_list(result), [1])

    def test_no_duplicates(self):
        head = list_to_linkedlist([1,2,3])
        result = self.solution.delete_duplicates(head)
        self.assertEqual(linkedlist_to_list(result), [1,2,3])

    def test_all_duplicates(self):
        head = list_to_linkedlist([2,2,2,2])
        result = self.solution.delete_duplicates(head)
        self.assertEqual(linkedlist_to_list(result), [2])

    def test_some_duplicates(self):
        head = list_to_linkedlist([1,1,2,3,3])
        result = self.solution.delete_duplicates(head)
        self.assertEqual(linkedlist_to_list(result), [1,2,3])

    def test_alternating_duplicates(self):
        head = list_to_linkedlist([1,1,2,2,3,3,4,4])
        result = self.solution.delete_duplicates(head)
        self.assertEqual(linkedlist_to_list(result), [1,2,3,4])

    def test_long_list(self):
        head = list_to_linkedlist([1,1,1,2,3,3,4,5,5,5,6])
        result = self.solution.delete_duplicates(head)
        self.assertEqual(linkedlist_to_list(result), [1,2,3,4,5,6])

if __name__ == "__main__":
    unittest.main()

