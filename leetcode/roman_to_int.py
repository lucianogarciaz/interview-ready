import unittest

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        myDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        j = 0
        for i, val in enumerate(s):
            j+=1
            if j<len(s) and myDict[s[j]]>myDict[s[i]]:
                sum -= myDict[s[i]]
                continue

            sum += myDict[s[i]]
        
        return sum

class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "III"
        expected = 3
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)

    def test_example_2(self):
        s = "LVIII"
        expected = 58
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)

    def test_example_3(self):
        s = "IV"
        expected = 4
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)

    def test_example_4(self):
        s = "IX"
        expected = 9
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)

    def test_example_5(self):
        s = "MCMXCIV"
        expected = 1994
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)

    def test_single_symbol(self):
        s = "V"
        expected = 5
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)

    def test_subtractive_notation(self):
        s = "XLIX"  # 49: XL (40) + IX (9)
        expected = 49
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)

        s2 = "XCIX"  # 99: XC (90) + IX (9)
        expected2 = 99
        result2 = self.solution.romanToInt(s2)
        self.assertEqual(result2, expected2)

        s3 = "CDXLIV"  # 444: CD (400) + XL (40) + IV (4)
        expected3 = 444
        result3 = self.solution.romanToInt(s3)
        self.assertEqual(result3, expected3)

if __name__ == '__main__':
    unittest.main()