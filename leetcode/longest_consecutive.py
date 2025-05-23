from typing import List
import unittest

def longestConsecutive(nums: List[int]) -> int:
    if len(nums)<=1:
        return len(nums)
    
    hash = set(nums)
    seq = 1
    for v in hash:
        if v-1 in hash:
            continue
        l = 1
        while v+l in hash:
            l+=1
        seq = max(seq,l)
    
    return seq
    

class TestLongestConsecutive(unittest.TestCase):
    def test_example1(self):
        nums = [100, 4, 200, 1, 3, 2]
        expected = 4  # The longest consecutive sequence is [1,2,3,4]
        result = longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        expected = 9  # The longest consecutive sequence is [0,1,2,3,4,5,6,7,8]
        result = longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_empty_array(self):
        nums = []
        expected = 0
        result = longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [1]
        expected = 1
        result = longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_no_consecutive(self):
        nums = [1, 3, 5, 7]
        expected = 1  # Each number forms its own sequence of length 1
        result = longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_duplicate_numbers(self):
        nums = [1, 2, 2, 3, 3, 3, 4]
        expected = 4  # The longest consecutive sequence is [1,2,3,4]
        result = longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        nums = [-3, -2, -1, 0, 1]
        expected = 5  # The longest consecutive sequence is [-3,-2,-1,0,1]
        result = longestConsecutive(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 