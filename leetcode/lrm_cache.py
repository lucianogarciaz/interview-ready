# tail:LRU x  y z head:MRU
# get: get the value from the map, update the lru as the most recent used
# put: add the new value to the head, and what it was the head update make it the second one. 
# If capacity is out of range: delete the LRU and delete that element from the map
# insert and delete
# inserting: change prev from next element and next from previous element
# delete: 
import unittest
class Solution:
    def __init__(self, capacity: int):
        self.capacity:int = capacity
        self.tail = None
        self.head = None
        self.mapLink = {self.tail: None, self.head: None}
    def put(self, key:int, val:int):
        pass
    def get(self, key:int)-> int:
        pass


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