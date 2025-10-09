import unittest
from typing import Dict

class ListNode:
    def __init__(self, key:int, val:int):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
class Solution:
    def __init__(self, capacity: int):
        self.capacity:int = capacity
        self.tail = None
        self.head = None
        self.mapll = {}
    def put(self, key:int, val:int):
        if key in self.mapll:
            node = self.mapll[key]
            self.remove(node)
            node.val = val
            self.insert(node)
        else:
            node = ListNode(key,val)
            self.insert(node)
            if self.capacity < len(self.mapll):
                # evict
                evict = self.head
                if evict: #this should always be true
                    self.remove(evict)

    def get(self, key:int)-> int:
        if key not in self.mapll:
            return -1
        node = self.mapll[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def insert(self, node:ListNode):
        node.next = None
        if self.tail:
            self.tail.next=node
        else:
            self.head = node
        self.tail = node
        self.mapll[node.key] = node
    def remove(self, node:ListNode):
        pr, ne = node.prev, node.next
        if pr:
            pr.next = ne
        else:
            self.head = ne
        if ne:
            ne.prev = pr
        else:
            self.tail = pr
        if node.key in self.mapll:
            del self.mapll[node.key]
        

class TestLRUCache(unittest.TestCase):
    def test_lru_cache(self):
        # Test case 1: Basic operations
        lru = Solution(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)
        lru.put(3, 3)
        self.assertEqual(lru.get(2), -1)
        lru.put(4, 4)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)

        # Test case 2: Update existing key
        lru = Solution(2)
        lru.put(1, 1)
        lru.put(2, 2)
        lru.put(1, 10)
        self.assertEqual(lru.get(1), 10)
        self.assertEqual(lru.get(2), 2)

        # Test case 3: Capacity of 1
        lru = Solution(1)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(2), 2)

        # Test case 4: Empty cache
        lru = Solution(2)
        self.assertEqual(lru.get(1), -1)

if __name__ == "__main__":
    unittest.main()