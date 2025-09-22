from typing import List
import unittest

class Solution:
    def plusOne(self, digits: List[int])->List[int]:
        i = len(digits)-1
        carry=True

        while carry and i>=0:
            if digits[i]<9:
                digits[i]=digits[i]+1
                carry=False
                break
            digits[i]=0
            i-=1
        
        if carry:
            digits = [1]+ digits
        return digits

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_digit_no_carry(self):
        self.assertEqual(self.solution.plusOne([1]), [2])

    def test_single_digit_with_carry(self):
        self.assertEqual(self.solution.plusOne([9]), [1,0])

    def test_multiple_digits_no_carry(self):
        self.assertEqual(self.solution.plusOne([1,2,3]), [1,2,4])

    def test_multiple_digits_with_carry(self):
        self.assertEqual(self.solution.plusOne([1,2,9]), [1,3,0])

    def test_all_nines(self):
        self.assertEqual(self.solution.plusOne([9,9,9]), [1,0,0,0])

    def test_trailing_nines(self):
        self.assertEqual(self.solution.plusOne([2,9,9]), [3,0,0])

    def test_zero(self):
        self.assertEqual(self.solution.plusOne([0]), [1])

    def test_large_input(self):
        digits = [9]*1000
        expected = [1] + [0]*1000
        self.assertEqual(self.solution.plusOne(digits), expected)

if __name__ == "__main__":
    unittest.main()
