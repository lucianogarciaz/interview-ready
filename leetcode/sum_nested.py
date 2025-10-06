import unittest

# [6, [2,3], 5]
class Solution:
    def sum_nested(self, x):
        if not x:
            return 0
        
        if isinstance(x[0], (int,float)):
            return x[0] + self.sum_nested(x[1:])
        else:
            return self.sum_nested(x[0]) + self.sum_nested(x[1:])


class TestSumNested(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty_list(self):
        self.assertEqual(self.s.sum_nested([]), 0)

    def test_flat_list(self):
        data = [1, 2, 3]
        self.assertEqual(self.s.sum_nested(data.copy()), 6)

    def test_simple_nested(self):
        data = [6, [2, 3], 5]
        self.assertEqual(self.s.sum_nested([*data]), 16)

    def test_deeply_nested(self):
        data = [[[[1]]], 2, [3, [4, [5]]]]
        self.assertEqual(self.s.sum_nested([*data]), 15)

    def test_with_floats(self):
        data = [1.5, [2.5, [3]], 3.0]
        self.assertAlmostEqual(self.s.sum_nested([*data]), 10.0)

    def test_with_negatives(self):
        data = [-1, [2, [-3, 4]], -2]
        self.assertEqual(self.s.sum_nested([*data]), 0)


if __name__ == '__main__':
    unittest.main()