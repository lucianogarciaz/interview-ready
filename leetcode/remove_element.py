from typing import List
import unittest

class Solution:
    # nums      write_index    read_index   for val =2
    # [3,2,2,3]     0           0
    # [3,2,2,3]     1           1
    # [3,2,2,3]     1           2
    # [3,2,2,3]     1           3
    # [3,3,2,3]     2           3
    

    def remove_element(self, nums:List[int], val:int)-> int:
        write_index = 0 
        for read_index in range(len(nums)):
            if val!= nums[read_index]:
                nums[write_index]= nums[read_index]
                write_index+=1
            
        return write_index



class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [3,2,2,3]
        val = 3
        expected_nums = [2,2]
        k = self.solution.remove_element(nums, val)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(sorted(nums[:k]), sorted(expected_nums))

    def test_example2(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        expected_nums = [0,1,3,0,4]
        k = self.solution.remove_element(nums, val)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(sorted(nums[:k]), sorted(expected_nums))

    def test_no_removal(self):
        nums = [1,2,3,4]
        val = 5
        expected_nums = [1,2,3,4]
        k = self.solution.remove_element(nums, val)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(sorted(nums[:k]), sorted(expected_nums))

    def test_remove_all(self):
        nums = [1,1,1,1]
        val = 1
        expected_nums = []
        k = self.solution.remove_element(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], expected_nums)

    def test_empty_list(self):
        nums = []
        val = 0
        expected_nums = []
        k = self.solution.remove_element(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], expected_nums)

    def test_single_element_remove(self):
        nums = [1]
        val = 1
        expected_nums = []
        k = self.solution.remove_element(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], expected_nums)

    def test_single_element_keep(self):
        nums = [2]
        val = 1
        expected_nums = [2]
        k = self.solution.remove_element(nums, val)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], expected_nums)

    def test_large_input(self):
        nums = [2]*1000 + [3]*1000 + [4]*1000
        val = 3
        expected_nums = [2]*1000 + [4]*1000
        k = self.solution.remove_element(nums, val)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(sorted(nums[:k]), sorted(expected_nums))

if __name__ == "__main__":
    unittest.main()
