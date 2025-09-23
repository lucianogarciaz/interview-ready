import unittest
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        writePosition = len(nums1)-1

        m = m-1
        n=n-1

        while m>=0 and n >= 0:
            if  m>=0 and n>=0 and nums1[m] > nums2[n]:
                nums1[writePosition] = nums1[m]
                m-=1
            else:
                nums1[writePosition] = nums2[n]
                n-=1
            writePosition-=1

        while n>=0 and writePosition>=0:
            nums1[writePosition]=nums2[n]
            n-=1
            writePosition-=1
        


class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,2,3,5,6])

    def test_case2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_case3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_case4(self):
        nums1 = [2,0]
        m = 1
        nums2 = [1]
        n = 1
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2])

    def test_case5(self):
        nums1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        m = 0
        nums2 = [-50,-50,-48,-47,-44,-44,-37,-35,-35,-32,-32,-31,-29,-29,-28,-26,-24,-23,-23,-21,-20,-19,-17,-15,-14,-12,-12,-11,-10,-9,-8,-5,-2,-2,1,1,3,4,4,7,7,7,9,10,11,12,14,16,17,18,21,21,24,31,33,34,35,36,41,41,46,48,48]
        n = 63
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [-50,-50,-48,-47,-44,-44,-37,-35,-35,-32,-32,-31,-29,-29,-28,-26,-24,-23,-23,-21,-20,-19,-17,-15,-14,-12,-12,-11,-10,-9,-8,-5,-2,-2,1,1,3,4,4,7,7,7,9,10,11,12,14,16,17,18,21,21,24,31,33,34,35,36,41,41,46,48,48])

    def test_case6(self):
        nums1 = [0,0,3,0,0,0,0,0,0]
        m = 3
        nums2 = [-1,1,1,1,2,3]
        n = 6
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [-1,0,0,1,1,1,2,3,3])

if __name__ == "__main__":
    unittest.main()
