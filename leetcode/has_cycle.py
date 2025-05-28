import unittest

class ListNode:
    def __init__(self, x=0, next=None) -> None:
        self.next = next
        self.val = x

class Solution: 
    def hasCycle(self, l: ListNode)->bool:
        seen = set()

        while l:
            if l in seen:
                return True
            seen.add(l)
            l = l.next
        return False
class Solution2:
    def hasCycle(self, l:ListNode)->bool:
        slow, fast = l,l
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

class TestHasCycle(unittest.TestCase):
    def create_linked_list(self, values: list[int], pos: int = -1) -> ListNode:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        nodes = [head]
        
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
            nodes.append(current)
            
        if pos >= 0:
            current.next = nodes[pos]
            
        return head

    def test_empty_list(self):
        solution = Solution()
        self.assertFalse(solution.hasCycle(None))
        solution = Solution2()
        self.assertFalse(solution.hasCycle(None))

    def test_single_node_no_cycle(self):
        solution = Solution()
        head = ListNode(1)
        self.assertFalse(solution.hasCycle(head))
        solution = Solution2()
        head = ListNode(1)
        self.assertFalse(solution.hasCycle(head))
                

    def test_single_node_with_cycle(self):
        solution = Solution()
        head = ListNode(1)
        head.next = head
        self.assertTrue(solution.hasCycle(head))
        solution = Solution2()
        head = ListNode(1)
        head.next = head
        self.assertTrue(solution.hasCycle(head))
        

    def test_multiple_nodes_no_cycle(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4])
        self.assertFalse(solution.hasCycle(head))
        solution = Solution2()
        head = self.create_linked_list([1, 2, 3, 4])
        self.assertFalse(solution.hasCycle(head))

    def test_multiple_nodes_with_cycle(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4], 1)  # Creates cycle at index 1
        self.assertTrue(solution.hasCycle(head))
        solution = Solution2()
        head = self.create_linked_list([1, 2, 3, 4], 1)  # Creates cycle at index 1
        self.assertTrue(solution.hasCycle(head))

if __name__ == '__main__':
    unittest.main()
