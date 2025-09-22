from typing import List
import unittest

class Solution:
    def addBinary(self,a:str, b:str)->str:
        i=len(a)-1
        j=len(b)-1
        carry = False
        res = []
        while i>=0 or j>=0:
            vala = a[i] if i>=0 else '0'
            valb= b[j] if j>=0 else '0'
            inter = '0'
            if carry:
                inter = '1'
                carry = False
            
            if vala == '1' and valb == '1':
                carry = True
            elif vala == '1' or valb == '1':
                if inter == '1':
                    carry = True
                    inter = '0'
                else:
                    inter = '1'
            
            res.insert(0,inter)
            i-=1
            j-=1
        
        if carry:
            res.insert(0,'1')
        return ''.join(res)


class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_addition(self):
        self.assertEqual(self.solution.addBinary("11", "1"), "100")
        self.assertEqual(self.solution.addBinary("1010", "1011"), "10101")
        self.assertEqual(self.solution.addBinary("0", "0"), "0")
        self.assertEqual(self.solution.addBinary("1", "0"), "1")
        self.assertEqual(self.solution.addBinary("0", "1"), "1")

    def test_carry_over(self):
        self.assertEqual(self.solution.addBinary("111", "1"), "1000")
        self.assertEqual(self.solution.addBinary("1", "111"), "1000")
        self.assertEqual(self.solution.addBinary("1111", "1"), "10000")

    def test_different_lengths(self):
        self.assertEqual(self.solution.addBinary("101", "10"), "111")
        self.assertEqual(self.solution.addBinary("1", "10000"), "10001")
        self.assertEqual(self.solution.addBinary("100", "110010"), "110110")

    def test_large_inputs(self):
        a = "1" * 100
        b = "1"
        expected = "1" + "0" * 100
        self.assertEqual(self.solution.addBinary(a, b), expected)

    # def test_leading_zeros(self):
    #     self.assertEqual(self.solution.addBinary("0001", "001"), "10")
    #     self.assertEqual(self.solution.addBinary("000", "000"), "0")

    # def test_empty_strings(self):
    #     self.assertEqual(self.solution.addBinary("", ""), "0")
    #     self.assertEqual(self.solution.addBinary("0", ""), "0")
    #     self.assertEqual(self.solution.addBinary("", "1"), "1")

if __name__ == "__main__":
    unittest.main()
